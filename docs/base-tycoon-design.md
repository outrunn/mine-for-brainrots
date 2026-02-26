# Base Tycoon System Design

**Date:** 2026-02-25
**Status:** Design Phase — Ready for Modeling in Studio

---

## Overview

The player base transforms from an empty concrete slab into a mining HQ through 30 stepping pads purchased in order. Each pad adds a visible structure or functional upgrade. The tycoon persists through rebirths — permanent progress that makes each cycle feel stronger.

**Key rule:** Dynamite is only unlocked after the second floor is built (Pad 11-12).

---

## The Base Story Arc

```
START:  Empty concrete slab, 4 pillars, lonely collector square
  |
SHACK:  Walls up, floor tiled, basic lighting -- scrappy mining hut
  |
WORKSHOP:  Second floor, dynamite bench, chimney puffing smoke
  |
FACTORY:  Portals glowing, jetpack pad on roof, conveyor humming
  |
HQ:  Nuclear facility, deep portals, balcony overlooking pit
  |
PENTHOUSE:  Gold trim, trophy cases, hot tub, prestige crown
```

Other players walking by should see your base and know exactly how far you are.

---

## Floor Plan (Top-Down)

The base is 49x60 studs. Front faces -Z (toward pit).

```
--------------- FRONT (PIT SIDE, -Z) ---------------
+---------------------------------------------------+
|                                                   |
|   [CS1]  [CS2]  [CS3]  [CS4]  [CS5]  [CS6]      |  Collector Squares
|   [CS7]  [CS8]                                    |  (2 rows of 4, or custom layout)
|                                                   |
| +-Portal-+        MAIN FLOOR         +-Portal-+  |
| | Frame  |    +--------------+        | Frame  |  |
| |  (L5)  |    |  ORE BIN /   |        | (L10)  |  |
| +--------+    |  CONVEYOR    |        +--------+  |
|               +--------------+                    |
|    DYNAMITE                          BRAINROT     |
|    CHUTE v              UPGRADE STATION           |
|   (drops from                                     |
|    2nd floor)     [BUTTON PATH WINDS HERE]        |
|                                                   |
|   +-Portal-+                        +-Portal-+   |
|   | (L15)  |        STAIRS ^        | (L18)  |   |
|   +--------+        ########        +--------+   |
|                     ########                      |
|                     ########                      |
+---------------------------------------------------+
--------------- BACK (+Z) --------------------------

SECOND FLOOR (above back half):
+-------------------------+
| DYNAMITE    |  STORAGE   |
| WORKBENCH   |  CRATES    |
|  * Fuse     |            |
|  * Powder   |  BALCONY > | (extends over pit)
|             |  ----------|
|   CHIMNEY ^ |            |
+-------------------------+

ROOF (above second floor):
+-------------------------+
|                         |
|    JETPACK PAD          |
|                         |
|         TELESCOPE       |
+-------------------------+

PENTHOUSE (on top of roof):
+-------------------------+
|  TROPHY    |   HOT TUB  |
|  CASES     |            |
|            |            |
|  JUKEBOX   |  GOLD TRIM |
+-------------------------+
```

---

## Button Path

Buttons snake through the base in purchase order. Each button only appears after the previous is bought. The path physically guides the player through the space:

```
START > [1] [2] [3] around ground floor perimeter
         |
        [4] [5] [6] [7] through center
         |
        [8] [9] [10] > up STAIRS to second floor
         |
        [11] [12] [13] [14] across dynamite area
         |
        [15] [16] [17] > up ladder to ROOF
         |
        [18] [19] [20] [21] roof pads
         |
        [22] [23] [24] > PENTHOUSE stairs
         |
        [25] [26] [27] [28] [29] [30] penthouse
```

The first button spawns at the front entrance. Player walks in, buys it, next one appears a few studs further in. This creates a natural tour of the base as it builds.

---

## Complete Pad Progression

### PHASE 1: Ground Floor (R0+) -- "Building the Shack"

All cosmetic + one big QoL (conveyor). Cheap, fast, lots of visual payoff. The player should buy one every few minutes during the R0 to R1 grind.

