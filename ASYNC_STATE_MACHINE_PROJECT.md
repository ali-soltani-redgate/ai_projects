# Async State Machine Model for Agent Execution

## Project Overview

This project teaches the **async state machine model** for building reliable agent systems. Instead of agents executing in a linear flow, they progress through well-defined states with explicit transitions, making the execution model predictable and resilient.

**Learning Goal**: Build a task execution agent that manages multiple states (idle, processing, waiting, completed, failed) and transitions between them asynchronously.

---

## Why Async State Machines for Agents?

1. **Predictability**: Each state has defined entry/exit behavior
2. **Resilience**: You can pause, resume, and recover from failures
3. **Observability**: Each transition is explicit and traceable
4. **Composability**: States can be reused across different agents
5. **Testability**: Each state transition can be tested independently

---

## Core Concepts

### State Machine Components

```
┌─────────────────────────────────────────┐
│  IDLE                                   │
│  - Waiting for input                    │
│  - Entry: Reset timers                  │
│  - Exit: Validate input                 │
└────────────┬────────────────────────────┘
             │ receiveTask()
             ▼
┌─────────────────────────────────────────┐
│  PROCESSING                             │
│  - Executing the task                   │
│  - Entry: Initialize execution          │
│  - Timeout: 30s                         │
└────────────┬────────────────────────────┘
             │ complete() or timeout()
             ▼
┌─────────────────────────────────────────┐
│  COMPLETED / FAILED                     │
│  - Task done or error occurred          │
│  - Entry: Cleanup resources             │
│  - Exit: Return to IDLE                 │
└─────────────────────────────────────────┘
```

### Key Properties

- **Current State**: Tracks where the agent is in its lifecycle
- **Context**: Data carried through the state machine (task details, results)
- **Transitions**: Functions that move between states
- **Side Effects**: Actions triggered on entry/exit of states
- **Guards**: Conditions that prevent invalid transitions

---

## Project Architecture

### Phase 1: Basic State Machine (Days 1-2)

Build a minimal state machine with:
- ✓ Enum-based states
- ✓ Context object for data flow
- ✓ Type-safe transitions
- ✓ Entry/exit handlers

**File**: `src/StateMachine.ts`

```typescript
type State = 'idle' | 'processing' | 'completed' | 'failed';

interface Context {
  taskId: string;
  input: unknown;
  result?: unknown;
  error?: Error;
}

type Handler = (ctx: Context) => Promise<void>;

interface StateConfig {
  entry?: Handler;
  exit?: Handler;
}
```

### Phase 2: Agent Executor (Days 2-3)

Build the agent that uses the state machine:
- ✓ Task queue management
- ✓ Async task execution
- ✓ Timeout handling
- ✓ Error recovery

**File**: `src/TaskAgent.ts`

```typescript
class TaskAgent {
  private state: State = 'idle';
  private context: Context;
  private stateConfig: Map<State, StateConfig>;

  async receiveTask(task: Task): Promise<void> {
    // Transition: idle -> processing
    await this.transitionTo('processing', { taskId: task.id, input: task.input });
  }

  async execute(): Promise<void> {
    // Runs the task based on current state
  }

  private async transitionTo(newState: State, context: Context): Promise<void> {
    // Exit current state
    // Enter new state
    // Update state
  }
}
```

### Phase 3: Observability (Days 3-4)

Add instrumentation:
- ✓ State transition logging
- ✓ Metrics (time in state, transition count)
- ✓ Event emitter for state changes
- ✓ Trace integration (Langfuse/OpenTelemetry)

### Phase 4: Resilience (Days 4-5)

Add robustness:
- ✓ Persistence (save state to disk/DB)
- ✓ Recovery (resume from last known state)
- ✓ Retry logic with exponential backoff
- ✓ Deadlock detection

---

## Implementation Roadmap

### Week 1: Core Implementation

```
Day 1: State Machine Scaffold
  → Create State enum
  → Define Context interface
  → Implement basic transition logic
  → Write unit tests for state transitions

Day 2: Agent Integration
  → Build TaskAgent class
  → Implement task processing loop
  → Add timeout handling
  → Test with sample tasks

Day 3: Entry/Exit Handlers
  → Add state lifecycle hooks
  → Implement resource cleanup
  → Add logging/debugging
  → Create integration tests

Day 4: Error Handling
  → Add error states
  → Implement retry logic
  → Add validation guards
  → Test failure scenarios

Day 5: Polish & Docs
  → Add comprehensive logging
  → Document state machine flow
  → Create examples
  → Performance profiling
```

### Week 2: Advanced Features (Optional)

- **Nested States**: Composite states for complex workflows
- **Parallel Processing**: Multiple concurrent state machines
- **Event Sourcing**: Replay state transitions from logs
- **Visualization**: Generate state machine diagrams

---

## Testing Strategy

### Unit Tests (Per State)

```typescript
describe('IDLE state', () => {
  it('should transition to PROCESSING on receiveTask', async () => {
    const agent = new TaskAgent();
    const task = { id: '1', input: 'test' };
    
    await agent.receiveTask(task);
    
    expect(agent.getState()).toBe('processing');
  });

  it('should call entry handler on transition', async () => {
    const entrySpy = jest.fn();
    const agent = new TaskAgent();
    agent.setStateHandler('processing', { entry: entrySpy });
    
    await agent.receiveTask(task);
    
    expect(entrySpy).toHaveBeenCalled();
  });
});
```

### Integration Tests (Full Flow)

```typescript
describe('Full task execution flow', () => {
  it('should complete a task successfully', async () => {
    const agent = new TaskAgent();
    
    await agent.receiveTask(task1);
    const result1 = await agent.execute();
    
    expect(agent.getState()).toBe('completed');
    expect(result1).toBeDefined();
    
    // Should auto-return to idle
    await waitFor(() => expect(agent.getState()).toBe('idle'));
  });

  it('should handle timeout and transition to failed', async () => {
    const agent = new TaskAgent({ timeout: 100 });
    const slowTask = { id: '1', input: async () => new Promise(r => {}) };
    
    await agent.receiveTask(slowTask);
    await agent.execute();
    await wait(150);
    
    expect(agent.getState()).toBe('failed');
  });
});
```

---

## Key Learning Outcomes

By completing this project, you'll understand:

1. **State Machine Design**: When to use states vs conditionals
2. **Async Patterns**: Handling concurrent operations reliably
3. **Error Recovery**: Building resilient systems
4. **Observability**: Instrumenting state transitions
5. **Testing State Machines**: Verifying all paths

---

## Resources & References

- **Pattern**: State machine pattern in concurrent systems
- **Related**: Actor model, workflow engines, saga pattern
- **Tools**: You can later integrate with Temporal, Airflow, or similar
- **Langfuse Integration**: Add observability to agent state transitions

---

## Success Criteria

✓ Agent correctly transitions through all states  
✓ No invalid transitions possible (type-safe)  
✓ Timeout handling works reliably  
✓ Error states are recoverable  
✓ All tests pass  
✓ Code is readable and well-documented  

---

## Extension Ideas

Once the core is solid, consider:

- **Multi-agent coordination**: State machines communicating with each other
- **Hierarchical states**: States containing sub-state-machines
- **Time-based transitions**: States that auto-transition after duration
- **External event handling**: States responding to external triggers
- **Checkpointing**: Save/restore full state for long-running agents

