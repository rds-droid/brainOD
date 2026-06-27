# Bash: Append Text to Multiple Files

**Source:** `03-simplify-bash-append.md` · **Phase 1** · Cleaned & annotated

## Overview

A beginner-to-intermediate guide on using the `>>` append operator inside `for` loops to bulk-modify files. Focused on real DevOps/SysAdmin scenarios: log rotation annotations, config mass-updates, CI/CD tagging, and audit trails.

## Core Content

### The Core Concept

The article teaches bulk file modification using `>>` (append operator) inside a `for` loop. For DevOps/SysAdmin, this applies to:

- Log rotation annotations — appending timestamps before archiving
- Config mass-updates — adding a directive to 50 nginx virtual host files
- Infrastructure tagging — labeling generated files during CI/CD
- Audit trails — appending "modified by [user] at [time]" for compliance

### Step-by-Step Progression

**Step 1: The building block — append to ONE file**

```bash
echo "hello world" >> myfile.txt
```

> `>>` appends to the end. `>` replaces the whole file. Don't mix them up.

**Step 2: Turn it into a script**

```bash
#!/bin/bash
echo "This is the appended text" >> filename.txt
```

Save, `chmod +x`, and run with `./script.sh`.

**Step 3: Append to MULTIPLE files with a loop**

```bash
#!/bin/bash
DIRECTORY="/home/yourname/documents"
TEXT="This is the appended text for all files."

for FILE in "$DIRECTORY"/*.txt; do
  echo "$TEXT" >> "$FILE"
  echo "Done: $FILE"
done
```

**Step 4: Add safety checks**

```bash
if [ -f "$FILE" ]; then  # Only if it's a real file (skip dirs, broken links)
```

**Step 5: Idempotency — don't add the same text twice**

```bash
if ! grep -qF "$TEXT" "$FILE"; then
  echo "$TEXT" >> "$FILE"
fi
```

> `grep -qF` — the `-F` flag treats text as a fixed string, not regex. Essential when text contains dots or special characters.

### Production Script Template

```bash
#!/bin/bash
#==================================================
# Script: append_text.sh
# Purpose: Append text to multiple files safely
#==================================================

# --- Configuration ---
DIRECTORY="/path/to/your/files"
PATTERN="*.conf"
TEXT="# Managed by Ansible - $(date)"

# --- Safety Checks ---
if [ ! -d "$DIRECTORY" ]; then
    echo "ERROR: Directory $DIRECTORY does not exist."
    exit 1
fi

# --- Dry-Run Mode (comment out to execute) ---
# DRY_RUN=true

# --- Main Logic ---
for FILE in "$DIRECTORY"/$PATTERN; do
    if [ -f "$FILE" ]; then
        if ! grep -qF "$TEXT" "$FILE"; then
            if [ "$DRY_RUN" = true ]; then
                echo "[DRY-RUN] Would append to: $FILE"
            else
                echo "$TEXT" >> "$FILE"
                echo "[OK] Appended to: $FILE"
            fi
        else
            echo "[SKIP] Already exists in: $FILE"
        fi
    fi
done
echo "Done."
```

### Quick Reference

| Symbol/Command | What It Does |
|----------------|-------------|
| `>` | Write to file (OVERWRITES everything) |
| `>>` | Append to file (adds to end) |
| `#!/bin/bash` | Declares this is a bash script |
| `chmod +x` | Makes script executable |
| `for ... in ...` | Loop through a list of items |
| `if [ -f ... ]` | Check if something is a regular file |
| `grep -qF` | Search quietly as fixed string (no regex) |
| `!` | Flip the result (NOT) |

### Real DevOps Scenarios

| Scenario | How This Helps |
|----------|---------------|
| Configuration Management | Append local overrides without replacing the whole file |
| CI/CD Pipelines | Append build numbers or git SHAs to `.env` files |
| Monitoring Setup | Bulk-add log collector configs to multiple server paths |
| Security Hardening | Append `umask` or `ulimit` settings to all `.bashrc` files |
| Disaster Recovery | Tag files with backup timestamps before rsync |

> [!TIP] Always test on a copy first: `cp -r /etc/nginx/sites-available /tmp/nginx-test`. Add `tar czf backup-$(date +%F).tar.gz "$DIRECTORY"` before bulk operations.

## Key Takeaways

1. `>>` appends, `>` overwrites — this distinction is the foundation of all file-writing scripts.
2. Always check `[ -f "$FILE" ]` inside loops — directories and broken symlinks will break your script.
3. Idempotency matters: `grep -qF` before appending prevents duplicate lines on re-runs.
4. Dry-run mode (`DRY_RUN=true` pattern) is a cheap insurance policy for production scripts.
5. The script template above is production-ready for config management, CI/CD, and audit scenarios.
