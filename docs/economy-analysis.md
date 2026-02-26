# Economy & Progression Analysis

**Goal:** 1-2 weeks casual play (~2 hrs/day, 14-28 total hours) to reach Rebirth 20
**Date:** 2026-02-25

---

## 1. Current Config Summary

### Ore Values (per block mined)
| Block | Base Value | Durability |
|-------|-----------|------------|
| Grass | 1 | 2 |
| Dirt | 1 | 3 |
| Stone | 1 | 5 |
| Coal | 5 | 6 |
| Redstone | 15 | 8 |
| Gold | 40 | 10 |
| Diamond | 100 | 15 |

### Pickaxe Tiers
| Tier | Name | Cost | Cumulative | Max Layer | MultiMine |
|------|------|------|-----------|-----------|-----------|
| 0 | Wooden | 0 | 0 | 4 | 1 |
| 1 | Stone | 200 | 200 | 6 | 1 |
| 2 | Iron | 1,000 | 1,200 | 10 | 2 |
| 3 | Gold | 5,000 | 6,200 | 14 | 3 |
| 4 | Diamond | 25,000 | 31,200 | 17 | 4 |
| 5 | Obsidian | 100,000 | 131,200 | 20 | 6 |

### Shaft Upgrades (Speed = 1 + level * 0.25)
| Level | Cost | Cumulative | Speed |
|-------|------|-----------|-------|
| 1 | 50 | 50 | 1.25 |
| 2 | 100 | 150 | 1.50 |
| 3 | 200 | 350 | 1.75 |
| 4 | 400 | 750 | 2.00 |
| 5 | 800 | 1,550 | 2.25 |
| 6 | 1,600 | 3,150 | 2.50 |
| 7 | 3,200 | 6,350 | 2.75 |
| 8 | 6,400 | 12,750 | 3.00 |
| 9 | 12,800 | 25,550 | 3.25 |
| 10 | 25,600 | 51,150 | 3.50 |

### Head Upgrades (Power = 1 + level)
| Level | Cost | Cumulative | Power |
|-------|------|-----------|-------|
| 1 | 75 | 75 | 2 |
| 2 | 150 | 225 | 3 |
| 3 | 300 | 525 | 4 |
| 4 | 600 | 1,125 | 5 |
| 5 | 1,200 | 2,325 | 6 |
| 6 | 2,400 | 4,725 | 7 |
| 7 | 4,800 | 9,525 | 8 |
| 8 | 9,600 | 19,125 | 9 |
| 9 | 19,200 | 38,325 | 10 |
| 10 | 38,400 | 76,725 | 11 |

### Full Rebirth Cycle Cost
| Category | Total Cost |
|----------|-----------|
| Pickaxe T0→T5 | 131,200 |
| Shaft 0→10 | 51,150 |
| Head 0→10 | 76,725 |
| **Total (no gacha)** | **259,075** |
| Practical (shaft/head ~7-8 + T5) | ~165,000 |

### Gacha Costs
| Tier | Cost | Common | Uncommon | Rare | Epic | Legendary | Mythic |
|------|------|--------|----------|------|------|-----------|--------|
| Basic | 500 | 60% | 25% | 10% | 4% | 1% | 0% |
| Premium | 2,500 | 25% | 35% | 25% | 10% | 4% | 1% |
| Ultra | 10,000 | 5% | 15% | 30% | 30% | 15% | 5% |

### Brainrot NPC Stats (level 1)
| Rarity | Mine Speed (s/hit) | Pickaxe Tier | Sell Price |
|--------|-------------------|-------------|------------|
| Common | 5.0 | 0 | 50 |
| Uncommon | 4.0 | 1 | 150 |
| Rare | 3.0 | 2 | 400 |
| Epic | 2.0 | 3 | 1,000 |
| Legendary | 1.2 | 4 | 3,000 |
| Mythic | 0.8 | 5 | 8,000 |

### Spin Wheel (5 spins/day, 3 bonus for new players)
| Slot | Weight | Type |
|------|--------|------|
| 2,000 Coins | 25% | Currency |
| 5,000 Coins | 20% | Currency |
| 10,000 Coins | 15% | Currency |
| 25,000 Coins | 10% | Currency |
| Rare Brainrot | 15% | Brainrot |
| Epic Brainrot | 10% | Brainrot |
| Mythic Brainrot | 5% | Brainrot |

**Expected value per spin:** 5,500 coins (currency outcomes only, brainrots = 0 coins)
**Daily spin EV:** 27,500 coins + ~1.5 brainrots

### Rebirth Multiplier (1.2^count, applies to ore selling + NPC income)
| Rebirth | Multiplier | Effective per-block (player) |
|---------|-----------|------------------------------|
| 0 | 1.00x | oreValue * 2.00 |
| 1 | 1.20x | oreValue * 2.20 |
| 2 | 1.44x | oreValue * 2.44 |
| 3 | 1.73x | oreValue * 2.73 |
| 5 | 2.49x | oreValue * 3.49 |
| 7 | 3.58x | oreValue * 4.58 |
| 10 | 6.19x | oreValue * 7.19 |

> **Note:** Player mining gives BOTH immediate currency (flat, no multiplier) AND
> sellable ore (with rebirth multiplier). Effective = oreValue * (1 + rebirthMult).
> NPC mining only gets the multiplied value into pending.

### Playtime Rewards (daily reset)
| Time | Reward |
|------|--------|
| 5 min | 200 Coins |
| 15 min | 500 Coins |
| 50 min | Rare Brainrot |
| 1 hr | 2,000 Coins |
| 2 hr | 1 Free Spin |
| **Daily total** | **2,700 coins + Rare + Spin** |

---

## 2. Layer Ore Value Analysis

Expected value per block (at R0, including sell = oreValue * 2):

| Layer | Zone | durMult | Tier Req | Avg Value/Block | Avg Durability |
|-------|------|---------|----------|----------------|---------------|
| 1-2 | Surface | 1.0 | 0 | 2.0 (grass/dirt) | 2.5 |
| 3 | Early | 1.0 | 0 | 3.4 | 5.2 |
| 4 | Early | 1.0 | 0 | 3.8 | 5.2 |
| 5 | Early | 1.1 | 1 | 6.8 | 6.0 |
| 6 | Early | 1.1 | 1 | 7.6 | 5.9 |
| 7 | Mid | 1.3 | 2 | 12.4 | 7.6 |
| 8 | Mid | 1.3 | 2 | 15.0 | 7.8 |
| 9 | Mid | 1.5 | 2 | 20.0 | 9.3 |
| 10 | Mid | 1.5 | 2 | 24.7 | 10.0 |
| 11 | Mid-Deep | 1.8 | 3 | 34.2 | 12.5 |
| 12 | Mid-Deep | 1.8 | 3 | 40.8 | 13.0 |
| 13 | Mid-Deep | 2.0 | 3 | 48.6 | 15.1 |
| 14 | Mid-Deep | 2.0 | 3 | 56.5 | 15.6 |
| 15 | Deep | 2.5 | 4 | 68.6 | 23.1 |
| 16 | Deep | 2.5 | 4 | 79.6 | 24.6 |
| 17 | Deep | 3.0 | 4 | 92.6 | 30.8 |
| 18 | Deepest | 3.5 | 5 | 106.0 | 39.5 |
| 19 | Deepest | 4.0 | 5 | 117.4 | 46.7 |
| 20 | Deepest | 4.5 | 5 | 128.0 | 53.7 |

---

## 3. Mining Rate Model

### Player Manual Mining

**Formula:**
- Cooldown = 0.5 / speed
- Hits to break = ceil(durability / power)
- Time per batch of M blocks = hits * cooldown (M blocks damaged simultaneously)
- Raw rate = M * valuePerBlock / timePerbatch
- Practical rate = raw * 0.55 (walking, selling, pit resets, finding blocks)

### Estimated Earning Rates (coins/min, at R0, 55% efficiency)

