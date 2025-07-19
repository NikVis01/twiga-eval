# EVALUATION STUDY - SCOPE OUT PROJECT
- Doc containing a prelimiary study of where to go from the observability submission from Ben and Simon to a complete eval system that can be implemented into Twiga.

## BASE OBSERVABILITY PROJECT
- What does it consist of and which parts are most useful to us going forward?

### Consensus from meeting with Alvaro
- Work iteratively based on the observability project.
- Consider which step pertains more to which metric (Correctness -> query/semantic enhancement & Faithfullness -> System Prompt)
- Maybe worth generating a ton of different system prompts and iterating thru to see which is most corret/faithfull
- Correctness probably can't be tested better than with a quiz.
- Structured cross-similarity is interesting: Looking at semantic similarity (cosine) between query, enriched query, retrieved content/data and output. I think this part is very interesting because it gives us a clear metric. Query enriching is also important here as it can introduce bias and halucinations but often still results in a better output. 

## EVALUATION METRICS
- Which metrics are we looking for and what are our primary concerns in evaluating Twiga.

### Correctness

### Faithfullness


## INDUSTRY STANDARDS
- This has been done before; what methods are used and how is Twiga different? What are we concerned with that is different than the primary model providers and tools using LLMs out there that are conducting extensive LLM evaluation?

### Frameworks
1. Langsmith
- Standard, more for observability but also eval

2. RAGAS
https://docs.ragas.io/en/stable/
- Apparently great for Faithfullness and correctness if u have a test dataset available

3. Custom
- Tons of custom suites used.

### Best Practices
Source: https://qdrant.tech/blog/rag-evaluation-guide/?utm_source=chatgpt.com

- Separate retriever and generator tests
- Analyze context recall/precision for IR stage
- Examine faithfulness and relevance for generation stage
- Tie everything together in CI/CD pipelines


## NEXT STEPS
- What needs to be added/implemented/built specifically to have more robust evaluation and observability?