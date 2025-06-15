'''
Basic evaluation of model without tools
TODO: 
- create target function that can do tool calls like the real chatbot
'''

from chat_models import chat, system_prompt
from evaluators import correctness_evaluator, conciseness_evaluator, hallucination_evaluator

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
dataset = client.read_dataset(dataset_name="Twiga Eval Dataset")
# Check if the dataset is empty
examples = client.list_examples(dataset_id=dataset.id)
if not examples:
    raise ValueError("The dataset is empty. Please add examples before running the evaluation.")
else:
    print(f"Dataset contains {len(list(examples))} examples.")



#target function that is called by the evaluation framework 
# TODO: create target function that can do tool calls like the real chatbot
async def target(inputs: dict) -> dict:
    api_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": inputs["question"]},
    ]

    config = RunnableConfig(tags=["eval-run"])
    response = await chat.ainvoke(api_messages, config=config)

    return {
        "answer": response.content.strip()
    }

print("Target function defined. Ready to run evaluation experiment.")


######### Run the evaluation experiment #########
# after running the evaluation, a link will be provided to view the results in langsmith
async def main():
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