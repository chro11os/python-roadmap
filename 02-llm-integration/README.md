# Phase 2 — LLM Integration
**Time:** 8–12 weeks · **Goal:** get reliable, structured results from LLM APIs and ship a simple AI app.

## 1. Prompt engineering (for consistency, not vibes)
- [ ] System prompts vs. user messages; roles
- [ ] Few-shot examples
- [ ] Step-by-step reasoning / extended thinking
- [ ] Output formatting: JSON, XML tags, schemas
- [ ] Prompt templates & variables
- [ ] Failure modes: hallucination, prompt injection, refusals — and mitigations

## 2. Model APIs
- [ ] Anthropic API (Claude) — Messages API, SDK
- [ ] OpenAI API
- [ ] Hugging Face / open-weight models; running one locally (e.g. Ollama)
- [ ] Request/response anatomy, stop reasons, errors, rate limits
- [ ] Streaming responses
- [ ] Structured output & tool/function calling
- [ ] Vision / multimodal inputs (images, PDFs)

## 3. Tokens & cost control
- [ ] Counting tokens; context window limits
- [ ] Pricing per input/output token; picking the right model size
- [ ] Prompt caching, batching, `max_tokens`
- [ ] Retries, timeouts, fallbacks between models

## 4. Evaluating outputs
- [ ] Build a small test set of inputs + expected outputs
- [ ] Automated checks (schema valid? contains X?)
- [ ] LLM-as-judge basics
- [ ] Compare prompts/models side by side

## 5. Shipping a UI
- [ ] Simple frontend (Streamlit, Gradio, or a small React/Next page)
- [ ] Backend holds the API key, never the browser

## ✅ Milestone project
An app that takes user input, calls an LLM, returns **validated structured output** (e.g. "paste a job post → get skills, seniority, salary range as JSON"), streams the response, and logs token cost per request.

## Done when…
- Same input gives you the same *shape* of output every time
- You know what each request costs
