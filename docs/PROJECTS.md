# AI Engineer Practice Projects

> End-to-end projects designed to run locally.  
> Each project builds on skills from the [AI Engineer Roadmap](AI_ENGINEER_ROADMAP.md).

---

## Project 1 — "Ask My Docs" (RAG Chatbot)

Build a RAG chatbot over a local collection of your own documents (PDFs, markdown, code).

**What you'll learn:**
- Document parsing & chunking strategies
- Embedding models & vector databases
- Retrieval pipeline design (similarity search, hybrid search)
- Prompt engineering with retrieved context
- Evaluation of RAG quality (faithfulness, relevance, recall)
- Streaming responses to the user

---

## Project 2 — "SQL Agent"

Build an agent that takes a natural language question, generates SQL, executes it against a local database, and returns a human-readable answer.

**What you'll learn:**
- Agent loop design (ReAct / tool-calling pattern)
- Function calling & tool schemas
- Structured output from LLMs
- Error handling & self-correction (invalid SQL → retry)
- Database interaction as a tool
- Prompt engineering for code generation

---

## Project 3 — "Code Review Bot"

Build a tool that takes a git diff as input and produces a structured code review with actionable suggestions.

**What you'll learn:**
- Working with structured/long inputs (diffs)
- Prompt engineering for analysis tasks
- Structured output (JSON with categories, severity, suggestions)
- Token management (large diffs vs. context windows)
- Integrating with developer tooling (git, CLI)
- Quality evaluation of generated reviews

---

## Project 4 — "Multi-Agent Research Assistant"

Build a system where multiple agents collaborate: one searches the web, one summarizes, one fact-checks, and a supervisor orchestrates the flow.

**What you'll learn:**
- Multi-agent architecture patterns (supervisor/worker)
- Agent-to-agent communication & state passing
- Parallel vs. sequential execution decisions
- Tool use across agents (web search, file I/O)
- Orchestration frameworks (LangGraph, CrewAI, or custom)
- Observability & tracing multi-step agent flows

---

## Project 5 — "Custom Fine-Tuned Classifier"

Take a real dataset (support tickets, emails, or bug reports), fine-tune a small model to classify them, deploy it locally, and build an eval pipeline around it.

**What you'll learn:**
- Dataset preparation & curation
- Fine-tuning (LoRA/QLoRA or API-based)
- Model evaluation (precision, recall, confusion matrix)
- Comparison: fine-tuned model vs. prompted LLM
- Local model serving (Ollama or vLLM)
- Building automated eval pipelines

---

## Project 6 — "Voice-Powered Task Manager"

Build an end-to-end app: speech-to-text → LLM intent parsing → tool execution (create/update/list tasks in a local DB) → text-to-speech response.

**What you'll learn:**
- Multimodal AI (speech-to-text, text-to-speech)
- Intent extraction & entity recognition with LLMs
- Tool orchestration (CRUD operations as tools)
- End-to-end system design (audio → understanding → action → audio)
- Local database integration
- Latency optimization across the full pipeline

---

## Suggested Order

| # | Project | Primary Roadmap Sections |
|---|---------|--------------------------|
| 1 | Ask My Docs | 3.2 RAG, 5.3 Evaluation |
| 2 | SQL Agent | 4.1–4.2 Agents & Tools |
| 3 | Code Review Bot | 3.1 Using LLMs, 8 Product Design |
| 4 | Multi-Agent Research | 4.4 Multi-Agent, 5.2 Observability |
| 5 | Fine-Tuned Classifier | 3.3 Fine-Tuning, 5.1 Serving |
| 6 | Voice Task Manager | 7 Multimodal, 4.2 Tool Use |

---

Pick one and ask me to get started. I'll give you just enough guidance to build it yourself.
