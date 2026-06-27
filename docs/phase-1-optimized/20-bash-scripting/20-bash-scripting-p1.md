# Bash Scripting for Linux SysAdmin Automation

**Source:** `20-bash-scripting.md` · **Phase 1** · Cleaned & annotated

## Overview

Bash scripting automates repetitive Linux server tasks by chaining commands with logic (if/then, loops, variables) and scheduling them with cron. Instead of typing the same commands daily (disk checks, service restarts, backups), write them once and let them run automatically.

## Core Content

### 1. The Elevator Pitch

Tiny instruction sets that your Linux server follows automatically. Check disk space, restart crashed services, back up files — write once, schedule, they run while you sleep. A robot intern that never forgets and works 24/7 for free.

### 2. Why This Matters

- **Unfair advantage:** Scripters manage 50 servers with the same effort others spend on 5. Go from reactive firefighting to proactive prevention.
- **Hidden leverage:** 30 minutes automating a daily task pays back 3 hours in the first month. After a year, you've reclaimed weeks and eliminated categories of human error.
- **"Aha!" moment:** "If I can type it, I can script it." The commands you already know (`df`, `systemctl`, `tar`, `grep`) are the building blocks. Scripting is just chaining them with logic.

### 3. Reality Check

- **Overrated when:** Everything is containerized and managed by Kubernetes — Bash is diminishing returns. Modern platforms (Lambda, GitHub Actions, Ansible) handle automation at a higher level.
- **Opportunity cost:** Python is more powerful, readable, and has better error handling. Bash is a local optimum; Python is often the global one.
- **Not for:** Windows-only users, people exclusively on managed cloud services, or anyone who finds the command line intimidating.

### 4. Core Concepts

| Concept | What It Does | Analogy |
|---------|-------------|---------|
| **Variables** | Store values for reuse | Contact name instead of memorizing number |
| **Conditionals** | IF/THEN logic gates | Nightclub bouncer |
| **Loops** | Repeat across targets | Factory worker checking each machine |
| **Cron** | Scheduled execution | Alarm clock that rings forever |
| **Pipes** | Chain commands together | Conveyor belt with specialized chefs |
| **Exit Codes** | Success/failure signals | Report cards |

### 5. AI Leverage

**Use AI for:** Code review and debugging, template generation, translating cryptic one-liners, cron schedule translation.

**Don't outsource:** Understanding the actual problem (only you know which directories matter), security decisions (`chmod 777` is dangerous), debugging in production at 2 AM.

**One AI workflow:** *"I need a Bash script that checks if my website responds with HTTP 200, restarts Nginx if not, logs to /var/log/health.log. Ubuntu 22.04. Include error handling and the exact cron entry for every 5 minutes."*

### 6. Learning Map

| Phase | Time | Goal |
|-------|------|------|
| **Hook** | 15 min | Write a disk usage check script. Print warning if >80%. Run instead of typing `df -h` manually. |
| **Foundation** | 1 hr | 3 principles: variables & quoting; test operators (`-f`, `-z`, `-gt`); redirection & logging |
| **Application** | 1–2 hr | Build "server health dashboard": disk + memory + top 5 CPU + service status in one report. Schedule with cron. |
| **Deep Dive** | Optional | `set -euo pipefail`, `trap`, `getopts`. Then graduate to Python for anything >100 lines. |

### 7. Go/No-Go

| Situation | Verdict |
|-----------|---------|
| Manage Linux servers, hate repetitive SSH | 🟢 **Learn this NOW** |
| Automate backups/monitoring without SaaS | 🟢 **Learn this NOW** |
| Building web apps, data science, mobile | 🟡 Learn Python instead |
| Zero command line experience | 🔴 Learn basic commands first |
| 100% Windows, no WSL/Linux | 🔴 PowerShell or Python is your path |
| Managed cloud only (RDS, Vercel) | 🟡 Read existing scripts, don't deep dive |

## Key Takeaways

1. **Bash is the duct tape of system administration** — not pretty, but it saves your sleep and your servers.
2. The 20% (variables, conditionals, loops, cron) handles 80% of real-world problems.
3. Always quote variables and check exit codes. Those two habits prevent 90% of script failures.
4. For anything over 100 lines, use Python. Bash is for quick automation, not application logic.
