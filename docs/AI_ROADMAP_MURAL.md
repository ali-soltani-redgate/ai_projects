# AI Engineer Roadmap — Mural Build Guide

Paste-ready content for building a **phase-based swimlane** mural from
[AI_ENGINEER_ROADMAP.md](AI_ENGINEER_ROADMAP.md).

Board: https://app.mural.co/t/sqlclone3118/home

---

## How to build it (5 minutes)

1. Open a blank Mural. Drop **5 columns** left→right, one per phase (titles + colors below).
2. For each fenced block below, **select the lines → copy → paste onto the canvas**.
   When Mural detects multiple lines it asks *"Create multiple sticky notes?"* → **Yes**.
   Each line becomes one sticky; the block lands as a tidy cluster.
3. Drag each cluster into its phase column, under its sub-area label.
4. Tip: set the sticky color **before** pasting so the whole cluster inherits it.

**Layout sketch**

```
PHASE 0          PHASE 1          PHASE 2          PHASE 3          PHASE 4
Foundations &    LLM APIs +       Agents,          LLMOps &         Fine-Tuning &
Assessment       Prompting + RAG  Orchestration    Production       Advanced
(1–2 weeks)      (1–2 months)     + HITL (1–2 mo)  (1–2 months)     (ongoing)
gray/blue        green            yellow           orange           purple
```

> Suggested sticky colors per phase — purely to make swimlanes pop:
> Phase 0 = gray, Phase 1 = green, Phase 2 = yellow, Phase 3 = orange, Phase 4 = purple.

---

## PHASE 0 — Foundations & Assessment  ·  1–2 weeks  ·  gray

### Math & Statistics
```
Linear algebra — vectors, matrices, embeddings
Probability & statistics — Bayes, distributions, sampling
Calculus basics — gradients, backprop intuition
```

### Python for AI
```
NumPy & Pandas fluency
Jupyter / notebook workflows
Async Python — serving & agents
```

### ML Core (assess gaps, fill as needed)
```
Supervised learning — regression, classification, trees, ensembles
Unsupervised learning — clustering, dimensionality reduction
Model evaluation — cross-validation, metrics, bias-variance
Feature engineering
Neural net fundamentals — activations, loss, optimizers
CNNs — image tasks
RNNs / LSTMs — sequence (historical context)
Transformers — attention, positional encoding
PyTorch or TensorFlow — one fluently
```

---

## PHASE 1 — LLM APIs + Prompting + RAG  ·  1–2 months  ·  green

### Using LLMs
```
Prompt engineering — zero/few-shot, chain-of-thought, system prompts
OpenAI / Azure OpenAI API
Anthropic, Gemini, open-source (Llama, Mistral, Qwen)
Token economics — context windows, pricing, rate limits
Context length management — map-reduce, sliding window, summarization
Structured output — JSON mode, function calling, tool use
```

### Retrieval-Augmented Generation (RAG)
```
Embedding models — ada, open-source alternatives
Vector databases — Pinecone, Weaviate, Qdrant, pgvector, Chroma
Chunking strategies — size, overlap, semantic
Hybrid search — vector + keyword/BM25
Reranking — Cohere, cross-encoders
RAG evaluation — faithfulness, relevance, recall
GraphRAG — knowledge-graph retrieval
Agentic RAG — dynamic retrieval decisions
```

---

## PHASE 2 — Agents, Orchestration & HITL  ·  1–2 months  ·  yellow

### Agent Frameworks
```
LangChain / LangGraph
PydanticAI — type-safe, Pydantic-native
Semantic Kernel
CrewAI / AutoGen / Agency Swarm
Custom agent loops — ReAct, tool-calling
```

### Tool Use & Function Calling
```
Designing tool schemas
Multi-step tool orchestration
Error handling & retry strategies
Sandboxing & security for code execution
```

### Memory & State
```
Short-term — conversation context
Long-term — vector stores, knowledge graphs
Session management patterns
```

### Multi-Agent Systems
```
Agent-to-agent communication
Supervisor / worker patterns
Parallel vs. sequential execution
```

### Human-in-the-Loop
```
Approval gates & escalation logic
Pause-and-ask vs. autonomous
Feedback & correction loops
Audit trails for agent decisions
```

---

## PHASE 3 — LLMOps & Production  ·  1–2 months  ·  orange

### Serving & Deployment
```
Model serving — vLLM, TGI, Triton, Ollama
API gateway patterns for LLMs
Streaming responses — SSE, WebSockets
Containerization — Docker for ML workloads
GPU infrastructure — A100, H100, cloud GPU
Quantization — GPTQ, AWQ, GGUF
Batch APIs — OpenAI / Anthropic Batch
LLM routing — LiteLLM, cost/complexity routing
```

### Monitoring & Observability
```
LLM observability — LangSmith, Langfuse, Logfire, Phoenix, W&B
Tracing agent execution
Cost tracking & optimization
Semantic & prompt caching — Redis, GPTCache, native
Latency profiling
```

### Evaluation & Testing
```
Eval frameworks — RAGAS, DeepEval, custom
Benchmark design — golden datasets
A/B testing for prompts
Regression testing for AI features
Red-teaming & safety testing
```

### CI/CD for AI
```
Prompt versioning
Model registry — MLflow, Hugging Face Hub
Automated eval in pipelines
Guardrails — content filtering, PII, hallucination checks
```

### Data Engineering for AI
```
Data pipelines — ETL, preprocessing
Document parsing — unstructured.io, docling
Synthetic data generation
Data labeling workflows
Data governance & licensing awareness
```

### AI Product & System Design
```
Designing AI-first features — when to use AI, when not
Latency vs. quality tradeoffs
Fallback strategies — graceful degradation
User feedback loops — thumbs up/down → improvement
Cost modeling for AI features
Responsible AI — bias, fairness, transparency
Security — prompt injection, data leakage, jailbreaks
```

---

## PHASE 4 — Fine-Tuning & Advanced  ·  ongoing  ·  purple

### Fine-Tuning & Customization
```
When to fine-tune vs. prompt vs. RAG
LoRA / QLoRA — parameter-efficient fine-tuning
Dataset preparation & curation
RLHF / DPO — alignment concepts
Running fine-tunes — OpenAI, Hugging Face, Axolotl
Distillation — smaller models mimic larger
```

### Multimodal AI
```
Vision-language models — GPT-4o, Gemini, LLaVA
Image generation — DALL-E, Stable Diffusion, Flux
Speech-to-text / text-to-speech — Whisper, ElevenLabs
Video understanding (emerging)
```

### Emerging & Advanced Topics
```
Model Context Protocol (MCP)
AI coding assistants — building & extending
Knowledge graphs + LLMs
Small language models — edge / on-device
Mixture of Experts (MoE)
Reasoning models — o1, o3, DeepSeek-R1
AI code-gen systems — Copilot, Cursor, Devin-style
Computer use & browser agents
Agentic coding workflows — multi-file edits, test gen
```

---

## Optional flourishes for the mural

- **Daily Habit card** (corner sticky): Concept 30m · Code 30m · Note 5m → *"Consistency beats intensity."*
- **Progress legend**: a checkmark/colored dot you place on each sticky once confident — mirrors the doc's checkboxes.
- **Gap-spotting**: at review time, clusters of un-dotted stickies = your focus areas.

---

*Source: AI_ENGINEER_ROADMAP.md · phase mapping per the Suggested Learning Path.*
