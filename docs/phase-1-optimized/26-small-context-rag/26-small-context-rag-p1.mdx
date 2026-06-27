# Hierarchical Summary RAG for Small Context Windows

**Source:** `26-small-context-rag.md` · **Phase 1** · Cleaned & annotated

## Overview

Hierarchical Summary RAG is a document search technique that uses summaries to find the right information, then switches to raw text to answer questions. Like a library card catalog: scan summary cards to locate the right book, then open the actual book to read the full answer. The core insight: summaries are great for finding stuff but terrible for answering from, because they compress away the exact details you need.

## Core Content

### 1. The Elevator Pitch

RAG on small-context models fails because retrieval finding the right chunk is not the same as the model seeing that chunk. The solution is a three-tier pipeline: document summaries → chunk summaries → raw chunks within a strict token budget. Summaries route the search, raw chunks provide the evidence, and a visible context budget prevents silent failures.

### 2. Why This Matters

- **Unfair advantage:** Build AI search that works on your laptop, not just on OpenAI's servers. Compete with a fraction of the compute.
- **Hidden leverage:** Summaries are indexed once and queried forever. Your search infrastructure compounds while competitors pay per-token for brute-force context stuffing.
- **"Aha!" moment:** Most RAG failures aren't retrieval failures -- they're context-budgeting failures disguised as retrieval failures.

### 3. Reality Check

- **Overrated when:** Using Claude 3.5 with 200K context or GPT-4 with 128K tokens -- naive RAG works fine for a while.
- **Opportunity cost:** Investing in indexing infrastructure instead of just throwing more context at the problem. For under 50 pages, this is over-engineering.
- **Not for:** People who hate debugging. The value is in traceability (seeing which summaries hit, which chunks got skipped). If you want a black box, pay for bigger context windows.

### 4. Core Concepts

| Concept | Analogy | Why Care |
|---------|---------|----------|
| **Summaries are maps, not territory** | GPS gets you to the neighborhood; street signs find the exact house | Use summaries for navigation, raw text for answers |
| **Context is a budget, not a bucket** | Packing a carry-on -- every "maybe" item pushes out a "definitely need" item | Token budget is a hard constraint: if it doesn't fit, it gets skipped |
| **Chunk boundaries are lies** | Cutting a movie into scenes doesn't make scene 4 make sense alone | Include neighbor chunks (previous/next) for coherence |
| **Recursive reduction** | Manager reads team lead reports, then reads summaries of those reports | Can't summarize 500 chunks in one prompt -- batch and reduce iteratively |
| **Retrieval != prompt assembly** | Finding the right book is useless if you can only carry 3 home | Fixing search doesn't fix context budgeting |

### 5. AI Leverage

**Use AI for:** Generating chunk summaries (the lossy compression layer), debugging traces (feed retrieval logs in to diagnose weak answers), simulating user questions to test budget adequacy.

**Don't outsource:** Context budget math -- this is deterministic and AI hallucinates numbers. Deciding what counts as "raw evidence" -- the human defines what "grounded" means for their domain.

**One AI workflow (indexing):** *"Summarize this chunk for retrieval. Preserve names, numbers, constraints, and errors. Do NOT answer a hypothetical question."*

**One AI workflow (debugging):** *"Here is the retrieval trace: [paste]. Which chunks were skipped that should have been included? Suggest a budget or chunking adjustment."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Build a toy RAG that fails -- chunk an article, stuff top-3 chunks into 250 tokens, watch it give a garbage answer |
| **Foundation** | 1 hr | Summaries route / raw chunks answer; token budgets are hard constraints; hierarchical search (document first, then chunk) |
| **Application** | 1-2 hr | Take a 50-page PDF, build the three-tier pipeline. Ask 5 questions, print trace for each. Adjust budget until all 5 get correct answers. |
| **Deep Dive** | Optional | Replace toy summarizer with small LLM, swap bag-of-words for real embeddings, add reranking, explore late chunking |

### 7. Go/No-Go Matrix

| If... | Then... |
|-------|---------|
| I want to run AI search on my laptop with <16GB VRAM | Learn this NOW |
| I have 100K+ documents and need sub-second retrieval | Learn this NOW (hierarchical routing scales) |
| I have a tiny corpus (<20 pages) and simple questions | Learn Phase 1 only, then use simple chunking |
| I want a "set it and forget it" RAG | Skip -- this requires ongoing debugging |
| I want to deeply understand retrieval systems | Learn this NOW -- the logic most frameworks abstract away |

> [!TIP] Most RAG failures aren't retrieval failures. They're context-budgeting failures disguised as retrieval failures. Fix the budgeting and you leapfrog 80% of implementations.

## Key Takeaways

- Use summaries for retrieval, raw chunks for answering -- never let the model generate from a summary.
- Token budgets are hard constraints, not suggestions. Use explicit budgeting to decide what reaches the model.
- Search hierarchical: document summaries first → chunk summaries inside selected docs → raw chunks by ID.
- Recursive reduction (batch summaries → higher-level summaries) prevents moving the context-window problem from answer time to indexing time.
- The trace is the product -- print doc hits, chunk hits, included chunks, and skipped chunks for every query.