| # | Name | Cost | Type | What Appears |
|---|------|------|------|-------------|
| 1 | **Front Fence** | 100 | Cosmetic | Low fence along pit side. Defines the base boundary. |
| 2 | **Floor Tiles** | 200 | Cosmetic | Concrete slab becomes checkered tile floor. Instantly nicer. |
| 3 | **Left Wall** | 350 | Cosmetic | Full wall on left side. Starting to feel enclosed. |
| 4 | **Right Wall** | 500 | Cosmetic | Right wall. Now it's a U-shape. |
| 5 | **Lanterns** | 750 | Cosmetic | 4 hanging lanterns on walls. Warm glow at night. |
| 6 | **Back Wall + Doorway** | 1,200 | Cosmetic | Closes the box. Proper doorway with frame. It's a building now! |
| 7 | **Ore Bin** | 2,000 | Functional | Storage bin near collector squares. Visual setup for conveyor. |
| 8 | **Furniture** | 3,000 | Cosmetic | Workbench, crate stack, barrel, wall shelf. Looks lived-in. |
| 9 | **Windows** | 4,500 | Cosmetic | Glass panes in walls. Light streams in. Can see the pit from inside! |
| 10 | **Ore Conveyor** | 8,000 | **Functional** | Belt from collector squares to ore bin. **Auto-sells ore every 30s.** |

**Phase 1 total: ~20,600**

**Pacing:** Player buys these during the R0 grind (~55 min). About 1 pad every 5 min.

**End state:** Enclosed ground floor with lighting, furniture, windows, and auto-sell conveyor.

---

### PHASE 2: Second Floor + Dynamite (R5+) -- "The Workshop"

Dynamite system starts here. Portal and jetpack access. This is where the base becomes a real operation.

| # | Name | Cost | Type | What Appears |
|---|------|------|------|-------------|
| 11 | **Second Floor Platform** | 12,000 | **Structural** | Floor platform above back half of base, connected to existing stairs. Opens up vertical space. |
| 12 | **Dynamite Workbench** | 18,000 | **Functional** | Workbench on 2nd floor. **Produces 1 dynamite/60s, stock 1.** Anvil, tools, sparks particle effect. |
| 13 | **Chimney** | 22,000 | Cosmetic | Brick chimney on roof. Puffs smoke when dynamite is crafting. Other players can see it! |
| 14 | **Dynamite Storage I** | 28,000 | **Functional** | Crate rack on 2nd floor. **Stock capacity -> 5.** Dynamite sticks visible in crates. |
| 15 | **Blast Powder I** | 35,000 | **Functional** | Powder barrel on workbench. **Radius: 3x3x3 -> 5x5x3.** Bigger explosions! |
| 16 | **Fuse Timer I** | 42,000 | **Functional** | Clock mechanism on workbench. **Production: 60s -> 45s.** Gears spin visually. |
| 17 | **Layer 5 Portal** | 50,000 | **Functional** | Portal frame on ground floor (left alcove). **TP to Coal zone.** Glowing blue swirl. |

**Phase 2 total: ~207,000**

**Pacing:** Player buys during R5-R8 (~3-4 hours). Bigger gaps, but each pad is impactful.

**End state:** Two-story workshop with active dynamite production, chimney smoke, first portal.

---

### PHASE 3: Operations Center (R10+) -- "The Factory"

The base becomes a serious mining facility. Multiple portals, jetpack, nuclear path begins. Phase 3 tycoon unlocks at R10.

| # | Name | Cost | Type | What Appears |
|---|------|------|------|-------------|
| 18 | **Second Floor Walls** | 55,000 | Cosmetic | Encloses 2nd floor. Windows overlook the pit. Railings. |
| 19 | **Jetpack Pad** | 70,000 | **Functional** | Platform on roof. **20s flight, 60s recharge.** Launch flame effect! |
| 20 | **Layer 10 Portal** | 90,000 | **Functional** | Portal frame (right alcove). **TP to Gold/Redstone zone.** Orange swirl. |
| 21 | **Fuse Timer II** | 110,000 | **Functional** | Upgraded clock. **Production: 45s -> 30s.** Faster gear animation. |
| 22 | **Blast Powder II** | 130,000 | **Functional** | Large barrel replaces small. **Radius: 5x5x3 -> 5x5x5.** Full cube blast! |
| 23 | **Layer 15 Portal** | 160,000 | **Functional** | Portal frame (left back). **TP to Diamond zone.** Purple swirl. |
| 24 | **Balcony** | 200,000 | **Cosmetic+** | Extends from 2nd floor over the pit. Railing, lanterns. Amazing view. Can mine from balcony edge! |

**Phase 3 total: ~815,000**

**Pacing:** During R10-R14 (~6 hours). Mix of portals and dynamite upgrades.

**End state:** Multi-portal factory with jetpack, huge dynamite, balcony overlooking the pit.

---

### PHASE 4: Elite HQ (R15+) -- "The Penthouse"

The flex. Nuclear dynamite, turbo jetpack, and the penthouse that everyone wants. Phase 4 tycoon unlocks at R15.

