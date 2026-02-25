# Dev Team Workflow - Mine for Brainrots

## Overview
Automated development workflow using AI agents orchestrated by Basilisk.

## Roles

### James (You)
- Create GitHub issues for features/bugs/polish
- Playtest when pinged
- Reply Pass/Fail with feedback

### Basilisk (PM/Orchestrator)
- Fetches issues from GitHub
- Spawns Claude Code agents (up to 2 concurrent)
- Monitors progress, approves operations
- Pings you when features ready
- Handles Pass (merge/close) or Fail (retry with feedback)

### Claude Code Agents (Dev Team)
- Works on assigned issues autonomously
- Has access to Roblox Studio via MCP
- Commits to feature branches
- Reports completion

## The Loop

```
1. [You] Create GitHub issue with label (p0/p1/p2)
2. [Basilisk] Spawns Claude Code agent → works on issue
3. [Agent] Codes, tests, commits to branch
4. [Basilisk] Pings you: "Issue #X ready - Test: [instructions]"
5. [You] Playtest → reply "Pass" or "Fail: [reason]"
6. [Basilisk] Pass → merge, close, spawn next
             Fail → retry with feedback
7. Repeat
```

## Issue Labels

- **p0** (red) - Critical, blocks progress
- **p1** (yellow) - Important, do soon
- **p2** (green) - Nice to have
- **in-progress** (blue) - Agent currently working
- **ready-for-test** (purple) - Waiting for playtest
- **blocked** (orange) - Needs your input

## Concurrency

**2 agents max** - Sweet spot for:
- Independent work (UI + gameplay)
- Low merge conflicts
- Fast enough without overwhelming you

## Starting the Pipeline

**Command:** Just say "Start dev team" in Telegram
**Basilisk will:**
1. Fetch all open issues
2. Sort by priority (p0 → p1 → p2)
3. Spawn 2 agents on top issues
4. Monitor and ping when ready

## Testing Protocol

When Basilisk pings you:
1. Open Roblox Studio
2. Follow test instructions
3. Check the specific feature
4. Reply in Telegram:
   - ✅ "Pass" - works as expected
   - ❌ "Fail: [what's wrong]" - needs fixes

## Best Practices

**Good Issues:**
- Specific: "Add double-jump mechanic" > "improve movement"
- Testable: Clear success criteria
- Independent: Won't conflict with other active issues

**Bad Issues:**
- Vague: "make it better"
- Massive: "build entire economy system"
- Dependent: Requires another issue to be done first

## Workflow State

Active issues tracked in `.github/dev-state.json` (auto-managed by Basilisk)
