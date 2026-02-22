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
