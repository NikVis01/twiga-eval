This is a simple backend for Twiga for AI development.

How to run:
Fill in the `.env`
* Put the Neon DB URI (that I share with you) into DATABASE_URL
* Put your own Together AI API key into LLM_API_KEY (you usually get 5 dollars in free credits)

Run the commands:
`poetry install`
or 
`uv install`

And then:
`source .venv/bin/activate` if on mac/linux, `.venv\Scripts\activate` if on windows. 

Then write:
`uvicorn app.main:app --port 8000 --reload` to start the development FastAPI server

You'll see that the LLM calls aren't implemented yet though.

# Evaluation and Observability

To enable evaluation and observability in your application, configure the following environment variables in your `.env` file:

```env
# Core configuration
DATABASE_URL=<YOUR_DATABASE_URL>
LLM_API_KEY=<YOUR_LLM_API_KEY>

# LangChain evaluation
LANGCHAIN_API_KEY=<YOUR_LANGCHAIN_API_KEY>

# Additonal variables for observability
LANGSMITH_TRACING=true
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=twiga-chatbot
````
Note: LANGCHAIN_PROJECT defines the name displayed in the LangSmith dashboard under “Tracing project”.

## Observability

With tracing enabled and your `ai.py` file updated, LangSmith will automatically record traces while the app runs.

You can view trace history on your [LangSmith dashboard](https://smith.langchain.com) by navigating to:
Tracing project > twiga-chatbot

## Evaluation
To evaluate your model's performance, follow these steps:

### 1. Create or Update the Dataset

Even if the dataset already exists, rerunning this command will add any new examples:

```bash
python -m app.evaluation.create_dataset
```

### 2. Run the Evaluation

Once your dataset is ready, start the evaluation with:

```bash
python -m app.evaluation.model_eval
```
After the evaluation completes, you'll receive a URL with the results. You can also find them in the dashboard under:
Datasets & Experiments > YOUR_DATASET_NAME > Experiments

Note : For more informatation on how to setup everything visit the langsmith docs https://docs.smith.langchain.com/
