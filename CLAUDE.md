# Mine for Brainrots

## Game Overview
"Mine for Brainrots" — Players mine a giant resetting pit of cubes to find ore, sell ore for money, and use money to pull brainrots (collectible characters) from a gacha system. Brainrots automate mining when acquired. Players upgrade their pickaxe (shaft = speed, head = power/durability damage) to progress.

## Quick Reference — Instance Map

### Server Scripts (`game.ServerScriptService`)
| Script | Lines | Purpose |
|--------|-------|---------|
| `BrainrotMiningServer` | 1240 | Main server script: base spawning, brainrot placement/mining loops, collector squares, carry system, rebirth cleanup hook, auto-save, PlayerAdded/Removing |
| `PitGenerator` | 211 | Generates the mining pit from PitConfig (20x20x20 layers, 145k blocks) |
| `MiningSystem` | 89 | Handles pickaxe mining (MineBlock event), block damage/destroy |
| `ShopServer` | 120 | Sell ore (with rebirth multiplier), buy upgrades incl. pickaxe tier (SellOre, BuyUpgrade events) |
| `GachaServer` | 76 | Gacha pulls (SpinGacha event → GachaResult) |
| `RebirthServer` | 72 | Rebirth system: validates pickaxe tier gate, fires cleanup, resets data, notifies client |
| `AdminServer` | 161 | Admin commands (AdminCommand RemoteFunction) |

### Server Modules (`game.ServerStorage`)
| Module | Lines | Purpose |
|--------|-------|---------|
| `PlayerDataManager` | 188 | DataStore save/load. Exports: `initPlayer`, `getData`, `savePlayer`, `removePlayer`, `removeOwnedBrainrot`, `performRebirth` |

### Server Assets (`game.ServerStorage`)
| Instance | Type | Details |
|----------|------|---------|
| `BlockTemplates/` | Folder | 7 block parts: Block_Grass, Block_Dirt, Block_Stone, Block_Stone_Coal, Block_Stone_Redstone, Block_Stone_Gold, Block_Stone_Diamond |
| `BrainrotModels/` | Folder | 105 brainrot Models (each has RootPart, FakeRootPart, AnimationController, mesh parts) |
| `PlayerBaseTemplate` | Part (49x1x60) | Base floor plate. Children: Stairs (Model, 30 stair Parts), CollectorSquare through CollectorSquare_7 (8 Parts, each with "base" child), Pillar1-4, Backyard, Roof, conveyour 1, conveyour 2 |
| `RebirthCleanup` | BindableEvent | Fired by RebirthServer to trigger cleanup in BrainrotMiningServer |

### Shared Config (`game.ReplicatedStorage.Modules`)
| Module | Lines | Key Data |
|--------|-------|----------|
| `PitConfig` | 82 | Pit origin `(0, 2.5, -100)`, 20x20 blocks, BLOCK_SIZE=5, 20 LAYER_DEFINITIONS, PICKAXE_TIERS (0-5), ORE_VALUES, DURABILITY, RESET_TIME=120s |
| `BrainrotConfig` | 192 | SQUARE_NAMES (8 squares), RARITIES (Common→Mythic with miningSpeed/pickaxeTier), GACHA_TIERS (Basic/Premium/Ultra), BRAINROT_POOL (105 names across 6 rarities), SELL_PRICES |
| `ShopConfig` | 40 | Shop upgrade costs/scaling |
| `RebirthConfig` | 17 | REBIRTH_MULTIPLIER=1.2, MIN_PICKAXE_TIER=5, getMultiplier(count) → 1.2^count |

