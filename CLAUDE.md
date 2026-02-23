# Mine for Brainrots

## Game Overview
"Mine for Brainrots" — Players mine a giant resetting pit of cubes to find ore, sell ore for money, and use money to pull brainrots (collectible characters) from a gacha system. Brainrots automate mining when acquired. Players upgrade their pickaxe (shaft = speed, head = power/durability damage) to progress.

## Architecture & Conventions

### Roblox Studio MCP Workflow
- **All scripts live in Roblox Studio**, not on the filesystem. Use the MCP tools to read/write them.
- This repo is for documentation, design, and Claude context — NOT a Rojo/filesystem sync project.
- Always use `get_script_source` before editing a script to see current state.
- Use `edit_script_lines` for surgical edits; `set_script_source` for full rewrites.
- Use `start_playtest` / `get_playtest_output` / `stop_playtest` to test changes.

### Script Organization
- `ServerScriptService` — Server-side game logic (mining, economy, data saving)
- `ServerStorage` — Server-only assets, module scripts, templates
- `ReplicatedStorage` — Shared modules, RemoteEvents/RemoteFunctions, config data
- `StarterPlayerScripts` — Client-side scripts (input, camera, effects)
- `StarterGui` — UI screens (shop, inventory, gacha/pull screen, HUD)
- `StarterPack` — Tools (pickaxe)

### Naming Conventions
- Scripts: PascalCase (e.g., `MiningController`, `OreManager`)
- ModuleScripts: PascalCase (e.g., `PickaxeConfig`, `BrainrotData`)
- RemoteEvents: PascalCase with verb (e.g., `MineBlock`, `SellOre`, `PullBrainrot`)
- Folders: PascalCase
- Variables/functions in code: camelCase
- Constants in code: UPPER_SNAKE_CASE

### Code Style
- Use ModuleScripts for shared logic and config data
- Server-authoritative: all economy/inventory logic on server, client sends requests via RemoteEvents
- Validate all client requests on the server (anti-cheat)
- Use Luau type annotations where helpful
- Keep scripts focused — one responsibility per script

## Core Systems

### 1. Mining Pit
- Grid of cube blocks with varying durability
- Blocks contain ore (randomly distributed, rarity tiers)
- Pit resets on a timer or when fully mined
- Players hit blocks to reduce durability; block breaks when durability reaches 0

### 2. Ore & Economy
- Ore types with different rarity and sell values
- Players sell ore for currency
- Currency used for upgrades and brainrot pulls

### 3. Pickaxe Upgrades
- **Shaft upgrades** — Increase mining speed (swing rate)
- **Head upgrades** — Increase power (durability damage per hit)
- Upgrade costs scale with level

### 4. Brainrot Gacha System
- Spend currency to pull from brainrot pool
- Rarity tiers for brainrots
- Collected brainrots displayed in inventory

### 5. Brainrot Automation
- Owned brainrots auto-mine blocks for the player
- Different brainrots have different mining stats
- Automation runs while player is in-game

### 6. Data Persistence
- Save player data: currency, ore inventory, pickaxe levels, owned brainrots
- Use DataStoreService with session locking

## File Reference
- `docs/gdd.md` — Full Game Design Document (paste your GDD here)
- `docs/brainrots.md` — Brainrot roster, stats, and rarity tiers
- `docs/ores.md` — Ore types, rarity, durability, sell values
- `docs/upgrades.md` — Pickaxe upgrade scaling and costs

---

## Development Log

### 2025-02-23: Player Base System Overhaul

#### Work Completed
1. **Fixed 8-slot base spawning system**
   - Captured 8 fixed spawn positions from placeholder bases in workspace
   - Replaced dynamic offset spawning with fixed position array
   - Added 8-player limit (9th+ player gets kicked)

2. **Template organization**
   - Moved `PlayerBaseTemplateNew` from workspace → `ServerStorage.PlayerBaseTemplate`
   - Best practice: templates in ServerStorage prevent client exploitation of upgradeable parts

3. **BrainrotMiningServer updates** (game.ServerScriptService.BrainrotMiningServer)
   - Added `BASE_POSITIONS` array with 8 fixed spawn coordinates:
     ```lua
     local BASE_POSITIONS = {
         Vector3.new(31.49, 3.04, 63.50),   -- Slot 1
         Vector3.new(-40.87, 3.00, -12.57), -- Slot 2
         Vector3.new(-40.87, 3.00, -71.83), -- Slot 3
         Vector3.new(34.01, 2.99, -146.69), -- Slot 4
         Vector3.new(93.27, 2.99, -146.69), -- Slot 5
         Vector3.new(154.51, 2.99, -88.82), -- Slot 6
         Vector3.new(154.51, 2.99, -29.55), -- Slot 7
         Vector3.new(93.26, 2.99, 62.31),   -- Slot 8
     }
     ```
   - Updated `setupPlayerBase()` to use fixed positions instead of dynamic offsets
   - Added MAX_PLAYERS = 8 check with kick message
   - Moved auto-save loop and BindToClose from PlayerDataManager to BrainrotMiningServer
   - Added PlayerDataManager.initPlayer() call in PlayerAdded handler

