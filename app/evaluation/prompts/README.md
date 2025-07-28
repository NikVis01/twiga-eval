# System prompts for evaluation and templates for automatic generation

## DIRS:
### tool_calling
- Contains tool-calling specific system prompts. I noticed that the model sometimes doesn't call the tool and has an option to not do it. 
- I think it generally should try to do this if the query is related to the book's content, which it generally is. We should however potentially allow non-tool called responses as a user might ask something general about pedagogy that the book doesn't specifically cover. 
- I've fleshed out the tool descriptions primarily regarding when they should be used and pushing on the fact that search_knowledge should be a high priority tool.
- Even though we could be doing better tool descriptions in the tool definition I also think it probably doesn't hurt to do so in the system prompt and focusing on WHEN they should be used.

### templates
- For future use in generating these system prompts using an LLM.

## Versions

### V1 / baseline.txt
- Just the baseline that was I think Victor added.

### V2
- I wasn't happy with how we describe and manage the tool-calling logic. Maybe there's some better ways to do this through langchain. Will talk to Alvaro about it, maybe it doesn't need to be part of the sys prompt.
- Wanted to include examples and nuance to use-cases of the tools as well as format as more effective XML.