### Remote Events (`game.ReplicatedStorage.Events`)
| Event | Type | Direction |
|-------|------|-----------|
| `MineBlock` | RemoteEvent | Client → Server (pickaxe hit) |
| `BlockDamaged` | RemoteEvent | Server → Client (damage feedback) |
| `BlockDestroyed` | RemoteEvent | Server → Client (block break) |
| `SellOre` | RemoteEvent | Client → Server |
| `BuyUpgrade` | RemoteEvent | Client → Server |
| `CurrencyUpdated` | RemoteEvent | Server → Client (HUD update) |
| `SpinGacha` | RemoteEvent | Client → Server |
| `GachaResult` | RemoteEvent | Server → Client |
| `PlaceBrainrot` | RemoteEvent | Client → Server |
| `PickUpBrainrot` | RemoteEvent | Client → Server |
| `ActivateSquare` | RemoteEvent | Client → Server |
| `DeactivateSquare` | RemoteEvent | Client → Server |
| `CollectPending` | RemoteEvent | Client → Server |
| `BrainrotUpdate` | RemoteEvent | Server → Client |
| `SquareUpdate` | RemoteEvent | Server → Client |
| `RequestPlacementUI` | RemoteEvent | Server → Client |
| `SellBrainrot` | RemoteEvent | Client → Server |
| `RequestRebirth` | RemoteEvent | Client → Server |
| `RebirthResult` | RemoteEvent | Server → Client (success, newRebirthCount, newMultiplier) |
| `GetPlayerData` | RemoteFunction | Client → Server |
| `AdminCommand` | RemoteFunction | Client → Server |

### Client Scripts (`game.StarterPlayer.StarterPlayerScripts`)
| Script | Lines | Purpose |
|--------|-------|---------|
| `MiningClient` | 177 | Tool-based mining input, sends MineBlock events |
| `ShopClient` | 831 | Shop UI (sell ore, buy upgrades, upgrade preview) |
| `GachaClient` | 534 | Gacha pull UI and animations |
| `BrainrotManagerClient` | 529 | Square placement UI, brainrot carry/place/pickup |
| `CurrencyHudClient` | 270 | Currency display HUD + rebirth count/multiplier display + hold-to-confirm rebirth button |
| `AdminClient` | 288 | Admin panel UI |

### GUI (`game.StarterGui`)
| ScreenGui | Used By |
|-----------|---------|
| `ShopGui` | ShopClient |
| `GachaGui` | GachaClient |
| `BrainrotManagerGui` | BrainrotManagerClient |
| `CurrencyHud` | CurrencyHudClient |
| `AdminGui` | AdminClient |

### Workspace (Runtime)
| Instance | Type | Details |
|----------|------|---------|
| `PlayerBases/` | Folder | Cloned bases at runtime (empty at edit time) |
| `DeployedBrainrots/` | Folder | Active brainrot clones at runtime |
| `Shop` | Model | 196 descendants, contains ShopKeeper |
| `GachaMachine` | Model | 89 descendants |
| `Terrain/` | Folder | 2 children |

### Key Spatial Constants
- **Pit origin**: `(0, 2.5, -100)` — top-left corner
- **Pit size**: 100x100 studs (20x20 blocks x 5 stud BLOCK_SIZE)
- **Pit center**: `(50, 2.5, -50)`
- **Base template front faces -Z** (collector squares toward pit, stairs/backyard on +Z back)
- **BASE_SLOTS** (in BrainrotMiningServer lines 46-62):
  - South (rot 0°): `(25, 3, 40)`, `(75, 3, 40)`
  - North (rot 180°): `(25, 3, -140)`, `(75, 3, -140)`
  - West (rot 90°): `(-40, 3, -25)`, `(-40, 3, -75)`
  - East (rot -90°): `(140, 3, -25)`, `(140, 3, -75)`

---

## Architecture & Conventions

### Roblox Studio MCP Workflow
- **All scripts live in Roblox Studio**, not on the filesystem. Use the MCP tools to read/write them.
- This repo is for documentation, design, and Claude context — NOT a Rojo/filesystem sync project.
- Always use `get_script_source` before editing a script to see current state.
- Use `edit_script_lines` for surgical edits; `set_script_source` for full rewrites.
- Use `start_playtest` / `get_playtest_output` / `stop_playtest` to test changes.

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

---

## Development Log

### 2026-02-25: Daily Spin System (Issue #23)