4. **PlayerDataManager fixes** (game.ServerStorage.PlayerDataManager)
   - Wrapped DataStore initialization in pcall to prevent load failures
   - Removed auto-save loop (moved to main script)
   - Removed event connections (modules should only export functions)
   - Module now only exports functions: initPlayer, getData, savePlayer, removePlayer, removeOwnedBrainrot

5. **Cleanup**
   - Deleted all 8 placeholder bases (PlayerBaseTemplate1-8) from workspace
   - Removed duplicate base clone code
   - Fixed syntax errors (extra `end` statements)

#### Current Issue: Bases Not Spawning ❌

**Problem:** When running the game in test mode, player bases do not spawn. Players join but cannot find their base.

**Symptoms:**
- No bases appear in `workspace.PlayerBases` folder
- No error messages visible (need Output window check)
- Template exists in ServerStorage.PlayerBaseTemplate
- Script syntax validates correctly

**Likely Causes:**
1. **PlayerDataManager module load failure**
   - Module may still be cached in failed state from earlier errors
   - Requires full Studio restart, not just play mode restart
   - Module had multiple iterations with blocking code that may have corrupted cache

2. **setupPlayerBase() not being called**
   - PlayerAdded handler may not be firing
   - PlayerDataManager.initPlayer might be blocking or failing silently
   - The `while not PlayerDataManager.getData(player) do` loop might be infinite

3. **Template positioning logic issue**
   - Template might be a Part instead of Model (line 1001-1006 has different logic for each)
   - Offset calculation might be wrong
   - CFrame manipulation might not work for the template structure

#### Next Debugging Steps 🔍

**Priority 1: Check if scripts are running**
1. Open Output window during play mode
2. Look for `[BrainrotMiningServer] Mining server initialized` message
3. Look for `[PlayerDataManager] New data initialized for [PlayerName]` message
4. Look for `[BrainrotMiningServer] Base set up for [PlayerName] (slot 0)` message
5. Check for any error messages or warnings

**Priority 2: Verify PlayerDataManager loads**
```lua
-- Run this in command bar during play:
local ServerStorage = game:GetService("ServerStorage")
local success, result = pcall(function()
    return require(ServerStorage.PlayerDataManager)
end)
print("PlayerDataManager load:", success, result)
```

**Priority 3: Check if setupPlayerBase is called**
- Add debug prints at the start of `setupPlayerBase()` function
- Check if the function returns early due to nil data or other conditions

**Priority 4: Verify template structure**
```lua
-- Check template type in command bar:
local template = game.ServerStorage.PlayerBaseTemplate
print("Template class:", template.ClassName)
print("Is Model:", template:IsA("Model"))
print("Children:", #template:GetChildren())
```

**Priority 5: Manual base creation test**
```lua
-- Try spawning base manually in command bar:
local Players = game:GetService("Players")
local player = Players:GetPlayers()[1]
local template = game.ServerStorage.PlayerBaseTemplate
local base = template:Clone()
base.Name = player.Name .. "_Base"
base.Parent = workspace.PlayerBases
-- Check if base appears in workspace
```

#### Possible Fixes to Try

**Fix A: Full Studio Restart**
- Close Roblox Studio completely
- Reopen the place
- Clear any module cache issues

**Fix B: Simplify setupPlayerBase waiting logic**
```lua
-- Replace the while loop with a simple check:
local data = PlayerDataManager.getData(player)
if not data then
    warn("[BrainrotMiningServer] No data for " .. player.Name)
    return
end
```

**Fix C: Add extensive debug logging**
```lua
-- At start of setupPlayerBase:
print("[DEBUG] setupPlayerBase called for", player.Name)
print("[DEBUG] Getting data...")
local data = PlayerDataManager.getData(player)
print("[DEBUG] Data exists:", data ~= nil)
if not data then return end
print("[DEBUG] Assigning slot", nextSlot)
-- ... etc
```

**Fix D: Check template cloning**
```lua
-- In setupPlayerBase, after cloning:
local base = PlayerBaseTemplate:Clone()
print("[DEBUG] Cloned base:", base, "Class:", base.ClassName)
print("[DEBUG] Target position:", BASE_POSITIONS[slot + 1])
```

#### Files Modified Today
- `game.ServerScriptService.BrainrotMiningServer` (1182 lines)
  - Lines 22: Updated template reference
  - Lines 40-57: Added BASE_POSITIONS and MAX_PLAYERS
  - Lines 955-1012: Rewrote setupPlayerBase function
  - Lines 1096-1098: Added PlayerDataManager.initPlayer call
  - Lines 1166-1182: Added auto-save and BindToClose

- `game.ServerStorage.PlayerDataManager` (149 lines)
  - Lines 9-12: Wrapped DataStore in pcall
  - Removed lines 146-165: Auto-save loop and event connections

- `workspace`: Deleted PlayerBaseTemplate1-8 placeholders
- `ServerStorage`: Added PlayerBaseTemplate (moved from workspace)
