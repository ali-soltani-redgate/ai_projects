# LLM-Based Agent Project

## Problem: Build a Conversational Research Agent with State Machine

Create an agent that answers questions by managing explicit state transitions:

### State Flow
```
┌──────┐
│ IDLE │  Waiting for user input
└───┬──┘
    │ receive_message()
    ▼
┌─────────┐
│ THINKING│  Calling LLM to decide: answer or use tool
└───┬──┬──┘
    │  │
    │  └─────────────────────┐
    │ (needs tool)           │ (direct answer)
    ▼                        │
┌───────────────┐            │
│ TOOL_EXECUTING│ Execute selected tool async
└───┬───────────┘            │
    │ tool result            │
    ▼                        │
┌──────────────┐             │
│ RESPONDING   │◄────────────┘
└───┬──────────┘ Generate final response
    │ response sent
    ▼
  IDLE
```

### Input
```python
message: str  # User question or statement
```

### Process
1. **IDLE** → receive message → **THINKING**
2. **THINKING** → call LLM (needs tool?) → **TOOL_EXECUTING** or **RESPONDING**
3. **TOOL_EXECUTING** → run tool async → **RESPONDING** 
4. **RESPONDING** → format answer → **IDLE**

### Output
```python
response: str  # Agent's answer
used_tools: list[str]  # Which tools were called
execution_time: float
```

### Example
```
User: "What's the capital of France and how many people live there?"

Agent:
  1. Calls LLM → decides needs search
  2. Searches "capital of France population"
  3. Gets result: "Paris, ~2.1M"
  4. Calls LLM with search result
  5. Returns: "The capital of France is Paris with approximately 2.1 million people."
```

### Tools Available
- `search(query: str) -> str` - simulate web search
- `read_file(path: str) -> str` - read local file
- `calculate(expr: str) -> float` - evaluate math

### Constraints
- Keep conversation history (last 10 messages)
- Support multi-turn conversations
- Handle tool errors gracefully
- Type hints throughout

---

## Implementation Steps

**Phase 1: State Machine Foundation**
- Define states: idle, thinking, tool_executing, responding
- Implement state transitions with guards
- Add entry/exit handlers per state

**Phase 2: LLM Integration**
- Implement THINKING state (call Claude API)
- Parse LLM response for tool decisions
- Conversation history management

**Phase 3: Tool Execution**
- Implement search, read_file, calculate tools
- TOOL_EXECUTING state runs tools asynchronously
- Error handling per tool

**Phase 4: Integration & Testing**
- Wire states together into agent
- Unit tests per state
- Multi-turn conversation tests

---

## File Structure
```
src/
  ├── state_machine.py      # State, StateConfig, StateContext
  ├── tools.py              # search(), read_file(), calculate()
  ├── research_agent.py     # ResearchAgent with states
  └── messages.py           # Message types

tests/
  ├── test_state_machine.py
  ├── test_tools.py
  └── test_agent.py
```

---

## Success Criteria
✓ All state transitions are type-safe  
✓ Agent correctly routes through states  
✓ Tools execute asynchronously  
✓ Conversation history persists  
✓ Tool errors handled gracefully  
✓ Multi-turn conversations work  
✓ All tests pass  
