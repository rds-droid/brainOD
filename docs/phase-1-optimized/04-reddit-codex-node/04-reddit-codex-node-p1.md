# OpenCode in n8n — Building a Bridge vs. ProDex/Codex

**Source:** `04-reddit-codex-node.md` · **Phase 1** · Cleaned & annotated

## Overview

A Reddit discussion thread about ProDex (an n8n community node integrating OpenAI Codex), followed by a deep analysis of whether you can achieve the same with OpenCode inside n8n, and broader browser-automation/MCP research architectures for n8n orchestration.

## Core Content

### Part 1: ProDex — What It Does

ProDex (`n8n-nodes-prodex`) is a community node that integrates OpenAI Codex into self-hosted n8n workflows.

**Key features:**
- Subscription-based device login auth (no API key metering)
- Full Codex agent path: sandbox modes, working directory, JSON output, thread memory (new/continue/resume)
- Skills system: install/list/invoke SKILL.md files for reusable expertise
- Chat Model node: plugs into n8n's native AI Agent for Codex-backed chat

**Limitations (self-admitted by author):**
- Self-hosted n8n only
- ProDex Chat Model ≠ full tool-calling agent
- Does not auto-edit workflows yet

### Part 2: Can You Do This with OpenCode?

**Short answer: Yes, but not the same kind of integration.**

OpenCode CLI capabilities:
| Flag | What It Does |
|------|-------------|
| `opencode` | Launches interactive TUI |
| `opencode -p "prompt"` | Non-interactive mode — runs once, exits |
| `opencode -p "prompt" -f json -q` | JSON output, quiet mode — ideal for scripts |
| `opencode -c /path` | Set working directory |

**Three approaches to bridge OpenCode into n8n:**

**Path 1: Shell Execution (Easiest, most brittle)**
```
n8n → [Execute Command node] → opencode -p "..." -f json -q
```
- Works today with n8n's built-in node
- No session persistence — each call is stateless
- No thread memory — unlike ProDex's continue/resume
- `-p` auto-approves all permissions (risky)

**Path 2: Custom n8n Node (Like ProDex, harder)**
- Spawns OpenCode as child process
- Manages config and parses JSON output
- Problem: OpenCode has no programmatic API — you're shelling out to a TUI app

**Path 3: Fork/Extend OpenCode (Most powerful, most work)**
- Add HTTP API or JSON-RPC interface
- Expose session management endpoints
- You're now maintaining a Go fork of an archived project

### Part 3: Better Alternative — n8n + Browser Automation

Instead of wedging OpenCode into n8n, use n8n as the orchestrator and MCP/browser tools as workers:

**Architecture 1: n8n + MCP Server (Headless Browser)**
```
n8n workflow → HTTP Request → MCP server → Playwright/Browser-Use → structured data back to n8n
```

**Architecture 2: n8n + Background Agent (Loosely Coupled)**
```
n8n writes job file → background agent processes → n8n polls or receives callback
```

**Specific tools discussed:**
- **Browser-Use (Open Source)** — LLM-controlled browser agent, handles dynamic JS, login flows, multi-step tasks. Python-based, run as separate service.
- **Playwright MCP** — Battle-tested browser automation, good for structured automation but doesn't reason like an agent.
- **AG-UI Protocol** — Frontend-to-agent protocol, not relevant for n8n orchestration (skip it).

> [!TIP] The author's bottom line: Don't try to build the entire agent inside n8n. Use n8n for orchestration/scheduling, Browser-Use for rendering/interacting, lightweight agents (Goose, custom Python) for adaptive reasoning, and connect them with simple HTTP or message queues.

### Part 4: Context Problem Solutions

| Option | Effort | Description |
|--------|--------|-------------|
| Session Files | Simple | n8n writes a JSON context file, agent reads/appends |
| Thread Memory | Complex | Needs an agent with programmatic session hooks |
| n8n Built-in Memory | Simplest | Each research step outputs to the next node — no external session needed |

### Comparison: ProDex vs. OpenCode Bridge

| Feature | ProDex (Codex) | Your OpenCode Bridge |
|---------|---------------|---------------------|
| Auth | Subscription device login | API keys/env vars |
| Session/Memory | Built-in (new/continue/resume) | None by default |
| Cost | Subscription-based | Pay for whatever API you configure |
| Sandbox | Codex's built-in | OpenCode's bash tool (runs on your machine) |
| Installation | `npm install` community node | Shell exec or custom node |

## Key Takeaways

1. **OpenCode can be called from n8n** via the Execute Command node with `-p` flag, but it's stateless and brittle — not a replacement for a proper API integration.
2. **ProDex works because Codex has an API.** OpenCode is a terminal app, not a service — the architectural mismatch makes a clean integration much harder.
3. **Better pattern:** n8n orchestrates, separate agent services (Browser-Use, Goose, custom Python) do the heavy lifting, connected via HTTP or message queues.
4. **The "context problem"** for research loops is solvable with session files or n8n's built-in data flow — no need for complex thread memory.
