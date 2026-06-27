# Building Your First MCP Server

**Source:** `24-first-mcp-server.md` · **Phase 1** · Cleaned & annotated

## Overview

MCP (Model Context Protocol) servers are bridges that give AI assistants the ability to interact with the real world -- APIs, files, databases, and more. You write a tiny TypeScript/Python file defining tools with descriptions and input schemas, and the AI discovers them automatically. No web framework, no deployment, just a script that connects AI to live data and actions.

## Core Content

### 1. The Elevator Pitch

MCP servers are USB ports for AI. Right now your AI is a brain with no hands -- it can talk about the weather but can't check it. MCP fixes that. You write a single file with a tool definition (name + description + inputs + a function), and the AI learns about it automatically and starts using it when relevant.

### 2. Why This Matters

- **Unfair advantage:** Make AI do anything you can code -- browse the web, query databases, create PRs, check your calendar. Everyone else is stuck with built-in tools; you build your own.
- **Hidden leverage:** Write once, use everywhere. One MCP server works with VS Code Copilot, Claude Desktop, Cursor, and any MCP-compatible client.
- **"Aha!" moment:** The AI doesn't just call your function -- it discovers it. You describe the tool in plain English and the AI figures out when to use it. You're programming capabilities, not behavior.

### 3. Reality Check

- **Overrated when:** You just want AI to write code or answer questions. MCP is only worth it for live data or real actions the AI can't do out of the box.
- **Opportunity cost:** You're learning a protocol, not a product. MCP might evolve or be replaced. Meanwhile you could be learning API design, TypeScript, or cloud functions.
- **Not for:** Non-coders, browser-only AI users, anyone without a specific "I wish my AI could do X" problem.

### 4. Core Concepts

| Concept | Analogy | Why Care |
|---------|---------|----------|
| **Server** (the `.ts`/`.py` file) | Lego baseplate -- snap tools onto it | One file, one bridge between AI and the real world |
| **Tool** (function + metadata) | Labeled button -- "Popcorn" button on microwave | Name, describe, define inputs. AI presses it when needed. |
| **Zod/Schema** | Bouncer -- validates data before your code runs | Prevents crashes from bad input |
| **Transport** (STDIO/HTTP) | Walkie-talkie -- how server and AI talk | STDIO for local, HTTP for remote. Pick one and move on. |
| **Inspector** | Car dashboard -- verify engine is running before hitting the road | Web UI to test tools without writing test scripts |

### 5. AI Leverage

**Use AI for:** Boilerplate generation (scaffold main.ts, package.json, Zod schema), API integration (paste API docs into AI to write fetch logic), debugging transport errors.

**Don't outsource:** Understanding the protocol flow (why `StdioServerTransport` exists, how AI discovers tools), naming and describing tools (bad descriptions = AI never uses your tool).

**One AI workflow:** *"I want to build an MCP server that [does X]. Give me the complete main.ts using the MCP SDK, with Zod validation, error handling, and a test using the MCP Inspector command."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Scaffold a fake weather tool that returns "sunny", run it in the Inspector, see your tool listed |
| **Foundation** | 1 hr | Tools are functions + metadata; Transport is the pipe; AI decides when to call (not you) |
| **Application** | 1-2 hr | Replace fake weather with real Open-Meteo API + geocoding. Wire into VS Code Copilot and ask "What's the weather in Tokyo?" |
| **Deep Dive** | Optional | Resources, prompts, sampling, HTTP/SSE transport for remote servers |

### 7. Go/No-Go Matrix

| If... | Then... |
|-------|---------|
| I want my AI to access live data (weather, stocks, files, APIs) | Learn this NOW |
| I use Claude Desktop or VS Code Copilot regularly | Learn this NOW |
| I only use ChatGPT via web browser | Skip |
| I have zero coding experience | Learn Python/TS basics first |
| I have 1-2 hours this weekend and basic JS/Python | Do Phase 1-3 -- you'll have a working server |

> [!TIP] MCP is not building for a platform. It's building for a protocol. One server works everywhere MCP is supported.

## Key Takeaways

- An MCP server is a single file with tool definitions (name + description + schema + function).
- The AI discovers your tools automatically -- you don't code "if/then" logic for when to call them.
- Zod schemas are the contract between AI and your code; they validate inputs before execution.
- The MCP Inspector is your debugger -- use it before wiring into any client.
- Start with STDIO transport (local). Add HTTP/SSE for remote access later.
