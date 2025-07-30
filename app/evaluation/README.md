
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

# Prompt Manager and Playground

In the evaluation/ dir you'll find a dir called prompts/. In this one there's a few different categories of prompts I've created with different versions of prompts focusing on different aspects/tasks such as tool calling or pedagogy. The prompt manager will load these prompts onto langsmith where they can be accessed through the left sidebar "prompts" tab. You can experiment with these manually through the playground or compare the prompts side by side as well as iterate and test them.

Run the upload to your dashboard with:
```bash
python -m app.evaluation.prompt_mangager.py
```

- You can create new categories as you want and nothing will break
- The prompt uploader will always choose the latest verison of prompt as long as each yaml file in each category is called v1.yaml, v2.yaml, v3.yaml and so on.

Comming features:
1. Evaluate on the twiga test dataset using different prompts and comparing side by side. This has yet to be implemented since it has to be done programmatically and its missing the tool calls that the agent is in the ai.py file. 