| State | Tier | S/H | Multi | Best Layer | Raw/s | **Practical/min** |
|-------|------|-----|-------|-----------|-------|-------------------|
| Fresh start | 0 | 0/0 | 1 | 3 | 1.1 | **36** |
| First buys | 0 | 2/2 | 1 | 3 | 3.4 | **112** |
| Stone pick | 1 | 3/3 | 1 | 5-6 | 11.8 | **390** |
| Iron pick | 2 | 5/5 | 2 | 9-10 | 52.8 | **1,740** |
| Gold pick | 3 | 6/6 | 3 | 13-14 | 98.5 | **3,250** |
| Diamond pick | 4 | 8/8 | 4 | 16-17 | 185 | **6,100** |
| Obsidian pick | 5 | 10/10 | 6 | 19-20 | 265 | **8,750** |

### NPC Brainrot Mining Rates (coins/min per NPC, at R0)

NPCs deal only 1 damage per hit, so high-durability blocks take many hits.

| Rarity | Speed | Tier | Best Layer | **coins/min** |
|--------|-------|------|-----------|--------------|
| Common | 5.0s | 0 | 3-4 | **4** |
| Uncommon | 4.0s | 1 | 5-6 | **8** |
| Rare | 3.0s | 2 | 9-10 | **18** |
| Epic | 2.0s | 3 | 13-14 | **42** |
| Legendary | 1.2s | 4 | 16-17 | **95** |
| Mythic | 0.8s | 5 | 19-20 | **175** |

> NPCs mine the accessible surface, so rates are lower than theoretical max.
> Walking + block-finding overhead adds ~3s per block cycle.

---

## 4. Hour-by-Hour Progression (Current Economy)

### Day 1, Session 1 (Hours 0-2)

| Time | Event | Balance | Rate |
|------|-------|---------|------|
| 0:00 | **Join game. 3 bonus spins.** EV ~16,500 coins + ~1 brainrot | 16,500 | - |
| 0:01 | Buy T1 (200), T2 (1,000), shaft 1-5 (1,550), head 1-4 (1,125), Basic gacha (500) | 12,125 | - |
| 0:02 | Buy T3 (5,000), shaft 6 (1,600), head 5-6 (3,600) | 1,925 | 3,250/min |
| 0:02-0:10 | Mine at T3 rate. Deploy 2 brainrots (+~50/min passive) | 28,125 | 3,300/min |
| 0:10 | Buy T4 (25,000), shaft 7 (3,200) | ~0 | 6,100/min |
| 0:10-0:25 | Mine at T4 rate | ~91,500 | 6,100/min |
| 0:25 | Buy head 7-8 (14,400), shaft 8 (6,400), T5 (100,000) | wait... |  |
| ~0:28 | **Buy T5 (100,000)** | ~5,000 | 8,750/min |
| ~0:30 | **REBIRTH #1** | 0 | - |
| 0:30-0:33 | Reassign 3-4 brainrots. Mine manually. | ~1,000 | 150/min |
| 0:33-0:45 | Progress T0→T3 (much faster with NPC help) | ~15,000 | 3,300+/min |
| 0:45-0:55 | T4 mining + NPCs | ~65,000 | 6,700/min |
| ~0:57 | **Buy T5, REBIRTH #2** | 0 | - |
| 0:57-1:20 | **Rebirth #3** cycle (faster: more brainrots, 1.44x mult) | | ~25 min |
| 1:20-1:40 | **Rebirth #4** cycle | | ~20 min |
| 1:40-2:00 | **Rebirth #5** begins | | - |

### Estimated Rebirth Pace
| Rebirth | Cumulative Time | Session |
|---------|----------------|---------|
| 1 | ~30 min | Day 1, Session 1 |
| 2 | ~57 min | Day 1, Session 1 |
| 3 | ~1h 20m | Day 1, Session 1 |
| 4 | ~1h 40m | Day 1, Session 1 |
| 5 | ~2h 00m | Day 1, Session 1 |
| 6 | ~2h 15m | Day 1, Session 2 |
| 7 | ~2h 30m | Day 1, Session 2 |
| 8 | ~2h 45m | Day 2 |
| 9 | ~3h 00m | Day 2 |
| **10** | **~3h 15m** | **Day 2** |

### VERDICT: Current economy reaches Rebirth 10 in ~3-4 hours, not 1-2 weeks.

---

## 5. Critical Issues Found

### ISSUE 1: Double-Dip Income (BUG?)
Player mining in `MiningSystem` (line 113) gives **immediate currency** (no multiplier)
AND stores ore in inventory. Selling ore via `ShopServer` gives **additional** currency
(with rebirth multiplier). This effectively **doubles** all player mining income.

**Impact:** All income estimates are 2x what ore values suggest.
**Fix options:**
- A) Remove immediate currency from MiningSystem (ore must be sold)
- B) Remove ore-to-inventory (mining gives currency only, no selling)
- Option A is recommended: makes selling a meaningful game loop.

### ISSUE 2: Bonus Spins Skip Early Game
3 new-player bonus spins give ~16,500 coins EV. This lets players buy T1+T2+T3
pickaxes and several shaft/head upgrades in the first minute. The entire "early game"
(Tier 0-2, first 30 min) is bypassed.

**Impact:** First ~30 min of progression is meaningless.
**Fix:** Reduce to 1 bonus spin, or make spins give smaller amounts.

### ISSUE 3: Multi-Mine Scaling Too Aggressive
| Tier | MultiMine | Effective Throughput |
|------|-----------|---------------------|
| 0-1 | 1 | 1x |
| 2 | 2 | 2x |
| 3 | 3 | 3x |
| 4 | 4 | 4x |
| 5 | 6 | 6x |

Combined with speed/power upgrades, T5 mines blocks ~50-100x faster than T0.
The exponential gap means the last pickaxe tier trivializes all costs.

### ISSUE 4: Pickaxe Cost Curve Too Flat
The cost jumps are: 200, 1000, 5000, 25000, 100000 (~5x each).
But earning rates jump ~3-5x per tier (from better ores + multi-mine).
The player's "time to next tier" stays roughly the same or decreases,
instead of increasing. There's no meaningful slowdown before rebirth.

### ISSUE 5: Rebirth Cycle Too Short
A rebirth requires ~131,200-165,000 coins. At T4 rates (~6,100/min),
that's only ~25 minutes of mining. Each subsequent rebirth is faster
due to multiplier + accumulated brainrots.

### ISSUE 6: NPC Income Negligible
Common/Uncommon brainrots earn 4-8 coins/min. The player earns 3,000+/min
by mid-game. NPCs feel irrelevant until Legendary/Mythic rarity (which are
extremely rare from gacha). This undermines the core loop of "collect brainrots
to automate mining."

### ISSUE 7: Sparse Unlock Cadence
After buying T3 pickaxe (~10 min in), the next meaningful unlock is T4 (~15 min later).
That's a 15-minute gap with nothing new. After T5, there's nothing until rebirth.
The shaft/head upgrades are too cheap to serve as milestones.

### ISSUE 8: Nothing New After Rebirth 1
Rebirth just makes numbers go up faster. There are no new:
- Pickaxe tiers
- Layers/zones
- Brainrot rarities
- Features/mechanics

Rebirths 2-10 are identical loops with bigger numbers.

---

## 6. Redesigned Core Loop

### 6A. The Loop (How It Feels to Play)

```
MINE ─→ SELL ─→ UPGRADE STATS ─→ BUY TYCOON PADS ─→ PULL GACHA
  ↑                                                        │
  │         ┌─────────────────────────────────────────────┘
  │         ↓
  │    DEPLOY BRAINROTS (passive income)
  │         │
  │         ↓
  │    HIT STAT GATE ─→ REBIRTH ─→ PERMANENT REWARD
  │                        │
  └────────────────────────┘  (stats reset, start over STRONGER)
```

**What resets on rebirth:** Shaft level, Head level, currency, ore inventory
**What stays forever:** Pickaxe tier, brainrots, tycoon pads, collector squares,
brainrot income multiplier, dynamite upgrades, portals, jetpack

### 6B. The Key Change: Pickaxes Are Rebirth Rewards

Pickaxes are **NOT purchasable**. You earn them by rebirthing. This makes each
rebirth feel like a transformative power-up, not just a number going up.

