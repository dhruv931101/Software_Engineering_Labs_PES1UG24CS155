# Lab 4 — Centipede Repair Lab

**Student Name:** Dhruv Swatantramath  
**SRN:** PES1UG24CS155  
**Course:** Software Engineering

## 1. Project Overview

This project is a single-file Centipede-lite game developed using **Python and Pygame**. It demonstrates segment-chain movement, chain splitting, projectile-versus-grid collision, and wave-based difficulty in an object-oriented codebase.

The lab uses an AI assistant as a debugging and pair-programming partner to analyze existing code, fix bugs, implement features, and verify the resulting behavior.

## 2. Game Features

- Player movement restricted to the bottom section of the screen.
- Projectile shooting using the Space key.
- Centipede segments that move across the screen and descend when encountering a border or mushroom.
- Mushrooms that obstruct movement and can be destroyed by shooting.
- Chain splitting when a body segment is hit.
- Wave-based difficulty, scoring, lives, reset, and game-over behavior.

## 3. Completed Vibe Coding Changes

### Task 1: Fix Mushroom Durability Bug
Fixed the mushroom durability logic so that a mushroom with four hit points requires exactly four successful hits to disappear.

### Task 2: Implement Mushroom Color Changes
Implemented `mushroom_color(hp)` to visually indicate the mushroom's remaining hit points.

### Task 3: Implement Segment Hit Effect
Implemented `on_segment_hit(segment, score)` to display a temporary visual spark or hit effect when a Centipede segment is destroyed.

### Task 4: Implement Progressive Wave Speed
Implemented `wave_speed_bonus(wave)` so later waves progressively increase the Centipede's movement speed.

## 4. Expected Behavior and Testing

The completed game is intended to preserve the existing gameplay while supporting the following behavior:

- Mushrooms require four hits to disappear.
- Mushroom color reflects remaining durability.
- Destroying a body segment splits the chain into independent chains.
- The game preserves player movement, shooting, scoring, lives, reset, and game-over functionality.
- Clearing a wave starts the next wave with increased movement speed.

## 5. Controls

| Key | Action |
|---|---|
| Arrow keys | Move the player |
| Space | Fire projectiles |
| R | Reset the game |

## 6. Technologies Used

- Python 3.10+
- Pygame
- Git and GitHub
- AI-assisted debugging and pair programming

## 7. Lab 4 Deliverables

The `Lab-4/` folder contains the game implementation and submission evidence:

- `game.py` — Source code for the completed game.
- `Before.mp4` — Video evidence of the game before the changes.
- `After.mp4` — Video evidence of the game after the changes.
- `Chat_History_Lab4.pdf` — Chat history documenting the AI-assisted development process.

## 8. Folder Structure

```text
Lab-4/
├── README.md
├── game.py
├── Before.mp4
├── After.mp4
└── Chat_History_Lab4.pdf
```

## 9. Summary

This lab demonstrates iterative software development using AI-assisted debugging, code review, bug fixing, and feature implementation. The final game incorporates mushroom durability correction, visual feedback, segment-hit effects, and progressive wave difficulty while preserving the core gameplay mechanics.
