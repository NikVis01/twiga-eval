from app.evaluation.chat_models import chat
from app.evaluation.evaluators import (
    correctness_evaluator,
    conciseness_evaluator,
    hallucination_evaluator,
)

from langsmith import Client
from dotenv import load_dotenv
import os
# from langchain_together import ChatTogether
from pydantic import SecretStr
from langchain_core.runnables import RunnableConfig
from langsmith import aevaluate
import asyncio

# Load environment variables
load_dotenv()


client = Client()

print("loading dataset...")
#read the dataset
dataset = client.read_dataset(dataset_name="Twiga Eval Dataset Test")
# Check if the dataset is empty
examples = client.list_examples(dataset_id=dataset.id)
if not examples:
    raise ValueError("The dataset is empty. Please add examples before running the evaluation.")
else:
    print(f"Dataset contains {len(list(examples))} examples.")



#target function that is called by the evaluation framework 
# NOTE: This is a bastic target function that does not use tools or the Twiga system prompt (only use for testing purposes)
async def basic_target(inputs: dict) -> dict:
    api_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": inputs["question"]},
    ]

    config = RunnableConfig(tags=["eval-run"])
    response = await chat.ainvoke(api_messages, config=config)

    print(f"Response: {response.content.strip()}")

    return {
        "answer": response.content.strip()
    }

#target function that evaluates the real Twiga chatbot 
from app.ai import generate_response
from app.database.models import Message, MessageRole, User

async def target(inputs: dict) -> dict:
    """
    print(f"=== PROCESSING EXAMPLE ===")
    print(f"Input: {inputs}")
    """
    try:
        print(f"Processing example: {inputs['question']}")
        # Fake/mock user data for running the evaluation
        user = User(
            id=13,
            name="John Doe",
            wa_id="255712345678",
            role="teacher",
            state="active",
            onboarding_state="completed",
            class_info={"geography": ["os2"]}, 
            # formatted_class_info="Form Two - Geography"  # set manually if your function uses it
        )

        # build the user message with the question form the example
        message = Message(
            role=MessageRole.user,
            user_id=user.id,
            content=inputs["question"]
        )

        #generate the response using the Twiga chatbot, same as when called from WhatsApp, but without history
        response = await generate_response(user=user, message=message, use_history=False)

        
        # print(f"Raw response object: {response}")
        #print(f"Response type: {type(response)}")
        if response:
            print(f"Response content: {response.content}")
            print(f"Response attributes: {dir(response)}")
   
        # print(f"Generated response: {response.content.strip() if response else 'No response.'}")
        result = {"answer": response.content.strip() if response else "No response."}
        # print(f"Output: {result}")
        # print(f"=== END EXAMPLE ===")
        
        return result
        
    except Exception as e:
        
        # print(f"Error processing example: {e}")
        result = {"answer": f"Error: {str(e)}"}
        # print(f"Output: {result}")
        # print(f"=== END EXAMPLE ===")
        
        return result


######### Run the evaluation experiment #########
# after running the evaluation, a link will be provided to view the results in langsmith
async def main():
    print("Starting evaluation experiment...")
    experiment_results = await aevaluate(
        target,
        data="Twiga Eval Dataset Test",
        evaluators=[
                correctness_evaluator,
                conciseness_evaluator, 
                hallucination_evaluator,
        ],
        experiment_prefix="test-eval-in-langsmith",
        max_concurrency=2,
    )
    print("Evaluation complete.")
    print("Results:", experiment_results)


if __name__ == "__main__":
    asyncio.run(main())