#### Work Completed
1. **Overhauled SpinConfig** (`game.ReplicatedStorage.Modules.SpinConfig`)
   - Changed from 1 free spin / 24h to 5 spins / day regenerating every 4h 48m (17280s)
   - `MAX_DAILY_SPINS = 5`, `REGEN_INTERVAL = 17280`, `NEW_PLAYER_BONUS_SPINS = 3`
   - Removed `BUY_SPIN_COSTS` entirely — no purchasing
   - Improved rewards: 500/1000/2500/5000 coins, 10 coal, 5 gold, 2 diamonds, gacha ticket (8 slots)

2. **Rewrote SpinServer** (`game.ServerScriptService.SpinServer`)
   - `regenerateSpins(data)` — calculates spins regenerated since last checkpoint, caps at MAX
   - New player detection: `freeSpinTimestamp == 0` → grants 3 bonus spins
   - Going from full→not-full resets regen timer to `now`
   - BuySpins handler replaced with no-op warning
   - Added per-player debounce
   - PlayerAdded hook to regenerate spins on join

3. **Updated SpinClient** (`game.StarterPlayer.StarterPlayerScripts.SpinClient`)
   - Displays "Spins: X/5" format instead of "Spins: X"
   - Shows "All spins ready!" when at max, "Next spin: Xh Xm" otherwise
   - Init mirrors server regen logic for accurate display
   - `SpinWheelResult` handler updated for new signature (added `maxSpins` param)

4. **Updated ShopServer** (`game.ServerScriptService.ShopServer`)
   - Added `freeSpinTimestamp` and `extraSpins` to `GetPlayerData` response

5. **Updated ButtonHandlers** (`game.StarterGui.MenusGUI.Scripts.ButtonHandlers`)
   - All buy-spin handlers now show "Coming Soon!" placeholder instead of firing BuySpins

#### Design Decisions
- **Regen model**: `extraSpins` = current available count, `freeSpinTimestamp` = last regen checkpoint. Elapsed intervals added as spins, timestamp advanced by consumed intervals (preserves partial progress).
- **New player bonus**: Detected by `freeSpinTimestamp == 0` (default), grants 3 spins immediately.
- **No purchasing**: BuySpins event still exists (to avoid breaking UI references) but server handler is a no-op.
- **Backward compatible**: Reuses existing `freeSpinTimestamp` and `extraSpins` data fields — no PlayerDataManager schema changes needed.

### 2026-02-25: Fix Base Spawning (Issue #31)

#### Bugs Found & Fixed
1. **Syntax error (showstopper)**: Stray `end` on line 750 of `BrainrotMiningServer` caused `Expected <eof>, got 'end'` parse error. The entire script failed to load — `PlayerAdded` never registered, so no player ever got a base.
   - **Fix**: Removed the stray `end` on line 750 (was left over from a previous refactor of `startSquareMiningLoop`).

2. **Slot counter never recycled**: `nextSlot` was a monotonically increasing counter (0, 1, 2, ...). When players left, `playerSlots[userId]` was cleared but `nextSlot` was never decremented. After 8 cumulative joins (even if all players left), all new players would be kicked with "Server is full!".
   - **Fix**: Replaced `nextSlot` counter with `findAvailableSlot()` scan that iterates `0..MAX_PLAYERS-1` and checks `playerSlots` for the first unused index. Freed slots are now properly recycled.

#### Files Changed (via MCP)
- `game.ServerScriptService.BrainrotMiningServer` — removed stray `end`, replaced slot assignment logic

### 2026-02-23: Rebirth System Implemented

#### Work Completed
1. **Created `RebirthConfig` module** (`game.ReplicatedStorage.Modules.RebirthConfig`)
   - `REBIRTH_MULTIPLIER = 1.2` (stacks multiplicatively: 1.2^count)
   - `MIN_PICKAXE_TIER = 5` (must max pickaxe to rebirth)
   - `getMultiplier(count)` helper function

2. **Updated `PlayerDataManager`**
   - Added `pickaxeTier = 0` to DEFAULT_DATA and saveData
   - Added `performRebirth(player)` — increments rebirths, resets currency/ore/pickaxe/upgrades/squares, keeps ownedBrainrots

3. **Updated `ShopServer`**
   - Added rebirth multiplier to SellOre: `math.floor(baseValue * 1.2^rebirths)`
   - Added `"pickaxe"` upgrade type to BuyUpgrade handler (reads cost from PitConfig.PICKAXE_TIERS)
   - Added `pickaxeTier` to GetPlayerData response