The shop only sells: Shaft upgrades, Head upgrades, Gacha pulls, Brainrot upgrades.

### 6C. Design Pillars

1. **Constant micro-unlocks** — Tycoon pads + stat levels fill every gap
2. **Dynamite = burst mining** — Complements steady pickaxe mining with periodic explosions
3. **Portals solve the surface problem** — Skip grass/dirt, go straight to deep ores
4. **Jetpack = quality-of-life** — Fly in pit, mine exposed walls
5. **Tycoon persists through rebirth** — Permanent power that makes you stronger each cycle

---

## 7. Rebirth System (Complete Redesign)

### 7A. What Resets vs What Stays

| Resets on Rebirth | Stays Forever |
|-------------------|---------------|
| Shaft level → 0 | Pickaxe tier (earned from rebirths) |
| Head level → 0 | All owned brainrots |
| Currency → 0 | Tycoon pads purchased |
| Ore inventory → empty | Collector square count |
| | Brainrot income multiplier |
| | Dynamite upgrades, portals, jetpack |

**Key insight:** Stats (shaft/head) are the GRIND. Everything else is PERMANENT PROGRESS.
This means each rebirth cycle is "re-level your stats" but you keep all your tools and toys.

### 7B. Starting State

**Player starts with:**
- Wooden Pickaxe (T0): layers 1-4 only, mine 1 block at a time
- 1 Collector Square active (the other 7 exist on the base but are LOCKED)
- Shaft 0, Head 0
- 0 brainrots, 0 currency

Everything else is earned. The base has 8 physical squares but 7 are
visibly locked (darkened/chained/greyed out) until earned through rebirths.

### 7C. Stat System (Shaft & Head)

Rebirth requires BOTH shaft AND head to reach a specific level.
The required level increases with each rebirth. This is the core pacing lever.

**Cost formula:** `floor(baseCost * 1.8 ^ (level - 1))`
- Both stats use baseCost = 50 (same base, clean mental model)
- 1.8x per level

| Level | Per-Level Cost | Cumulative (one stat) | Both Stats |
|-------|---------------|----------------------|------------|
| 1 | 50 | 50 | 100 |
| 2 | 90 | 140 | 280 |
| 3 | 162 | 302 | 604 |
| 4 | 292 | 594 | 1,188 |
| 5 | 525 | 1,119 | **2,238** |
| 6 | 945 | 2,064 | **4,128** |
| 7 | 1,701 | 3,765 | **7,530** |
| 8 | 3,062 | 6,827 | **13,654** |
| 9 | 5,512 | 12,339 | **24,678** |
| 10 | 9,922 | 22,261 | **44,522** |
| 11 | 17,859 | 40,120 | **80,240** |
| 12 | 32,147 | 72,267 | **144,534** |
| 13 | 57,864 | 130,131 | **260,262** |
| 14 | 104,156 | 234,287 | **468,574** |
| 15 | 187,480 | 421,767 | **843,534** |

**Stat effects (no cap):**
- Shaft: pickaxeSpeed = 1 + level × 0.15 (L5 = 1.75x, L10 = 2.5x, L15 = 3.25x)
- Head: pickaxePower = 1 + level (L5 = 6 dmg, L10 = 11 dmg, L15 = 16 dmg)

**Bulk buy (+1, +5, +10):**
After rebirth, player needs to re-level from 0. Bulk buttons make this fast:
- **+1**: Buy next level (shows cost)
- **+5**: Buy next 5 levels (shows sum)
- **+10**: Buy next 10 levels (shows sum)
- Greyed out if can't afford. No discount — purely convenience.
- Example: After R12 (needs S12/H12), player clicks +10 then +1 twice. 3 clicks, done.

### 7D. The 20 Rebirth Rewards

**Design rules:**
- Player starts with 1 square, earns 7 more (total 8) across 20 rebirths
- 5 pickaxe tiers spread across the journey (T1 early, T5 is the final reward)
- Every single rebirth gives something that changes gameplay, no filler
- "Quick double" gates (same level as previous) create moments of easy wins
- Tycoon phases unlock automatically at certain rebirths (bonus, not the reward)

#### TIER 1: STARTER (R1-R5) — Learning the Loop

| R | Gate | Stat Cost | Reward | Why It Matters |
|---|------|-----------|--------|---------------|
| **1** | S5/H5 | 2,238 | **Stone Pickaxe (T1)** | Layers 5-6 unlock. Coal! Real income starts. |
| **2** | S6/H6 | 4,128 | **+1 Square** (2nd slot) | 2 NPCs. Passive income DOUBLED. |
| **3** | S7/H7 | 7,530 | **+1 Square** (3rd slot) | 3 NPCs. Army is forming. |
| **4** | S8/H8 | 13,654 | **Iron Pickaxe (T2, multi 2)** | Gold ore! Mine 2 blocks per swing! |
| **5** | S8/H8 | 13,654 | **Auto-Collect** | NPCs deposit earnings automatically. No manual pickup. |

> R5 has the SAME gate as R4. Quick win! Player thinks "wait, I can rebirth
> again immediately?" This is the moment they understand the loop is fun.
> Also unlocks **Tycoon Phase 2** (jetpack, portals, enhanced dynamite).

#### TIER 2: BRONZE (R6-R10) — Building Power

| R | Gate | Stat Cost | Reward | Why It Matters |
|---|------|-----------|--------|---------------|
| **6** | S9/H9 | 24,678 | **+1 Square** (4th slot) | 4 NPCs with auto-collect = serious passive income. |
| **7** | S9/H9 | 24,678 | **1.5× Brainrot Income** | All 4 NPCs earn 50% more. Stacks with rarity. |
| **8** | S10/H10 | 44,522 | **Gold Pickaxe (T3)** | Diamond ore access! Layers 11-14. |
| **9** | S10/H10 | 44,522 | **+1 Square** (5th slot) | 5 NPCs mining diamonds. |
| **10** | S11/H11 | 80,240 | **Premium Gacha Unlock** | Way better odds for Rare/Epic brainrots. |

> R10 is a milestone. Player has 5 squares, T3 pickaxe, 1.5x NPC income,
> and now Premium Gacha for better brainrots. They feel POWERFUL.
> Also unlocks **Tycoon Phase 3** (deep portals, advanced dynamite).

#### TIER 3: SILVER (R11-R15) — Going Deep

| R | Gate | Stat Cost | Reward | Why It Matters |
|---|------|-----------|--------|---------------|
| **11** | S11/H11 | 80,240 | **+1 Daily Spin** (6 total) | More daily free rewards. Extra 5,500 coins/day EV. |
| **12** | S12/H12 | 144,534 | **Diamond Pickaxe (T4, multi 3)** | Layers 15-17! 3 blocks per swing! Deep mining. |
| **13** | S12/H12 | 144,534 | **+1 Square** (6th slot) | 6 NPCs. Army is getting serious. |
| **14** | S13/H13 | 260,262 | **2.0× Brainrot Income** | All 6 NPCs earn DOUBLE. Replaces 1.5x. |
| **15** | S13/H13 | 260,262 | **Brainrot Level Cap → 15** | Upgrade brainrots to level 15. NPCs get way faster. |

> R15 milestone. 6 squares, T4 pickaxe, 2x income, level 15 brainrots.
> Also unlocks **Tycoon Phase 4** (nuclear fuse, L18 portal, penthouse).

#### TIER 4: GOLD (R16-R20) — The Endgame

| R | Gate | Stat Cost | Reward | Why It Matters |
|---|------|-----------|--------|---------------|
| **16** | S14/H14 | 468,574 | **Ultra Gacha Unlock** | 30% Epic, 15% Legendary, 5% Mythic. Best pulls. |
| **17** | S14/H14 | 468,574 | **+1 Square** (7th slot) | 7 NPCs. One more to go! |
| **18** | S15/H15 | 843,534 | **2.5× Brainrot Income** | 7 high-level NPCs earning 2.5x. Massive passive. |
| **19** | S15/H15 | 843,534 | **+1 Square** (8th slot — FULL!) | **ALL 8 SQUARES UNLOCKED!** Full NPC deployment. |
| **20** | S15/H15 | 843,534 | **Obsidian Pickaxe (T5, multi 4)** | **THE FINAL REWARD.** Layers 18-20. Full pit access. |

