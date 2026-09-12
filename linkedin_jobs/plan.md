# Plan to learn Agentic systems in pratice
We want to create an agentic systems to search suitable jobs and matches with input CV. We are going to build this agent step by step and take baby steps. The end goal is build a secure system on AWS

## Phase 1 - Create a simple app to call claude models

- [x] Create a simple app to call claude models
  - [x] Init a project with uv
  - [x] Add packages needed for the agent and LLMs
    - [x] Add langchain
    - [x] Add langchain-anthropic to connect to Anthropic models
  - [x] Create env file for the Anthropic API key
  - [x] Add python-dotenv package to load the API key
  - [x] Connect to claude haiku model and test it with simple prompt
  - [x] Refactor agent to use the model with ChatAnthropic

## Phase 2 - Create a simple agent with LangChain to call a simple tool

- [x] Create an agent with LangChain without tool
- [x] Invoke the agent with a simple user prompt
- [x] Refactor the code so we can pass `HumanMessage` rather than pass a raw message
- [x] Print the agent's response
  - [x] As LangChain returns response as the agent state, we need to print last message, which is AIMessage

## Phase 3 - Add an observability tool

- [x] Host it locally
  - [x] Clone the repo
  - [x] Run it on Docker
  - [x] Check the [host](http://localhost:3000)
- [x] Add langfuse package
- [ ] Integrate the agent with langfuse
- [ ] Create a simple agent with LangChain to call a simple tool
  
- [ ] Create a simple agent with LangChain to get the user location, job name and type of job and return list of jobs

## Tips

### Interperter in VS code

- If the interperter complains about the packages, you need to do this:
  - Check the active virtual env and activate it if needed
  - Set the right path for the interpreter
  - Run uv syn

## Comparision

### LangChain

- We should pass the user prompt with messages format
  - PydanthicAI would be cleaner
    - Ex: result = agent.run_sync("What is the capital of France?")

- We should get the agent's response with `content = result["messages"][-1].content`
  - PydanthicAI would be cleaner
    - Ex: `print(result.output)`
