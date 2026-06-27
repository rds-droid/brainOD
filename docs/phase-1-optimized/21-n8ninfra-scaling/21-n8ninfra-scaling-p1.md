# n8n Infrastructure Scaling — Beginner to Scale

**Source:** `21-n8ninfra-scaling.md` · **Phase 1** · Cleaned & annotated

## Overview

How you host n8n determines whether it handles 10 tasks a day or 400,000 a month. Three infrastructure tiers: a $6 hobby server (SQLite), a $30 production setup (PostgreSQL), and a distributed system (Redis workers). Core idea: start embarrassingly simple, upgrade only when your metrics scream at you.

## Core Content

### 1. The Elevator Pitch

Automate like a Fortune 500 company for the cost of a pizza. Self-hosted n8n starts at $6/month vs. $50–500/month for Zapier/Make. 10–80× cheaper for the same outcome. The catch: your database choice determines your ceiling.

### 2. Why This Matters

- **Cost advantage:** Self-hosted n8n at $6 vs. Zapier at $50–500/month.
- **Transferable skill:** The scaling pattern (SQLite → PostgreSQL → Redis queue) applies to virtually every growing web app.
- **"Aha!" moment:** Your database choice is your bottleneck, not your code. SQLite is fine for testing but chokes on concurrency. Switch to PostgreSQL and everything "broken" suddenly works.

### 3. Reality Check

- **Overrated when:** You run fewer than 100 workflows/day — you'll never need PostgreSQL or Redis. The "scale tier" is a flex, not a requirement.
- **Opportunity cost:** Learning Docker, PostgreSQL, Redis vs. building useful workflows. A broken automation on a "scale" server is worth less than a working one on a $6 box.
- **Not for:** People who value "it just works" over cost savings (use n8n Cloud at $24/mo), anyone without basic Linux/Docker comfort, teams with no backup discipline.

### 4. Core Concepts

| Tier | Setup | Analogy |
|------|-------|---------|
| **Tier 1: $6 Experiment** | Single droplet, SQLite | Scooter — cheap, gets you moving |
| **Tier 2: Real Database** | PostgreSQL | Car — handles traffic, passengers, weather |
| **Tier 3: Highway System** | Redis workers | Extra lanes and toll booths |
| **Backups** | Insurance policy | Fire insurance for a house you built |
| **Migration Signal** | `SQLITE_BUSY` errors | Check engine light |

### 5. AI Leverage

**Use AI for:** Translating n8n docs into Docker Compose files, generating PostgreSQL connection strings, debugging SQLITE_BUSY errors, writing cron jobs for backups.

**Don't outsource:** Deciding WHEN to upgrade (only your metrics know), understanding workflow volume and team pain points, actually testing backups.

**One AI workflow:** *"I'm migrating n8n from SQLite to PostgreSQL on a DigitalOcean droplet with [X] workflows and [Y] daily executions. Give me step-by-step migration plan, Docker Compose, and rollback strategy."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Spin up a $6 droplet with one-click n8n install. Build one automation. |
| **Foundation** | 1 hr | 3 principles: workflows are triggers+actions; database is your ceiling; backups are part of the product |
| **Application** | 1–2 hr | Migrate a working SQLite instance to PostgreSQL. Document the process. |
| **Deep Dive** | Optional | Read queue mode docs, set up Redis, simulate 50+ concurrent workflows |

### 7. Go/No-Go

| Situation | Verdict |
|-----------|---------|
| Personal automation, zero headaches | 🟢 Start with n8n Cloud ($24/mo) |
| Save money > save time | 🟢 Self-host $6 droplet with SQLite |
| Team of 3+ editing workflows | 🟢 Skip to PostgreSQL immediately |
| 5,000+ daily executions, see SQLITE_BUSY | 🟢 Migrate to PostgreSQL this week |
| Building automations > managing servers | ⏳ Use n8n Cloud, ignore self-hosting |
| Zero Linux/Docker experience | ⚠️ Learn Cloud tier only |
| 100+ daily execs, no backup system | ⚠️ Learn backup strategy ONLY |

## Key Takeaways

1. **Most people over-engineer Tier 3 while under-engineering Tier 1 backups.** Don't be most people.
2. `SQLITE_BUSY` errors are your signal to migrate to PostgreSQL. Don't ignore them.
3. The scaling pattern (SQLite → PostgreSQL → Redis) is transferable knowledge to any web application.
4. If you can't restore a backup, you don't own your data. Test restores, not just backups.
