# Dev Team Workflow - Updated

## Pre-Flight Checklist (REQUIRED BEFORE SPAWNING AGENTS)

### Step 1: Verify MCP Connection
```bash
cd ~/Dev/games/roblox/mine-for-brainrots
.github/test-mcp.sh
```

**Must see:**
- ✅ .mcp.json found
- ✅ Port 58741: Responding
- ✅ Port 58742: Responding  
- ✅ Port 58743: Responding

**If any port fails:**
1. Open Roblox Studio
2. Load the mine-for-brainrots project
3. Enable the MCP plugin
4. Re-run test

### Step 2: Check Available Agent Slots
- Port 58741 → Agent 1
- Port 58742 → Agent 2
- Port 58743 → Agent 3

**Max 3 concurrent agents** (one per MCP port)

### Step 3: Spawn Agent
Only spawn after MCP test passes.

---

## Starting the Dev Team

**Command:** "Start dev team"

**Basilisk will:**
1. Run MCP pre-flight check
2. If MCP fails → notify you, wait for Studio to be ready
3. If MCP passes → fetch issues, spawn agents
4. Monitor progress and ping when ready to test

---

## Current Status

**MCP Ports:** ✅ All 3 responding
**Active Agents:** 2 running
**Available Slots:** 1 free (port 58743)

---

## Lessons Learned

- **Always test MCP before spawning** - agents can't work without Studio MCP connection
- **Visible terminals** - easier to debug and approve prompts
- **One agent per MCP port** - prevents connection conflicts