4. **Created `RebirthServer`** (`game.ServerScriptService.RebirthServer`)
   - Validates pickaxeTier >= 5 gate
   - Fires `RebirthCleanup` BindableEvent to BrainrotMiningServer
   - Calls `performRebirth()`, notifies client with `RebirthResult`
   - Debounce per player, immediate save after rebirth

5. **Updated `BrainrotMiningServer`**
   - Added `RebirthConfig` require
   - Applied rebirth multiplier to mining loop ore value (line ~530)
   - Added `RebirthCleanup` BindableEvent handler: stops mining loops, destroys all clones (pit/square/carried), clears target blocks, reinitializes square states on existing base

6. **Updated `CurrencyHudClient`**
   - Rebirth info frame showing "R3 | 1.73x income" (visible when rebirths > 0)
   - REBIRTH button with hold-to-confirm (2 seconds) — visible when pickaxeTier >= 5
   - Progress bar animation during hold
   - Celebration flash on successful rebirth
   - Polls pickaxeTier every 5s to show/hide button

7. **Created Remote Events & BindableEvent**
   - `RequestRebirth` (RemoteEvent, client → server)
   - `RebirthResult` (RemoteEvent, server → client)
   - `RebirthCleanup` (BindableEvent in ServerStorage, server-internal)

#### Design Decisions
- **What resets:** currency, ore, pickaxe tier, shaft/head levels, square assignments
- **What stays:** ALL owned brainrots, rebirth count
- **Multiplier applies to:** ore sell value (ShopServer) + brainrot mining income (BrainrotMiningServer)
- **Base stays intact** during rebirth — only data and deployed clones are cleared
- Rebirth shop/additional upgrades deferred to future session

### 2026-02-23: Base Spawning Fixed

#### Work Completed
1. **Fixed base spawning around the pit**
   - Replaced old `BASE_POSITIONS` (hardcoded Vector3 offsets) with `BASE_SLOTS` (position + rotation)
   - 2 bases per side of the pit, all facing inward (8 total)
   - Fixed critical bug: old code only moved root Part, not child parts (stairs, squares, pillars)
   - New code uses CFrame rotation to move AND rotate all descendant BaseParts

2. **Fixed typos**
   - Renamed `ColectorSquare_3` → `CollectorSquare_3` (in ServerStorage and Workspace templates)
   - Renamed `ColectorSquare_4` → `CollectorSquare_4` (in ServerStorage and Workspace templates)
   - Fixed `"ColectorSquare_4"` → `"CollectorSquare_4"` in BrainrotConfig.SQUARE_NAMES

3. **Cleanup**
   - Deleted stray `PlayerBaseTemplate` from Workspace (should only exist in ServerStorage)
   - Removed stray `end` on line 1123 causing syntax error

### 2025-02-23: Player Base System Overhaul (Previous Session)

#### Work Completed
1. **Fixed 8-slot base spawning system**
   - Captured 8 fixed spawn positions from placeholder bases in workspace
   - Replaced dynamic offset spawning with fixed position array
   - Added 8-player limit (9th+ player gets kicked)

2. **Template organization**
   - Moved `PlayerBaseTemplateNew` from workspace → `ServerStorage.PlayerBaseTemplate`

3. **BrainrotMiningServer updates**
   - Added BASE_POSITIONS array, MAX_PLAYERS = 8
   - Updated setupPlayerBase(), added PlayerDataManager.initPlayer() call
   - Moved auto-save loop and BindToClose from PlayerDataManager to BrainrotMiningServer

4. **PlayerDataManager fixes**
   - Wrapped DataStore initialization in pcall
   - Removed auto-save loop and event connections (modules should only export functions)
   - Module now only exports: initPlayer, getData, savePlayer, removePlayer, removeOwnedBrainrot

5. **Cleanup**
   - Deleted all 8 placeholder bases (PlayerBaseTemplate1-8) from workspace
   - Removed duplicate base clone code
   - Fixed syntax errors (extra `end` statements)