> R20 has the same gate as R18/R19. The player does THREE quick rebirths
> in a row to finish the game. Each one feels incredible: 2.5x income →
> 8th square → Obsidian Pickaxe. A triple finale.

### 7E. Reward Distribution Summary

| Category | Rebirths | Count | Progression |
|----------|----------|-------|-------------|
| **Collector Squares** | R2, R3, R6, R9, R13, R17, R19 | 7 (1→8) | Spread evenly, each is impactful |
| **Pickaxe Tiers** | R1, R4, R8, R12, R20 | 5 (T1→T5) | Transformative moments |
| **Brainrot Income** | R7, R14, R18 | 3 (1.5x→2.0x→2.5x) | Scales with NPC count |
| **Auto-Collect** | R5 | 1 | Major QoL |
| **Gacha Unlocks** | R10, R16 | 2 (Premium, Ultra) | Better brainrots |
| **Daily Spin** | R11 | 1 (+1 spin/day) | Passive daily value |
| **Brainrot Level Cap** | R15 | 1 (10→15) | NPC upgrade depth |

**Tycoon phases (bonus, not counted as rebirth reward):**
| Rebirth | Tycoon Phase |
|---------|-------------|
| 0 | Phase 1: Basic Base (pads 1-10) |
| 5 | Phase 2: Enhanced (pads 11-17: jetpack, portals) |
| 10 | Phase 3: Advanced (pads 18-24: deep portals, big dynamite) |
| 15 | Phase 4: Elite (pads 25-30: nuclear fuse, L18 portal) |

### 7F. Gate Difficulty Curve

The stat gates use "quick doubles" — two rebirths at the same level —
to create pacing variety. Some cycles feel like a grind, then the next
one is a quick win. This emotional rhythm keeps players engaged.

```
Gate Level
   15 ─────────────────────────────────── ●●● R18/R19/R20
   14 ──────────────────────────── ●● R16/R17
   13 ────────────────────── ●● R14/R15
   12 ───────────────── ●● R12/R13
   11 ──────────── ●● R10/R11
   10 ──────── ●● R8/R9
    9 ───── ●● R6/R7
    8 ──── ●● R4/R5
    7 ── ● R3
    6 ─ ● R2
    5 ● R1
   └──────────────────────────────────────→ Rebirth #
```

**Pattern:** Increase by 1 → stay → increase by 1 → stay → ...
Then triple-stay at the end for the grand finale.

### 7G. Bulk Buy Details

| Button | Effect | UI Shows |
|--------|--------|----------|
| **+1** | Buy next level | "Shaft 6 → 7: $1,701" |
| **+5** | Buy next 5 at once | "Shaft 3 → 8: $10,861" |
| **+10** | Buy next 10 at once | "Shaft 0 → 10: $22,261" |
| **MAX** | Buy to rebirth gate | "Shaft 0 → 12: $72,267" (if affordable) |

The **MAX** button is the real QoL hero. After rebirth, player clicks MAX on shaft,
MAX on head, done. Two clicks to reach the gate if they have enough money.
(This only becomes practical in later rebirths when the player's accumulated
tools let them earn fast.)

### 7H. Rebirth Roadmap UI (Always Visible)

```
┌──────────────────────────────────────────────────────────────┐
│  REBIRTH ROADMAP                                You: R6      │
│                                                              │
│  STARTER                                                     │
│  ✓ R1  Stone Pickaxe              ✓ R4  Iron Pickaxe (2x)   │
│  ✓ R2  +1 Mining Slot             ✓ R5  Auto-Collect         │
│  ✓ R3  +1 Mining Slot                                        │
│                                                              │
│  BRONZE                                                      │
│  ✓ R6  +1 Mining Slot            ► R7  1.5x NPC Income      │
│  ○ R8  Gold Pickaxe               ○ R9  +1 Mining Slot      │
│  ○ R10 Premium Gacha                                         │
│                                                              │
│  SILVER                              GOLD                    │
│  ○ R11 +1 Daily Spin               ○ R16 Ultra Gacha        │
│  ○ R12 Diamond Pickaxe (3x)        ○ R17 +1 Mining Slot     │
│  ○ R13 +1 Mining Slot              ○ R18 2.5x NPC Income    │
│  ○ R14 2.0x NPC Income             ○ R19 +1 Mining Slot     │
│  ○ R15 Brainrot Lvl Cap 15         ○ R20 OBSIDIAN PICKAXE   │
│                                                              │
│  NEXT: Shaft 9 + Head 9  ████████████░░░░░░  67%            │
└──────────────────────────────────────────────────────────────┘
```

Player always sees:
1. What they've earned (checkmarks = pride)
2. What's next (highlighted = motivation)
3. What's coming (locked = anticipation)
4. Progress bar toward next gate (urgency)

---

## 8. Tycoon Base & Dynamite System

### 8A. Persistence & Rebirth Interaction

| Category | Resets? | Rationale |
|----------|---------|-----------|
| Tycoon pads | NO | Permanent base progression |
| Dynamite stock | NO | Feels bad to lose stockpile |
| Jetpack/portals | NO | QoL shouldn't regress |
| Cosmetic structures | NO | Visual progress is satisfying |

New tycoon PHASES are gated by rebirth count (see 7C above).

### 8B. Tycoon Stepping Pad Progression

#### Phase 1: Basic Base (Rebirth 0+) — Total: 23,600

| # | Pad Name | Cost | Effect |
|---|----------|------|--------|
| 1 | Front Wall | 150 | Cosmetic |
| 2 | Side Walls | 300 | Cosmetic |
| 3 | Floor Tiles | 400 | Cosmetic |
| 4 | **Dynamite Dispenser** | 750 | 1 dynamite / 60s, stock 1 |
| 5 | Storage Crate I | 1,000 | Stock capacity → 5 |
| 6 | Stairs | 1,500 | Cosmetic + roof access |
| 7 | **Blast Powder I** | 2,500 | Blast radius: 3x3x3 → 5x5x3 |
| 8 | Fuse Timer I | 4,000 | Production: 60s → 45s |
| 9 | Doorway | 5,000 | Cosmetic |
| 10 | **Ore Conveyor** | 8,000 | Auto-sell ore every 30s |

#### Phase 2: Enhanced (Rebirth 5+) — Total: 190,000

| # | Pad Name | Cost | Effect |
|---|----------|------|--------|
| 11 | Second Floor | 10,000 | Cosmetic + more pad space |
| 12 | **Jetpack Pad** | 15,000 | 20s flight, 60s recharge |
| 13 | **Layer 5 Portal** | 20,000 | TP to Coal zone |
| 14 | Fuse Timer II | 25,000 | Production: 45s → 30s |
| 15 | Storage Crate II | 30,000 | Stock capacity → 10 |
| 16 | **Blast Powder II** | 40,000 | Radius: 5x5x3 → 5x5x5 |
| 17 | **Layer 10 Portal** | 50,000 | TP to Gold zone |

#### Phase 3: Advanced (Rebirth 10+) — Total: 890,000

| # | Pad Name | Cost | Effect |
|---|----------|------|--------|
| 18 | Balcony | 60,000 | Cosmetic (pit overlook) |
| 19 | **Jetpack Upgrade** | 80,000 | Duration: 20s → 45s |
| 20 | Fuse Timer III | 100,000 | Production: 30s → 20s |
| 21 | **Layer 15 Portal** | 125,000 | TP to Diamond zone |
| 22 | **Blast Powder III** | 150,000 | Radius: 5x5x5 → 7x7x5 |
| 23 | Mega Storage | 175,000 | Stock capacity → 20 |
| 24 | **Ore Conveyor II** | 200,000 | Auto-sell: 30s → 10s |

#### Phase 4: Elite (Rebirth 15+) — Total: 3,450,000

