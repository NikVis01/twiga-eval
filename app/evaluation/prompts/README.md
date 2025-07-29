# System prompts for evaluation and templates for automatic generation

## DIRS:
### tool_usage
- Contains tool-calling specific system prompts. I noticed that the model sometimes doesn't call the tool and has an option to not do it. 
- I think it generally should try to do this if the query is related to the book's content, which it generally is. We should however potentially allow non-tool called responses as a user might ask something general about pedagogy that the book doesn't specifically cover. 
- I've fleshed out the tool descriptions primarily regarding when they should be used and pushing on the fact that search_knowledge should be a high priority tool.
- This is now included in the others as well but it was a good first step and can be used if you want to avoid verbosity.

UPDATE:
- This prompt has since been rewritten to have the tool selection guidenlines wrapper to optimize for tool calling in the ai.py file. I noticed we call the LLM twice; once for tools and once for final response but we could have 2 different prompts for this that focus on these respectively, but instead I'm baking them into one by working more on tool calling logic to avoid context loss and identity crisis between these two calls.
- We can still refractor the tool usage by working on registry.py to have better descriptions. 

### ux_educational
- First step towards a more rounded educational chatbot, focusing on approach, education methods, question/response situations as well as how to treat the user. Using a bit of theory regarding pedagogy as well to help the teachers teach effectively.

### short
- Least verbose version of the sys prompt still retaining XML-wrapper structure to help LLM not mix up the different sections of the prompt 

### verbose
- A very verbose set of prompts that feed in a lot of context about the user's background, how they should be treated as well as formatting with even more XML wrappers for clarity. 
