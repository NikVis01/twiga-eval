# System prompts for evaluation and templates for automatic generation

## DIRS:
### tool_usage
- Contains tool-calling specific system prompts. I noticed that the model sometimes doesn't call the tool and has an option to not do it. 
- I think it generally should try to do this if the query is related to the book's content, which it generally is. We should however potentially allow non-tool called responses as a user might ask something general about pedagogy that the book doesn't specifically cover. 
- I've fleshed out the tool descriptions primarily regarding when they should be used and pushing on the fact that search_knowledge should be a high priority tool.
- Even though we could be doing better tool descriptions in the tool definition I also think it probably doesn't hurt to do so in the system prompt and focusing on WHEN they should be used.
- This is now included in the others as well but it was a good first step and can be used if you want to avoid verbosity.

### ux_educational
- First step towards a more rounded educational chatbot, focusing on approach, education methods, question/response situations as well as how to treat the user. Using a bit of theory regarding pedagogy as well to help the teachers teach effectively.

### short
- Least verbose version of the sys prompt still retaining XML-wrapper structure to help LLM not mix up the different sections of the prompt 

### verbose
- A very verbose set of prompts that feed in a lot of context about the user's background, how they should be treated as well as formatting with even more XML wrappers for clarity. 