| # | Pad Name | Cost | Effect |
|---|----------|------|--------|
| 25 | Penthouse Frame | 250,000 | Cosmetic |
| 26 | **Nuclear Fuse** | 350,000 | Rate: 20s → 10s, 2x blast dmg |
| 27 | **Layer 18 Portal** | 500,000 | TP to Deepest zone |
| 28 | **Jetpack Turbo** | 600,000 | Duration: 45s → 90s |
| 29 | Storage Vault | 750,000 | Stock capacity → 50 |
| 30 | **Penthouse Complete** | 1,000,000 | Cosmetic capstone |

**Grand total all phases: ~4,553,600 coins**

### 8C. Dynamite Details

| Stage | Rate | Radius | Blocks | Damage | Est. coins/min |
|-------|------|--------|--------|--------|----------------|
| Dispenser (Pad 4) | 1/60s | 3x3x3 | 27 | 10 | 50 |
| + Blast I (Pad 7) | 1/60s | 5x5x3 | 75 | 10 | 100 |
| + Fuse I (Pad 8) | 1/45s | 5x5x3 | 75 | 10 | 130 |
| + Fuse II + Blast II | 1/30s | 5x5x5 | 125 | 10 | 500 |
| + Fuse III + Blast III | 1/20s | 7x7x5 | 245 | 10 | 2,000 |
| + Nuclear Fuse | 1/10s | 7x7x5 | 245 | 20 | 8,000+ |

> Dynamite damage 10 one-shots blocks up to ~layer 8 (dur ≤10).
> Nuclear (20 dmg) one-shots up to ~layer 14. Beyond that, dynamite
> softens blocks for pickaxe follow-up. Portal placement determines
> which layers the dynamite hits.

### 8D. Portal & Jetpack Summary

**Portals** (skip surface, go straight to valuable layers):
| Portal | Phase | Cost | Skip Layers |
|--------|-------|------|-------------|
| Layer 5 | 2 | 20k | Skip 4 layers of Grass/Dirt/Stone |
| Layer 10 | 2 | 50k | Direct Gold/Diamond access |
| Layer 15 | 3 | 125k | Premium ore zone |
| Layer 18 | 4 | 500k | Deepest, richest ores |

**Jetpack** (fly in pit, mine exposed walls):
| Level | Phase | Duration | Recharge |
|-------|-------|----------|----------|
| Basic | 2 | 20s | 60s |
| Upgraded | 3 | 45s | 45s |
| Turbo | 4 | 90s | 30s |

---

## 9. Hour-by-Hour Progression (Full Redesign)

### Income Model Per Rebirth Cycle

The player's income in each cycle comes from:
1. **Manual mining** — scales with shaft (speed) + head (power) + pickaxe tier (multi-mine + layers)
2. **NPC brainrots** — scales with count, rarity, brainrot income multiplier
3. **Dynamite** — scales with tycoon upgrades + portal access
4. **Spin wheel** — 5/day, EV ~27,500/day
5. **Playtime rewards** — ~2,700 coins + Rare brainrot + spin per day

### Rebirth Cycle Timing

"Quick double" rows (same gate as previous) are marked with ⚡ — these are fast wins
that break up the grind and keep the player hooked.

| R | Gate | Stat Cost | Avg Income | **Cycle Time** | Key Unlocks Helping This Cycle |
|---|------|-----------|-----------|---------------|-------------------------------|
| 1 | S5/H5 | 2,238 | ~40/min | **~55 min** | T0 pickaxe, 1 square, 1 NPC |
| 2 | S6/H6 | 4,128 | ~70/min | **~60 min** | T1 pick (coal!), tycoon pads |
| 3 | S7/H7 | 7,530 | ~100/min | **~55 min** | 2 squares, dynamite |
| 4 | S8/H8 | 13,654 | ~150/min | **~60 min** | 3 squares, portals soon |
| ⚡5 | S8/H8 | 13,654 | ~250/min | **~35 min** | T2 multi-mine 2! Quick win! |
| 6 | S9/H9 | 24,678 | ~350/min | **~50 min** | Auto-collect, Phase 2 tycoon |
| ⚡7 | S9/H9 | 24,678 | ~500/min | **~35 min** | 4 squares. Quick win! |
| 8 | S10/H10 | 44,522 | ~600/min | **~55 min** | 1.5x NPC income |
| ⚡9 | S10/H10 | 44,522 | ~900/min | **~35 min** | T3 pick (diamonds!). Quick win! |
| 10 | S11/H11 | 80,240 | ~1,200/min | **~55 min** | 5 squares, Phase 3 tycoon |
| ⚡11 | S11/H11 | 80,240 | ~1,600/min | **~40 min** | Premium Gacha. Quick win! |
| 12 | S12/H12 | 144,534 | ~2,000/min | **~60 min** | +1 daily spin, deep portals |
| ⚡13 | S12/H12 | 144,534 | ~2,800/min | **~40 min** | T4 multi-mine 3! Quick win! |
| 14 | S13/H13 | 260,262 | ~3,500/min | **~60 min** | 6 squares, nuclear dynamite |
| ⚡15 | S13/H13 | 260,262 | ~4,500/min | **~45 min** | 2.0x NPC income. Quick win! |
| 16 | S14/H14 | 468,574 | ~5,500/min | **~70 min** | Brainrot cap 15, Phase 4 |
| ⚡17 | S14/H14 | 468,574 | ~7,000/min | **~55 min** | Ultra Gacha. Quick win! |
| 18 | S15/H15 | 843,534 | ~8,500/min | **~80 min** | 7 squares, all portals |
| ⚡19 | S15/H15 | 843,534 | ~10,000/min | **~70 min** | 2.5x NPC. Quick win! |
| ⚡20 | S15/H15 | 843,534 | ~12,000/min | **~60 min** | 8 squares. TRIPLE FINALE! |

**Total active play: ~19 hours of mining + sell trips + setup**
**Realistic with breaks, exploring, gacha, tycoon building: ~25-28 hours = 12-14 days at 2 hrs/day**

> **Why quick doubles work:** After grinding to S10/H10 for R8, the player earns T3 pickaxe.
> Next cycle (R9) has the SAME gate. With T3's multi-mine and diamond access, they blow
> through it in 35 min. That fast win releases dopamine and motivates the next real grind.
> The pattern repeats every 2 rebirths, creating a satisfying push-reward rhythm.

> Income estimates factor in: pickaxe tier earned from previous rebirth, accumulated brainrots,
> tycoon pads (dynamite/portals/conveyor), spin wheel, and the brainrot income multiplier.
> Each cycle, the player starts at 0 currency but has MORE tools than the last cycle.

### Detailed Day-by-Day Walkthrough

#### DAY 1 (Hours 0-2) — "The Hook"

