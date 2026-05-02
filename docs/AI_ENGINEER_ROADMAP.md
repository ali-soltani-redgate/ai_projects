# AI Engineer Roadmap

> For senior software engineers transitioning into AI engineering.  
> Use the checkboxes to track where you are.

---

## 1. Foundations

### 1.1 Math & Statistics (as needed)
- [ ] Linear algebra (vectors, matrices, dot products, embeddings geometry)
- [ ] Probability & statistics (Bayes, distributions, sampling)
- [ ] Calculus basics (gradients, backpropagation intuition)

### 1.2 Python for ML/AI
- [ ] NumPy, Pandas fluency
- [ ] Jupyter / notebook workflows
- [ ] Async Python (for serving & agents)

---

## 2. Machine Learning Core

### 2.1 Classical ML
- [ ] Supervised learning (regression, classification, trees, ensembles)
- [ ] Unsupervised learning (clustering, dimensionality reduction)
- [ ] Model evaluation (cross-validation, metrics, bias-variance)
- [ ] Feature engineering

### 2.2 Deep Learning
- [ ] Neural network fundamentals (activations, loss functions, optimizers)
- [ ] CNNs (image tasks)
- [ ] RNNs / LSTMs (sequence tasks — mostly historical context now)
- [ ] Transformers architecture (attention, positional encoding)
- [ ] PyTorch or TensorFlow (at least one fluently)

---

## 3. Large Language Models (LLMs)

### 3.1 Using LLMs
- [ ] Prompt engineering (zero-shot, few-shot, chain-of-thought, system prompts)
- [ ] OpenAI / Azure OpenAI API
- [ ] Anthropic, Google Gemini, open-source models (Llama, Mistral, Qwen)
- [ ] Token economics (context windows, pricing, rate limits)
- [ ] Structured output (JSON mode, function calling, tool use)

### 3.2 Retrieval-Augmented Generation (RAG)
- [ ] Embedding models (text-embedding-ada, open-source alternatives)
- [ ] Vector databases (Pinecone, Weaviate, Qdrant, pgvector, Chroma)
- [ ] Chunking strategies (size, overlap, semantic chunking)
- [ ] Hybrid search (vector + keyword/BM25)
- [ ] Reranking (Cohere, cross-encoders)
- [ ] Evaluation of RAG pipelines (faithfulness, relevance, recall)

### 3.3 Fine-Tuning & Customization
- [ ] When to fine-tune vs. prompt vs. RAG (decision framework)
- [ ] LoRA / QLoRA (parameter-efficient fine-tuning)
- [ ] Dataset preparation & curation
- [ ] RLHF / DPO (alignment concepts)
- [ ] Running fine-tunes (OpenAI, Hugging Face, Axolotl)

---

## 4. AI Agents & Orchestration

### 4.1 Agent Frameworks
- [ ] LangChain / LangGraph
- [ ] PydanticAI (type-safe, Pydantic-native agents)
- [ ] Semantic Kernel
- [ ] CrewAI / AutoGen / Agency Swarm
- [ ] Custom agent loops (ReAct pattern, tool-calling loops)

### 4.2 Tool Use & Function Calling
- [ ] Designing tool schemas
- [ ] Multi-step tool orchestration
- [ ] Error handling & retry strategies
- [ ] Sandboxing & security for code execution

### 4.3 Memory & State
- [ ] Short-term (conversation context)
- [ ] Long-term (vector stores, knowledge graphs)
- [ ] Session management patterns

### 4.4 Multi-Agent Systems
- [ ] Agent-to-agent communication
- [ ] Supervisor / worker patterns
- [ ] Parallel vs. sequential execution

---

## 5. MLOps & LLMOps

### 5.1 Serving & Deployment
- [ ] Model serving (vLLM, TGI, Triton, Ollama)
- [ ] API gateway patterns for LLMs
- [ ] Streaming responses (SSE, WebSockets)
- [ ] Containerization (Docker for ML workloads)
- [ ] GPU infrastructure basics (A100, H100, cloud GPU options)

### 5.2 Monitoring & Observability
- [ ] LLM observability (LangSmith, Langfuse, Logfire, Phoenix, Weights & Biases)
- [ ] Tracing agent execution
- [ ] Cost tracking & optimization
- [ ] Latency profiling

### 5.3 Evaluation & Testing
- [ ] LLM evaluation frameworks (RAGAS, DeepEval, custom evals)
- [ ] Benchmark design (golden datasets)
- [ ] A/B testing for prompts
- [ ] Regression testing for AI features
- [ ] Red-teaming & safety testing

### 5.4 CI/CD for AI
- [ ] Prompt versioning
- [ ] Model registry (MLflow, Hugging Face Hub)
- [ ] Automated eval in pipelines
- [ ] Guardrails (content filtering, PII detection, hallucination checks)

---

## 6. Data Engineering for AI

- [ ] Data pipelines for training/fine-tuning (ETL, preprocessing)
- [ ] Document parsing (PDFs, HTML, tables — unstructured.io, docling)
- [ ] Synthetic data generation
- [ ] Data labeling workflows
- [ ] Data governance & licensing awareness

---

## 7. Multimodal AI

- [ ] Vision-language models (GPT-4o, Gemini, LLaVA)
- [ ] Image generation (DALL-E, Stable Diffusion, Flux)
- [ ] Speech-to-text / text-to-speech (Whisper, ElevenLabs)
- [ ] Video understanding (emerging)

---

## 8. AI Product & System Design

- [ ] Designing AI-first features (when to use AI, when not to)
- [ ] Latency vs. quality tradeoffs
- [ ] Fallback strategies (graceful degradation)
- [ ] User feedback loops (thumbs up/down → improvement)
- [ ] Cost modeling for AI features
- [ ] Responsible AI (bias, fairness, transparency)
- [ ] Security (prompt injection, data leakage, jailbreaks)

---

## 9. Emerging & Advanced Topics

- [ ] Model Context Protocol (MCP)
- [ ] AI coding assistants (building & extending)
- [ ] Knowledge graphs + LLMs
- [ ] Small language models (SLMs) for edge/on-device
- [ ] Mixture of Experts (MoE) architectures
- [ ] Reasoning models (o1, o3, DeepSeek-R1)
- [ ] AI compiler & code generation systems
- [ ] Agentic coding (Copilot agent mode, Cursor, Devin-style)

---

## Suggested Learning Path (for someone 6 months in)

| Phase | Focus | Timeframe |
|-------|-------|-----------|
| **Now** | Assess gaps in sections 1–3 above | 1 week |
| **Phase 1** | RAG deep-dive + vector DBs + eval | 1–2 months |
| **Phase 2** | Agents & orchestration (section 4) | 1–2 months |
| **Phase 3** | LLMOps, monitoring, production patterns | 1–2 months |
| **Phase 4** | Fine-tuning + advanced topics | ongoing |

---

## How to Use This Roadmap

1. Go through each section and check items you're confident in
2. Identify clusters of unchecked items — those are your gaps
3. Prioritize based on what your current/target role demands
4. Build projects that combine multiple skills (e.g., a RAG agent with eval pipeline)

---

*Last updated: 2025-05-02*