| # | Name | Cost | Type | What Appears |
|---|------|------|------|-------------|
| 25 | **Jetpack Upgrade** | 250,000 | **Functional** | Pad upgrade. **Duration: 20s -> 45s.** Bigger flame, longer trails. |
| 26 | **Nuclear Fuse** | 350,000 | **Functional** | Replaces workbench clock with reactor core. **Rate: 30s -> 15s, 2x blast dmg.** Green glow, radiation particles. The chimney now glows green. |
| 27 | **Layer 18 Portal** | 500,000 | **Functional** | Portal frame (right back). **TP to Deepest zone.** Red/black swirl. Intimidating. |
| 28 | **Jetpack Turbo** | 650,000 | **Functional** | Final pad upgrade. **Duration: 45s -> 90s.** Golden flame effect! |
| 29 | **Dynamite Mega Storage** | 800,000 | **Functional** | Full storage wall. **Stock -> 20.** Visible dynamite stacks everywhere. Slightly dangerous looking. |
| 30 | **Penthouse** | 1,200,000 | **Cosmetic** | Full top floor: gold-trim walls, trophy cases (display rarest brainrots), jukebox, hot tub, neon "MINE BOSS" sign visible from pit. THE flex. |

**Phase 4 total: ~3,750,000**

**Pacing:** During R15-R20 (~8 hours). Big purchases spaced across endgame.

**End state:** Nuclear-powered mining HQ with penthouse, every portal, turbo jetpack.

**Grand total all phases: ~4,793,000**

---

## Visual Design Notes

### Portal Color Coding

Each portal should have a distinct color matching its zone:

| Portal | Color | Zone |
|--------|-------|------|
| Layer 5 | **Blue** | Coal (dark underground) |
| Layer 10 | **Orange** | Gold/Redstone (warm metals) |
| Layer 15 | **Purple** | Diamond (precious, deep) |
| Layer 18 | **Red/Black** | Deepest (dangerous, lava-adjacent) |

### Dynamite Visual Progression

The workbench should visibly upgrade as pads are bought:

1. **Base (Pad 12):** Simple wooden bench, hand tools, single fuse
2. **+Blast Powder (Pad 15):** Barrel of powder appears, bench gets bigger
3. **+Fuse Timer (Pad 16):** Clock/gear mechanism bolted onto bench
4. **+Nuclear Fuse (Pad 26):** Entire bench replaced with reactor containment unit. Green glow. Hazard stripes on floor. Chimney shifts from gray smoke to green glow

### Base Lighting Progression

| Phase | Lighting |
|-------|---------|
| Start | None (dark slab) |
| Pad 5 (Lanterns) | Warm yellow glow |
| 2nd floor | Workshop lighting (brighter, industrial) |
| Portals | Colored glow bleeds from portal frames |
| Nuclear Fuse | Green ambient glow on 2nd floor |
| Penthouse | Neon signs, gold accent lighting |

### "Other Players See This" Moments

These pads are specifically designed to be visible from the pit so other players notice:

- **Chimney (Pad 13)** -- smoke/glow visible from anywhere
- **Balcony (Pad 24)** -- player standing on balcony overlooking pit
- **Jetpack (Pad 19)** -- launch flame visible when taking off
- **Penthouse neon sign (Pad 30)** -- "MINE BOSS" visible from the pit
- **Portal swirls** -- colored glow visible through windows

### Locked Collector Square Visuals

The 7 locked squares should look distinct from the 1 active one:

- **Active:** Bright, glowing border, particle effect (ready to deploy)
- **Locked:** Dark/gray, chain overlay or padlock icon, "Unlock at R2" floating text
- **Newly unlocked:** Brief golden flash + chain-break particle effect when earned

---

## Optional Extras

Additional pads that could slot in or replace existing ones:

| Idea | Type | What It Does |
|------|------|-------------|
| **Telescope** | Cosmetic/Fun | On roof. Zoom camera into pit. See what layer you'll portal to. |
| **Trampoline** | Fun | In backyard. Launches player high -- can land in pit without jetpack. |
| **Lucky Totem** | Functional | Small totem pole. +5% ore value on all income. Subtle but stacks with rebirth. |
| **Brainrot Showcase** | Cosmetic | Glass case on ground floor displaying your rarest deployed brainrot. Rotates slowly. |
| **Slide** | Fun | From roof to ground floor. Fast, silly, players love it. |
| **Garden** | Cosmetic | Backyard area with flowers/crystals that grow based on your rebirth count. |
| **Ore Display** | Cosmetic | Wall-mounted cases showing one of each ore type you've mined. Fills in over time. |
| **Smoke Machine** | Cosmetic | Floor fog on ground floor. Industrial atmosphere. |
| **Name Sign** | Cosmetic | Sign above door with player's username. Gold-plated at R20. |

---

## Tycoon Config Reference