| Time | What Happens | Dopamine Hit |
|------|-------------|-------------|
| 0:00 | Join. 1 bonus spin → 2,000 coins. Start mining grass. | Free money! |
| 0:03 | Buy Pad 1 (Wall, 150). First tycoon pad! | Base is building! |
| 0:06 | Shaft 1 (50). Noticeably faster mining. | Speed up! |
| 0:08 | Pad 2 (Side Walls, 300). | Base growing! |
| 0:10 | Head 1 (50). Blocks break faster. | Power up! |
| 0:13 | Pad 3 (Floor Tiles, 400). | Looks cool! |
| 0:15 | Shaft 2 (90). Mining getting smoother. | Speed up again! |
| 0:17 | Head 2 (90). Two-hit most surface blocks. | Power! |
| 0:20 | **Pad 4: Dynamite Dispenser (750)**. | **DYNAMITE!** First stick spawns. |
| 0:21 | **Throw first dynamite**. 27 blocks explode at once! | **BOOM! Biggest moment yet** |
| 0:23 | Pad 5 (Storage, 1,000). Can stockpile 5 now. | More booms coming! |
| 0:25 | Shaft 3 (162). Head 3 (162). | Dual upgrade! |
| 0:28 | Pad 6 (Stairs, 1,500). Climb to roof, see the whole pit. | Exploration moment |
| 0:32 | **Pad 7: Blast Powder (2,500)**. Dynamite now 5x5x3! | **Way bigger explosions!** |
| 0:35 | 5-min playtime reward: 200 coins. | Free! |
| 0:38 | Shaft 4 (292). Pad 8: Fuse Timer (4,000). Dynamite every 45s. | Faster production! |
| 0:42 | Head 4 (292). Mining feels strong now. | Power! |
| 0:45 | Pad 9 (Doorway, 5,000). Base has a real entrance. | Looks like a house! |
| 0:50 | **Shaft 5 (525). Head 5 (525).** | **Stat gate reached!** |
| 0:51 | **REBIRTH #1!** → **Stone Pickaxe (T1) earned!** | **HUGE MOMENT. New pickaxe!** |
| 0:52 | Stats reset to 0. But now mining layers 5-6. COAL! | Deeper, richer ores |
| 0:53 | Bulk buy: +5 shaft (+5 head) using post-rebirth earnings. | Back to speed in 2 clicks |
| 0:55 | 15-min reward: 500 coins. Basic Gacha Pull → **First brainrot!** | **Collection starts!** |
| 1:00 | Deploy brainrot on your 1 square. Passive income starting. | AFK money! |
| 1:05 | **Pad 10: Ore Conveyor (8,000)**. Auto-sell! No more shop trips. | **Game-changer QoL** |
| 1:10 | Mine Coal zones. Income way up from T1 pickaxe. | Feeling the rebirth power |
| 1:15 | Shaft 6 (945). Head 6 (945). Approaching R2 gate. | Getting close... |
| 1:20 | 50-min reward: **Rare brainrot!** | **Free rare!** (Can't deploy yet — only 1 square) |
| 1:50 | **Shaft 6/Head 6 reached.** | **R2 gate!** |
| 1:52 | **REBIRTH #2!** → **+1 Collector Square** (2nd slot). | **Now you can deploy that rare!** |
| 1:53 | Bulk buy +6/+6. Deploy 2nd brainrot. 2 NPCs mining! | Quick re-level |
| 2:00 | **End of Day 1.** R2 done, T1 pickaxe, 2 squares, 2 brainrots. | Hooked. Coming back tomorrow. |

**Day 1 unlock count: ~20+** (10 tycoon pads, 6+ stat levels, 2 rebirths, 2+ brainrots, dynamite, conveyor, playtime rewards)
**Average: one unlock every 6 minutes for the first 2 hours.**

#### DAY 2 (Hours 2-4) — "Building the Army"

| Time | What Happens |
|------|-------------|
| 2:00 | 5 daily spins (EV: 27,500). Mine coal layers with T1. Income ~100/min. |
| 2:15 | Shaft 7/Head 7 reached. |
| 2:17 | **REBIRTH #3!** → **+1 Collector Square** (3rd slot). Deploy 3rd brainrot! |
| 2:20 | Bulk buy +7/+7. Three NPCs mining for you. Tycoon pads 11+ available. |
| 2:30 | Buy Pad 11: Second Floor (10k). Pad 12: **Jetpack Pad** (15k). |
| 2:35 | **First jetpack flight!** Fly over the pit. Mine exposed walls mid-air! |
| 2:45 | Buy **Layer 5 Portal** (20k). Skip surface, straight to coal layers! |
| 3:00 | Shaft 8/Head 8 reached. 3 NPCs + portal + dynamite = ~150/min. |
| 3:02 | **REBIRTH #4!** → **Iron Pickaxe (T2, multi-mine 2!)**. Layers 7-10! |
| 3:03 | Two blocks per swing! Gold ore unlocked! Income jumps to ~250/min. |
| 3:20 | Buy Fuse II (25k), Storage II (30k). Dynamite every 30s! |
| 3:30 | Shaft 8/Head 8 again — **SAME GATE as R4!** |
| 3:32 | ⚡ **REBIRTH #5!** → **Auto-Collect!** Quick win — only 35 min! |
| 3:33 | NPCs now deposit earnings automatically. No more manual pickup! |
| 3:33 | Also unlocks **Tycoon Phase 2** fully. Portals and jetpack upgrades! |
| 3:45 | Buy **Blast Powder II** (40k). Dynamite 5x5x5! |
| 3:55 | Buy **Layer 10 Portal** (50k). Direct gold/redstone access! |
| 4:00 | End of Day 2. R5 done, T2 pickaxe, auto-collect, 3 squares, Phase 2 started. |

#### DAY 3-4 (Hours 4-8) — "Power Surge"

| Time | What Happens |
|------|-------------|
| 4:00-4:50 | R6 cycle. Shaft/Head 9. 4 NPCs with auto-collect = serious passive. |
| 4:50 | **REBIRTH #6** → **+1 Collector Square** (4th slot). |
| 4:50-5:25 | ⚡ R7 cycle (same S9/H9 gate). Quick win with 4 squares! |
| 5:25 | **REBIRTH #7** → **1.5× Brainrot Income!** All 4 NPCs earn 50% more! |
| 5:25-6:20 | R8 cycle. Shaft/Head 10. Blast Powder III (150k). |
| 6:20 | **REBIRTH #8** → **Gold Pickaxe (T3)!** Diamond ore! Layers 11-14! |
| 6:20-6:55 | ⚡ R9 cycle (same S10/H10 gate). T3 multi-mine shreds. Quick win! |
| 6:55 | **REBIRTH #9** → **+1 Collector Square** (5th slot). |
| 6:55 | Also unlocks **Tycoon Phase 3**. Deep portals, nuclear dynamite! |
| 6:55-7:50 | R10 cycle. Shaft/Head 11. Buy Jetpack Upgrade (80k), Fuse III (100k). |
| 7:50 | **REBIRTH #10** → **Premium Gacha Unlock!** Way better brainrot odds! |
| 7:50 | **MILESTONE: Halfway done!** 5 squares, T3 pick, 1.5x NPC, Premium Gacha. |

**Hours 4-8: 5 rebirths in 4 hours.** The quick doubles keep the pace feeling fast.
Player has 5 squares, T3 pickaxe, auto-collect, 1.5x NPC income. Feeling powerful.

#### DAY 5-7 (Hours 8-14) — "Going Deep"

| Time | What Happens |
|------|-------------|
| 8:00-8:40 | ⚡ R11 cycle (same S11/H11 gate). Premium Gacha = better brainrots! |
| 8:40 | **REBIRTH #11** → **+1 Daily Spin** (6 total). Quick win! |
| 8:40-9:40 | R12 cycle. Shaft/Head 12. Buy **L15 Portal** (125k). Diamond zone access! |
| 9:40 | **REBIRTH #12** → **Diamond Pickaxe (T4, multi-mine 3!)** Layers 15-17! |
| 9:40-10:20 | ⚡ R13 cycle (same S12/H12 gate). T4 is devastating. Quick win! |
| 10:20 | **REBIRTH #13** → **+1 Collector Square** (6th slot). |
| 10:20-11:20 | R14 cycle. Shaft/Head 13. Nuclear Fuse (350k). Buy big tycoon pads. |
| 11:20 | **REBIRTH #14** → **2.0× Brainrot Income!** 6 NPCs × 2x = massive passive. |
| 11:20-12:05 | ⚡ R15 cycle (same S13/H13 gate). Quick win! |
| 12:05 | **REBIRTH #15** → **Brainrot Level Cap → 15!** Upgrade NPCs further. |
| 12:05 | Also unlocks **Tycoon Phase 4**. Nuclear dynamite, L18 portal, penthouse! |
| 12:05-14:00 | Buy Phase 4 pads. **L18 Portal** (500k). **Jetpack Turbo** (600k). |

**Hours 8-14: 5 rebirths in 6 hours.** Pace slows slightly but quick doubles prevent
any cycle from feeling like a slog. Player is now a mining powerhouse.

#### DAY 8-11 (Hours 14-20) — "The Endgame"

| Time | What Happens |
|------|-------------|
| 14:00-15:10 | R16 cycle. Shaft/Head 14. Brainrots at lvl 15, all portals active. |
| 15:10 | **REBIRTH #16** → **Ultra Gacha Unlock!** 30% Epic, 15% Legend, 5% Mythic! |
| 15:10-16:05 | ⚡ R17 cycle (same S14/H14 gate). Ultra pulls = Mythic brainrots! Quick win! |
| 16:05 | **REBIRTH #17** → **+1 Collector Square** (7th slot). |
| 16:05-17:25 | R18 cycle. Shaft/Head 15. Storage Vault (750k). Penthouse (1M). |
| 17:25 | **REBIRTH #18** → **2.5× Brainrot Income!** 7 high-level NPCs × 2.5x! |
| 17:25-18:35 | ⚡ R19 cycle (same S15/H15 gate). 2.5x income makes this fly. |
| 18:35 | **REBIRTH #19** → **+1 Collector Square (8th — ALL SLOTS FULL!)** |
| 18:35-19:35 | ⚡ R20 cycle (same S15/H15 gate again!). 8 NPCs, 2.5x, all tools. |
| 19:35 | **REBIRTH #20!!** → **OBSIDIAN PICKAXE (T5, multi-mine 4!)** |
| | **THE GAME IS COMPLETE.** Full pit access. Golden base overlay. Title unlocked. |

**The triple finale (R18/R19/R20 at same S15/H15 gate) gives the player three
consecutive quick wins, each one more exciting than the last. The final 3 hours
feel like a victory lap.**

### Unlock Cadence Summary

| Phase | Hours | Unlocks/Hr | Highlights |
|-------|-------|-----------|------------|
| Day 1 (Hook) | 0-2 | **~10/hr** | Pads, stats, R1-R2, dynamite, brainrots |
| Day 2 (Army) | 2-4 | **~6/hr** | R3-R5, T2 pickaxe, auto-collect, jetpack |
| Day 3-4 (Surge) | 4-8 | **~3/hr** | R6-R10, T3 pickaxe, Phase 2-3 tycoon |
| Day 5-7 (Deep) | 8-14 | **~2/hr** | R11-R15, T4 pickaxe, Phase 4 tycoon |
| Day 8-11 (End) | 14-20 | **~1.5/hr** | R16-R20, T5 pickaxe, triple finale |

**Nothing is ever more than ~30 minutes away.** Even in the endgame, the player
is always approaching a stat level, tycoon pad, or rebirth gate. The "quick double"
pattern ensures every other rebirth feels fast and rewarding.

---

## 10. What Makes This Loop Addictive (Designer Notes)

### The Three Hooks

**1. Variable Reward Schedule (Gacha + Spins)**
- Gacha pulls give random-rarity brainrots → "maybe this one is Mythic!"
- Spin wheel daily → anticipation every session start
- Rare brainrots from playtime rewards → surprise dopamine

**2. Clear Progress Bars (Stat Gates + Tycoon Pads)**
- Player can always SEE how close they are to the next rebirth
- Tycoon pads visible but greyed out → "I need 15,000 more for the jetpack"
- Shaft/head levels are small, frequent upgrades → constant "number go up"

**3. Transformative Moments (Rebirths)**
- Each rebirth CHANGES how you play, not just how fast
- T1: "I can mine Coal now!" T2: "TWO blocks per swing!" T3: "DIAMOND ORE!"
- Portals: "I can teleport into the pit?!" Jetpack: "I can FLY?!"
- These are the moments players tell their friends about

### The Retention Curve

```
Excitement
    ▲
    │  ╱╲    ╱╲      ╱╲        ╱╲          ╱╲
    │ ╱  ╲  ╱  ╲    ╱  ╲      ╱  ╲        ╱  ╲
    │╱    ╲╱    ╲  ╱    ╲    ╱    ╲      ╱    ╲
    │          ╲╱      ╲  ╱      ╲    ╱      ╲
    │                   ╲╱        ╲  ╱        ╲
    │                              ╲╱
    └──────────────────────────────────────────────────────→ Time
     R1  R2  R3  R4 ⚡R5  R6 ⚡R7  R8 ⚡R9  R10 ... ⚡R18 ⚡R19 ⚡R20
```

Each rebirth is a peak. Quick doubles (⚡) are mini-peaks between the grind.
The triple finale at R18-R20 is the biggest sustained peak. The key is:
- Dips never go too low (tycoon pads + stat levels fill the gaps)
- Peaks get bigger (each reward is more impactful than the last)
- The pattern is predictable enough to trust, varied enough to excite

### Anti-Frustration Design

| Problem | Solution |
|---------|----------|
| "I just rebirthed and I'm weak" | Bulk buy +10 gets you back fast |
| "Mining surface is boring" | Portals skip to deep layers |
| "I have to walk to the shop" | Ore Conveyor auto-sells |
| "My brainrots are useless" | NPC damage scales with rarity + income mult |
| "I don't know what to do" | Rebirth roadmap always visible |
| "The grind is repetitive" | Dynamite, jetpack, portals add variety |
| "What's the point of rebirthing?" | Each reward visibly changes gameplay |

---

## 11. Config Changes Summary

### Pickaxe Tiers (NO LONGER PURCHASABLE — rebirth rewards only)

```lua
-- PitConfig.PICKAXE_TIERS (remove cost field, add rebirthRequired)
[0] = { name = "Wooden",   maxLayer = 4,  multiMine = 1, rebirthRequired = 0 },
[1] = { name = "Stone",    maxLayer = 6,  multiMine = 1, rebirthRequired = 1 },
[2] = { name = "Iron",     maxLayer = 10, multiMine = 2, rebirthRequired = 4 },
[3] = { name = "Gold",     maxLayer = 14, multiMine = 2, rebirthRequired = 8 },
[4] = { name = "Diamond",  maxLayer = 17, multiMine = 3, rebirthRequired = 12 },
[5] = { name = "Obsidian", maxLayer = 20, multiMine = 4, rebirthRequired = 20 },
```

### Shaft/Head (No cap, 1.8x scaling, bulk buy)

```lua
-- ShopConfig.UPGRADES (revised)
shaft = {
    displayName = "Shaft (Speed)",
    baseCost = 50,
    costMultiplier = 1.8,
    maxLevel = 999,  -- effectively uncapped
    bulkOptions = { 1, 5, 10, "MAX" },
},
head = {
    displayName = "Head (Power)",
    baseCost = 50,
    costMultiplier = 1.8,
    maxLevel = 999,
    bulkOptions = { 1, 5, 10, "MAX" },
},

-- MAX button: buys levels up to the current rebirth gate requirement.
-- Example: Player at R6 (gate S9/H9), shaft is 3. MAX buys shaft 4-9 (6 levels).
-- Shows total cost and result: "Shaft 3 → 9: $18,416"
-- Greyed out if player can already meet or exceed the gate, or can't afford it.
```

### Rebirth Config (Complete Rewrite — 20 Rebirths)

```lua
-- RebirthConfig (revised)
local RebirthConfig = {}

RebirthConfig.MAX_REBIRTHS = 20

RebirthConfig.GATES = {
    -- STARTER TIER (R1-R5)
    [1]  = { shaft = 5,  head = 5  },
    [2]  = { shaft = 6,  head = 6  },
    [3]  = { shaft = 7,  head = 7  },
    [4]  = { shaft = 8,  head = 8  },
    [5]  = { shaft = 8,  head = 8  },  -- quick double!
    -- BRONZE TIER (R6-R10)
    [6]  = { shaft = 9,  head = 9  },
    [7]  = { shaft = 9,  head = 9  },  -- quick double!
    [8]  = { shaft = 10, head = 10 },
    [9]  = { shaft = 10, head = 10 },  -- quick double!
    [10] = { shaft = 11, head = 11 },
    -- SILVER TIER (R11-R15)
    [11] = { shaft = 11, head = 11 },  -- quick double!
    [12] = { shaft = 12, head = 12 },
    [13] = { shaft = 12, head = 12 },  -- quick double!
    [14] = { shaft = 13, head = 13 },
    [15] = { shaft = 13, head = 13 },  -- quick double!
    -- GOLD TIER (R16-R20)
    [16] = { shaft = 14, head = 14 },
    [17] = { shaft = 14, head = 14 },  -- quick double!
    [18] = { shaft = 15, head = 15 },
    [19] = { shaft = 15, head = 15 },  -- quick double!
    [20] = { shaft = 15, head = 15 },  -- TRIPLE FINALE!
}

RebirthConfig.REWARDS = {
    -- STARTER TIER
    [1]  = { type = "pickaxe",      tier = 1,    description = "Stone Pickaxe (layers 5-6)" },
    [2]  = { type = "square",       count = 1,   description = "+1 Collector Square (2nd)" },
    [3]  = { type = "square",       count = 1,   description = "+1 Collector Square (3rd)" },
    [4]  = { type = "pickaxe",      tier = 2,    description = "Iron Pickaxe (layers 7-10, 2x mine)" },
    [5]  = { type = "autoCollect",               description = "Auto-Collect (NPCs deposit automatically)" },
    -- BRONZE TIER
    [6]  = { type = "square",       count = 1,   description = "+1 Collector Square (4th)" },
    [7]  = { type = "brainrotMult", value = 1.5, description = "1.5x Brainrot Income" },
    [8]  = { type = "pickaxe",      tier = 3,    description = "Gold Pickaxe (layers 11-14)" },
    [9]  = { type = "square",       count = 1,   description = "+1 Collector Square (5th)" },
    [10] = { type = "gachaUnlock",  tier = "premium", description = "Premium Gacha Unlock" },
    -- SILVER TIER
    [11] = { type = "dailySpin",    count = 1,   description = "+1 Daily Spin (6 total)" },
    [12] = { type = "pickaxe",      tier = 4,    description = "Diamond Pickaxe (layers 15-17, 3x mine)" },
    [13] = { type = "square",       count = 1,   description = "+1 Collector Square (6th)" },
    [14] = { type = "brainrotMult", value = 2.0, description = "2.0x Brainrot Income" },
    [15] = { type = "brainrotCap",  value = 15,  description = "Brainrot Level Cap → 15" },
    -- GOLD TIER
    [16] = { type = "gachaUnlock",  tier = "ultra", description = "Ultra Gacha Unlock" },
    [17] = { type = "square",       count = 1,   description = "+1 Collector Square (7th)" },
    [18] = { type = "brainrotMult", value = 2.5, description = "2.5x Brainrot Income" },
    [19] = { type = "square",       count = 1,   description = "+1 Collector Square (8th — FULL!)" },
    [20] = { type = "pickaxe",      tier = 5,    description = "Obsidian Pickaxe (layers 18-20, 4x mine)" },
}

-- Tycoon phase unlocks (bonus, not a rebirth reward)
RebirthConfig.TYCOON_PHASES = {
    [1] = { minRebirth = 0,  pads = {1, 10},  name = "Basic Base" },
    [2] = { minRebirth = 5,  pads = {11, 17}, name = "Enhanced" },
    [3] = { minRebirth = 10, pads = {18, 24}, name = "Advanced" },
    [4] = { minRebirth = 15, pads = {25, 30}, name = "Elite" },
}

-- What resets on rebirth
RebirthConfig.RESETS = { "shaftLevel", "headLevel", "currency", "ore", "pickaxeSpeed", "pickaxePower" }

-- What persists:
-- pickaxeTier, ownedBrainrots, tycoonPurchased, dynamiteStock, maxSquares,
-- brainrotIncomeMult, autoCollect, premiumGachaUnlocked, ultraGachaUnlocked,
-- extraDailySpins, brainrotLevelCap

return RebirthConfig
```

### NPC Damage Buff

```lua
-- BrainrotMiningServer (add near top)
local NPC_DAMAGE = {
    Common = 1, Uncommon = 2, Rare = 3,
    Epic = 5, Legendary = 8, Mythic = 12
}

-- Line 680: change from
durability = durability - 1
-- to
durability = durability - (NPC_DAMAGE[brainrotInfo.rarity] or 1)
```

### MiningSystem Fix (Remove Double-Dip)

```lua
-- MiningSystem line 113: REMOVE this line
-- data.currency += oreValue

-- KEEP line 114:
data.ore[blockType] = (data.ore[blockType] or 0) + 1
```

### New PlayerDataManager Fields

```lua
-- Add to DEFAULT_DATA:
maxSquares = 1,              -- starts at 1! increases via rebirth rewards (persists)
brainrotIncomeMult = 1.0,    -- increases via rebirth rewards (persists)
autoCollect = false,          -- unlocked at R5 (persists)
premiumGachaUnlocked = false, -- unlocked at R10 (persists)
ultraGachaUnlocked = false,   -- unlocked at R16 (persists)
extraDailySpins = 0,          -- +1 at R11 (persists)
brainrotLevelCap = 10,        -- raised to 15 at R15 (persists)
tycoonPurchased = {},          -- { [padIndex] = true } (persists)
dynamiteStock = 0,             -- (persists)
lastDynamiteTime = 0,          -- (persists)

-- Update performRebirth() to NOT reset any of the above.
-- Also keep: pickaxeTier, ownedBrainrots, rebirths
-- Only reset: shaftLevel, headLevel, currency, ore, pickaxeSpeed, pickaxePower

-- Reward granting in RebirthServer (pseudocode):
-- local reward = RebirthConfig.REWARDS[newRebirthCount]
-- if reward.type == "pickaxe" then data.pickaxeTier = reward.tier
-- elseif reward.type == "square" then data.maxSquares += reward.count
-- elseif reward.type == "brainrotMult" then data.brainrotIncomeMult = reward.value
-- elseif reward.type == "autoCollect" then data.autoCollect = true
-- elseif reward.type == "gachaUnlock" then
--     if reward.tier == "premium" then data.premiumGachaUnlocked = true
--     elseif reward.tier == "ultra" then data.ultraGachaUnlocked = true end
-- elseif reward.type == "dailySpin" then data.extraDailySpins += reward.count
-- elseif reward.type == "brainrotCap" then data.brainrotLevelCap = reward.value
-- end
```

---

## 12. Tuning Levers

### If progression is too FAST:
- Raise stat gate levels (e.g., remove a "quick double" — R5 needs S9/H9 instead of S8/H8)
- Increase shaft/head cost multiplier (1.8 → 2.0)
- Reduce dynamite production rates
- Reduce spin wheel payouts
- Remove the triple finale (make R19/R20 need S16/H16)

### If progression is too SLOW:
- Lower stat gate levels (e.g., add another quick double)
- Decrease shaft/head cost multiplier (1.8 → 1.6)
- Add more playtime reward milestones
- Increase NPC damage values
- Give 2 bonus spins to new players instead of 1
- Reduce gate by 1 level on the cycle that's too slow (~40% cost cut)

### If a specific rebirth cycle feels like a wall:
- That cycle's gate level is the knob. Reduce by 1 level = ~44% cost reduction (1.8x).
- Example: R14 at S13/H13 = 260,262 both stats. Reduce to S12/H12 = 144,534. Much better.
- Or make it a quick double of the previous gate (same level = instant relief).

### If the early game is too slow (player leaves before R1):
- Reduce R1 gate from S5/H5 to S4/H4 (cost: 1,188 both stats vs 2,238)
- Increase tycoon pad density in Phase 1 (more frequent small unlocks)
- Give 2 bonus spins instead of 1 (more starting capital)

### If endgame feels hollow (player quits after R15):
- Make R16-R20 rewards more visually impressive (Ultra Gacha has special effects)
- Add cosmetic rewards alongside mechanical ones (golden pickaxe skin, special trail)
- Ensure Mythic brainrots from Ultra Gacha are noticeably powerful and flashy

### Key metrics to playtest:
1. **Time to R1** (target: 50-60 min)
2. **Quick double cycles** (target: 30-40 min each, should feel fast)
3. **Normal cycles R6-R15** (target: 50-70 min each)
4. **Endgame cycles R16-R20** (target: 55-80 min each)
5. **Total time to R20** (target: 25-28 active hours = ~2 weeks at 2 hrs/day)
6. **Longest gap between ANY unlock** (target: never > 25 min)
7. **NPC income as % of total** (target: 15-30% by R10, 30-45% by R20)
8. **Player quit rate between rebirths** (if high → check if cycle is a wall, add quick double)
