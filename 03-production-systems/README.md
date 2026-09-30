# Phase 3 — Production Systems
**Time:** 8–12 weeks · **Goal:** build RAG pipelines and agents that act, and run them reliably.

## 1. Orchestration frameworks
- [ ] LangChain / LangGraph: chains, tools, memory, multi-step flows
- [ ] Know when to skip the framework and just write plain code
- [ ] Alternatives worth a look: LlamaIndex, Claude Agent SDK

## 2. RAG (Retrieval-Augmented Generation)
- [ ] Document loading (PDF, HTML, Markdown)
- [ ] Chunking strategies & chunk size tradeoffs
- [ ] Embedding models
- [ ] Vector DBs: pgvector, Chroma, Qdrant, Pinecone
- [ ] Semantic vs. keyword (BM25) vs. hybrid search
- [ ] Reranking
- [ ] Citing sources in answers
- [ ] Evaluating retrieval: did it fetch the right chunks?

## 3. Agents
- [ ] Tool use loop: model → tool call → result → model
- [ ] Designing good tools (clear names, schemas, error messages)
- [ ] Actions: call APIs, update records, trigger workflows
- [ ] Planning, multi-step tasks, stopping conditions
- [ ] Human-in-the-loop approval for risky actions
- [ ] Multi-agent patterns (and why to avoid them until needed)

## 4. MCP (Model Context Protocol)
- [ ] What MCP is: a standard way to plug tools/data into models
- [ ] Use existing MCP servers (GitHub, Google Drive, etc.)
- [ ] Build your own MCP server
- [ ] Permissions & safety boundaries

## 5. LLMOps
- [ ] Prompt versioning (prompts live in git)
- [ ] Tracing & monitoring (Langfuse, LangSmith, or plain logs)
- [ ] Eval suites run in CI
- [ ] Cost dashboards & budgets
- [ ] Handling model upgrades/deprecations
- [ ] Caching, queues, rate limiting
- [ ] Security: prompt injection, data leakage, PII
- [ ] Deploy: Docker + a cloud host

## ✅ Milestone project
A deployed RAG chatbot over your own docs with citations, plus one agent tool (e.g. "create a GitHub issue"), with tracing and an eval set in CI.

## Done when…
- You can explain why an answer was wrong (bad retrieval vs. bad generation)
- Your system survives an API outage without crashing