```lua
-- TycoonConfig module
local TycoonConfig = {}

TycoonConfig.PHASE_GATES = {
    [1] = 0,   -- Phase 1: pads 1-10, available from start
    [2] = 5,   -- Phase 2: pads 11-17, requires R5
    [3] = 10,  -- Phase 3: pads 18-24, requires R10
    [4] = 15,  -- Phase 4: pads 25-30, requires R15
}

TycoonConfig.PADS = {
    -- Phase 1: Ground Floor
    [1]  = { name = "Front Fence",           cost = 100,     phase = 1, type = "cosmetic" },
    [2]  = { name = "Floor Tiles",           cost = 200,     phase = 1, type = "cosmetic" },
    [3]  = { name = "Left Wall",             cost = 350,     phase = 1, type = "cosmetic" },
    [4]  = { name = "Right Wall",            cost = 500,     phase = 1, type = "cosmetic" },
    [5]  = { name = "Lanterns",              cost = 750,     phase = 1, type = "cosmetic" },
    [6]  = { name = "Back Wall + Doorway",   cost = 1200,    phase = 1, type = "cosmetic" },
    [7]  = { name = "Ore Bin",               cost = 2000,    phase = 1, type = "functional" },
    [8]  = { name = "Furniture",             cost = 3000,    phase = 1, type = "cosmetic" },
    [9]  = { name = "Windows",               cost = 4500,    phase = 1, type = "cosmetic" },
    [10] = { name = "Ore Conveyor",          cost = 8000,    phase = 1, type = "functional",
             effect = { autoSellInterval = 30 } },

    -- Phase 2: Second Floor + Dynamite
    [11] = { name = "Second Floor Platform", cost = 12000,   phase = 2, type = "structural" },
    [12] = { name = "Dynamite Workbench",    cost = 18000,   phase = 2, type = "functional",
             effect = { dynamiteRate = 60, dynamiteStock = 1, blastRadius = {3,3,3}, blastDamage = 10 } },
    [13] = { name = "Chimney",               cost = 22000,   phase = 2, type = "cosmetic" },
    [14] = { name = "Dynamite Storage I",    cost = 28000,   phase = 2, type = "functional",
             effect = { dynamiteStock = 5 } },
    [15] = { name = "Blast Powder I",        cost = 35000,   phase = 2, type = "functional",
             effect = { blastRadius = {5,5,3} } },
    [16] = { name = "Fuse Timer I",          cost = 42000,   phase = 2, type = "functional",
             effect = { dynamiteRate = 45 } },
    [17] = { name = "Layer 5 Portal",        cost = 50000,   phase = 2, type = "functional",
             effect = { portalLayer = 5 } },

    -- Phase 3: Operations Center
    [18] = { name = "Second Floor Walls",    cost = 55000,   phase = 3, type = "cosmetic" },
    [19] = { name = "Jetpack Pad",           cost = 70000,   phase = 3, type = "functional",
             effect = { jetpackDuration = 20, jetpackRecharge = 60 } },
    [20] = { name = "Layer 10 Portal",       cost = 90000,   phase = 3, type = "functional",
             effect = { portalLayer = 10 } },
    [21] = { name = "Fuse Timer II",         cost = 110000,  phase = 3, type = "functional",
             effect = { dynamiteRate = 30 } },
    [22] = { name = "Blast Powder II",       cost = 130000,  phase = 3, type = "functional",
             effect = { blastRadius = {5,5,5} } },
    [23] = { name = "Layer 15 Portal",       cost = 160000,  phase = 3, type = "functional",
             effect = { portalLayer = 15 } },
    [24] = { name = "Balcony",               cost = 200000,  phase = 3, type = "cosmetic" },

    -- Phase 4: Elite HQ
    [25] = { name = "Jetpack Upgrade",       cost = 250000,  phase = 4, type = "functional",
             effect = { jetpackDuration = 45, jetpackRecharge = 45 } },
    [26] = { name = "Nuclear Fuse",          cost = 350000,  phase = 4, type = "functional",
             effect = { dynamiteRate = 15, blastDamage = 20 } },
    [27] = { name = "Layer 18 Portal",       cost = 500000,  phase = 4, type = "functional",
             effect = { portalLayer = 18 } },
    [28] = { name = "Jetpack Turbo",         cost = 650000,  phase = 4, type = "functional",
             effect = { jetpackDuration = 90, jetpackRecharge = 30 } },
    [29] = { name = "Dynamite Mega Storage", cost = 800000,  phase = 4, type = "functional",
             effect = { dynamiteStock = 20 } },
    [30] = { name = "Penthouse",             cost = 1200000, phase = 4, type = "cosmetic" },
}

return TycoonConfig
```
