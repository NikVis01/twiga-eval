from dotenv import load_dotenv
import os
from langchain_together import ChatTogether
from pydantic import SecretStr
import json
from langchain.schema import HumanMessage


''' 
NOTE: Using a LLM for this classification task is a lot of overhead so for now we will use the hardcoded function below
# Load environment variables
load_dotenv()
LLM_API_KEY = os.getenv("LLM_API_KEY")


query_eval_model = ChatTogether(
    api_key=SecretStr(LLM_API_KEY) if LLM_API_KEY else None,
    model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
    temperature=0.0,
)



async def classify_query_async(query: str) -> dict:
    system_instruction = (
        "You are an assistant that classifies educational chatbot queries.\n"
        "Given a user query, return a JSON with:\n"
        "- query_type: one of ['lesson_plan', 'summary', 'explanation', 'fact_question', 'casual', 'other']\n"
        "- topic: the main subject of the query, like 'agriculture', 'history', 'climate', or 'unknown'\n"
        "Only return a valid JSON string."
    )

    prompt = f"Classify this query:\n\"{query}\"\n\nReturn only JSON."

    try:
        response = await query_eval_model.ainvoke([
            HumanMessage(content=system_instruction),
            HumanMessage(content=prompt)
        ])
        data = json.loads(response.content)
        return {
            "query_type": data.get("query_type", "other"),
            "topic": data.get("topic", "unknown")
        }
    except Exception as e:
        print(f"Classification failed: {e}")
        return {
            "query_type": "other",
            "topic": "unknown"
        }
'''


async def classify_query_async(query: str) -> dict:
    query_lower = query.lower()

    # Simple hardcoded rules to classify query_type
    if any(kw in query_lower for kw in ["lesson plan", "plan for", "create lesson"]):
        query_type = "lesson_plan"
    elif any(kw in query_lower for kw in ["summary", "summarize", "overview"]):
        query_type = "summary"
    elif any(kw in query_lower for kw in ["explain", "explanation", "describe"]):
        query_type = "explanation"
    elif any(kw in query_lower for kw in ["what is", "who is", "when", "where", "fact"]):
        query_type = "fact_question"
    elif any(kw in query_lower for kw in ["hi", "hello", "how are you", "thanks"]):
        query_type = "casual"
    else:
        query_type = "other"

    # Simple hardcoded rules to guess topic
    if "agriculture" in query_lower:
        topic = "agriculture"
    elif "history" in query_lower:
        topic = "history"
    elif "climate" in query_lower:
        topic = "climate"
    else:
        topic = "unknown"

    return {
        "query_type": query_type,
        "topic": topic
    }
