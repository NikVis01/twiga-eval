# EVALUATION STUDY - SCOPE OUT PROJECT
- Doc containing a prelimiary study of where to go from the observability submission from Ben and Simon to a complete eval system that can be implemented into Twiga.

## BASE OBSERVABILITY PROJECT
- What does it consist of and which parts are most useful to us going forward?

### Consensus from meeting with Alvaro
- Work iteratively based on the observability project.
- Consider which step pertains more to which metric (Correctness -> query/semantic enhancement & Faithfullness -> System Prompt)
- Maybe worth generating a ton of different system prompts and iterating thru to see which is most corret/faithfull
- Correctness probably can't be tested better than with a quiz-style thing that already is implemented. 
- Structured cross-similarity is interesting: Looking at semantic similarity (cosine) between query, enriched query, retrieved content/data and output. I think this part is very interesting because it gives us a clear metric. Query enriching is also important here as it can introduce bias and halucinations but often still results in a better output. 

## ATTACK PLAN
- What needs to be added/implemented/built specifically to have more robust evaluation and observability?

0. Giga test-dataset
- Maybe let's test this thing crazy rigurously on tons of examples - see how it performs and get some larger data.
- Let's maybe build out the create_dataset.py script to have:
    1. Query templates (lesson plans, summaries, exam questions, comparison, key terms, etc).
    2. Generation of larger dataset from these templates (randomize which query template to use when with a good distribution)
    (This is kind of funny tho using query templates to generate a dataset with an LLM to evaluate an LLM with an LLM as a judge)

1. System Prompt Evaluation
https://mirascope.com/blog/langsmith-prompt-management
- Langsmith has a system for prompt managment and evaluation.
- Maybe find iteratively which system prompts perform best in the different metrics.
- This could extend to Tool Descriptions as well.

- After testing out the eval system a bit I think we definetly need to focus on system prompt eval particularly.
- The twiga mock-backend didn't perform very well in the eval, at least in my tests - maybe I configed something wrong. 
- Poor conciseness and could have better Faithfullness scores. 

2. Reflect/Research on Faithfullness vs Hallucination
- Langsmith evaluates Faithfullness with the "Hallucination" metric.
- After digging a bit deeper into Langsmith turns out that Hallucination is treated the same way as we define "Faithfullness"
- i.e. how true is the output to the source material. 

3. Visualize and compare
- Dig into the dataviz libraries and stuff?