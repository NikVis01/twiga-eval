# Twiga Evaluation
- Start of the eval project
- This .md is for quick intro about the project, in this dir there will be a list of all resources associated to LLM and RAG eval
- Links, thoughts, frameworks and evaluation metrics to implement in depth.

### Contact people
Niklavs, Ben, Hampus

### Linear link
https://linear.app/twiga-team/project/llm-evaluation-c16be4b2451d/overview 

### Introduction
The evaluation of an LLM (and query output) is key for knowing which LLM performs best in Twiga and how we should organise the information in the Database. 

This task is supposed to use the framework that Ben and Simon used for the Hackathon, but for making that framework work we need to:
Do a bit of research on which ways we should evaluate the LLMs: correctness, extension, precision, doubts of the LLM…

Create a test environment where we have stored the expected response for a given prompt. This test environment should be big enough to be representative of all possible Twiga calls and should also be updated with any feature that is added to the system.

### System
In short, we need something similar to what Ben and Simon did in their Hackathon project. We need a system that:

Is able to catch every single LLM call and logs/stores it → Connectors

Ability to retrieve past calls.

Scalability of that logging system → Álvaro Mazcuñán Herreros can help here a lot!

Create a mini benchmarking system where we can test different LLMs in different tasks.

Investigating which tasks are more important for the initial test (1 or 2, we are not experts yet).

Test scalability?
