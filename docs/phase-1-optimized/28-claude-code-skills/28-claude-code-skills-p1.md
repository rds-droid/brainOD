# Claude Code — Terminal AI Coding Assistant

**Source:** `28-claude-code-skills.md` · **Phase 1** · Cleaned & annotated

## Overview

Claude Code is Anthropic's terminal-based AI coding assistant. You type natural language, it reads your entire codebase, edits files, runs tests, and commits code, all while staying in your terminal. The key differentiator is the subagent system that lets Claude spawn mini-Claudes for parallel tasks, along with hooks, slash-commands, skills, and `CLAUDE.md` for deep customization.

## Core Content

### 1. The Elevator Pitch

Claude Code is a senior developer who lives inside your command line and never needs coffee breaks. It reads your entire repo in one shot, edits files across the project, runs tests, and commits code. With skills, hooks, and subagents, it shifts your workflow from writing code line-by-line to shipping features by intent.

### 2. Why This Matters

- **Unfair advantage:** Ship code 10x faster without context-switching between IDE, browser, and ChatGPT. It reads your entire repo in one shot -- something no other tool does natively.
- **Hidden leverage:** The subagent system lets Claude spawn mini-Claudes for parallel tasks (testing, reviewing, researching). The bigger your codebase, the more it shines.
- **"Aha!" moment:** When you say "refactor this auth system to use JWT" and it touches 12 files, writes tests, and runs them, all while you watch. You stop coding line-by-line and start coding by intent.

### 3. Reality Check

- **Overrated when:** Writing scripts under 100 lines or doing frontend tweaks. Setup overhead isn't worth it for trivial tasks.
- **Opportunity cost:** You're not learning the underlying tools (git internals, testing frameworks, CI/CD). When the AI hallucinates, you need the skills to catch it.
- **Not for:** Purists who believe typing every character builds mastery. People on slow internet (constant token streaming). Anyone who can't tolerate occasional confident wrong answers.

### 4. Core Concepts

| Concept | Analogy | Why Care |
|---------|---------|----------|
| **Skills** | Teaching your barista your exact coffee order | Custom instructions you write once, Claude uses forever |
| **Subagents** | A kitchen with specialized stations instead of one overwhelmed chef | Claude clones itself for parallel tasks (tests, review, research) |
| **Hooks** | Car beeping when you forget your seatbelt | Scripts that auto-run when Claude does things (before saving, after testing) |
| **Slash Commands** | Speed-dial for your most frequent calls | Pre-written prompts for `/commit`, `/test`, `/docs` |
| **CLAUDE.md** | Leaving a detailed note for a house-sitter | README just for Claude -- project rules, conventions, constraints |

### 5. AI Leverage

**Use AI for:** Research (compare auth libraries), summarization (500-file PR → one paragraph), boilerplate (repetitive CRUD, API routes, test scaffolding).

**Don't outsource:** Architecture decisions (AI over-engineers) and security-sensitive code (auth, payments, PII -- trust but verify).

**One AI workflow:** *"Read the entire codebase, identify the 3 most complex functions, and create a /refactor slash command that will safely simplify each one with tests. Run the tests after each change."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Install Claude Code, open any repo, type "Explain this codebase in 3 sentences, then list the 5 most important files" |
| **Foundation** | 1 hr | Context is king (CLAUDE.md preloads rules); subagents are your force multiplier (`/agent`); hooks prevent regret |
| **Application** | 1-2 hr | Prompt Claude to add a complete feature end-to-end (auth with login, logout, protected routes, tests, conventional commit). Don't touch the keyboard. |
| **Deep Dive** | Optional | Build custom skills and hooks for your stack, explore Ralph Wiggum autonomous loop, read Anthropic agentic patterns |

### 7. Go/No-Go Matrix

| If... | Then... |
|-------|---------|
| I want to ship features faster without switching windows | Learn this NOW |
| I care more about deep language mastery than speed | Skip or deprioritize |
| I have a large, complex codebase with many contributors | Learn this NOW |
| I have strict security/compliance requirements | Learn Hooks + review workflows only |
| I only write small scripts or single-file projects | Skip, use ChatGPT instead |
| I want autonomous AI that codes while I sleep | Learn Ralph Wiggum + orchestrators, expect to babysit |

> [!TIP] Claude Code is a force multiplier for experienced developers and a crutch for beginners. If you already know how to code, it makes you 10x faster. If you don't, it makes you 10x more dangerous.

## Key Takeaways

- Claude Code reads the entire repo in one shot -- the only tool that does this natively.
- Subagents (`/agent`) let you parallelize tasks -- one instance tests, one reviews, one refactors.
- Hooks are event-driven safety rails (auto-lint before save, auto-test before commit).
- The `/` slash-command system turns complex workflows into single keystrokes.
- `CLAUDE.md` in your repo root is the single most impactful configuration -- it sets context for every session.
