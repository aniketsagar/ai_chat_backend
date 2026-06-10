10/6/2026

- Changes to cache structure.
- Currently the cache holds
  {
  data : "str",
  conversation_id:""
  }

- we add timestamp and status to it

{
data:"",
timestamp:"",
response_status:"",
conversation_id:""
}

response_status: Started/InProgress/Completed/Failed/Incomplete
timestamp: timestamp for every event we store, so this feild will be overwritten quite frequently.

data: string data, accumalated chunks
conversation_id: string

1. OpenAI provider, needs to send the response_status based on the event that it sees.
2. Provider Service forwards the same structure to conversation service.
3. Conversation service parses the structure and callse caching service to store the data,
4. Caching service stores the data in the above format.
