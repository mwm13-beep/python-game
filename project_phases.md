# ⚔️ Turn-Based Tactics RPG — Project Phases

## 🎯 Project Vision

A story-driven, single-player, turn-based tactics RPG with rich narrative, character growth, and exploration. Players will travel through a connected world (inspired by Dragon Quest), battle visible enemies, and unlock class-based abilities that can be carried across builds. The game will feature a 2.5D pixel art style and be developed for eventual release on Steam.

---

## Phase 1: 🎮 Vertical Slice Demo (DQ1 Scope)

**Core Goal:**  
Build a polished, small-scale playable demo that includes exploration, visible enemies, turn-based combat, basic dialogue, and a few connected maps — playable start to finish in 1–2 hours.

**Key Objectives:**
- [ ] Implement player-controlled free exploration on a tile-based map
- [ ] Add basic terrain collision
- [ ] Create a system for enemies to patrol and detect proximity
- [ ] Implement combat state transition on player-enemy contact
- [ ] Expand combat system to include HP, death, movement, and basic abilities
- [ ] Create a simple ability framework (e.g. rush attack, ranged attack)
- [ ] Create temporary units/assets for testing (using placeholder or AI-bootstrapped art)
- [ ] Add rudimentary UI (HP display, action buttons)
- [ ] Build a dialogue system triggered by events/NPCs
- [ ] Add static map transitions (e.g. between village, forest, dungeon)
- [ ] Create a demo area with 2–3 connected maps and 3+ enemy types

---

## Phase 2: 📚 Narrative and System Expansion

**Core Goal:**  
Lay the groundwork for long-form storytelling and early game scaling. Focus on adding support for branching dialogue, early quests, and persistent state between maps.

**Key Objectives:**
- [ ] Add dialogue scripting with branching choices
- [ ] Add a first-pass quest system (trigger → progress → reward)
- [ ] Introduce persistent data (party status, flags, visited locations)
- [ ] Improve UI polish and in-game prompts
- [ ] Expand the world map to include at least one town + multi-room dungeon
- [ ] Add 2–3 new enemy types with unique abilities
- [ ] Add 2–3 new abilities (cross-class compatible)

---

## Phase 3: 🧠 Class & Ability Depth

**Core Goal:**  
Introduce more tactical complexity: class switching, skill inheritance, and unit loadouts.

**Key Objectives:**
- [ ] Implement a class system with stat growth and equipable abilities
- [ ] Create UI for viewing/managing learned abilities
- [ ] Allow learned abilities to be equipped across compatible classes
- [ ] Add a system for ability acquisition (e.g. via leveling, story events, trainers)
- [ ] Expand unit behavior in combat (AI logic, priority targeting)
- [ ] Add enemy variants that force ability and strategy variation

---

## Phase 4: 🌍 World Building & Full Loop

**Core Goal:**  
Support a full-game loop: world progression, save/load, multiple story arcs, NPCs, and non-combat gameplay.

**Key Objectives:**
- [ ] Add save/load system with slot support
- [ ] Implement fast travel / map navigation system
- [ ] Add towns with shops, inns, and flavor NPCs
- [ ] Add puzzle or non-combat exploration mechanics
- [ ] Build more maps: overworld routes, multiple dungeons, unique regions
- [ ] Support optional content: hidden areas, optional bosses, side quests

---

## Phase 5: 🚀 Polish & Steam Release

**Core Goal:**  
Finalize the game with polish, QA, and platform prep for Steam distribution.

**Key Objectives:**
- [ ] Replace placeholder assets with finalized art/music (created or refined manually)
- [ ] Add polish animations, sound design, and transitions
- [ ] Optimize performance and memory usage
- [ ] Integrate Steam SDK (achievements, save sync)
- [ ] Package game for distribution (build system, resolution settings, etc.)
- [ ] Write store page, trailer, screenshots, and marketing material

---

## Notes:
- Art and music assets will be bootstrapped with AI tools early and replaced as the developer's personal skill improves.
- Phase boundaries are flexible. Tasks may shift or be revisited as new ideas arise during development.
