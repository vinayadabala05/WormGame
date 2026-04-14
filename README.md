# 🐍 2D Worm AI Game (Multi-Agent System)

## 📌 Overview

This project is a **2D Worm (Snake) Game with Autonomous Agents**, developed as part of a technical assignment.

The system simulates **10 independent agents**, each controlling a worm with a head and 3 body segments.
Each agent autonomously moves toward a target using AI-based decision logic.

---

## 🎯 Objective

* Create a worm-based game
* Implement an autonomous agent
* Simulate reward-based learning behavior

---

## 🧠 Key Features

### ✔ Multi-Agent System

* 10 agents running simultaneously
* Each agent operates independently
* Same behavior logic for all agents

### ✔ Worm Structure

* Head + 3 body segments
* Smooth movement
* Realistic snake-like visuals

### ✔ Autonomous Movement

Agents automatically:

* Detect target position
* Move toward goal direction
* Optimize path using heuristic logic

---

## 🎮 Game Mechanics

### 🟢 Goal

Each worm moves toward a randomly spawned target (food).

### 🔴 Target Behavior

* New target appears after consumption
* Random position in grid

### 🔁 Reset Condition

* Agent resets when hitting boundaries

---

## 🧮 Reward Function (ML-Inspired)

This project simulates a **geometric reward system** using:

### 1. Velocity Matching

* Measures how efficiently the agent moves closer to the target
* Based on distance reduction

### 2. Direction Alignment

* Measures alignment between movement direction and target direction
* Uses cosine similarity

### 3. Combined Reward

```
Reward = (Velocity × 0.6 + Direction × 0.4)
```

### 4. Decay-Based Accumulation

```
Total Reward = Previous Reward × 0.99 + Step Reward
```

### 5. Bonus Reward

* Additional reward when target is reached

---

## 📊 Benchmark

* Displayed as:

```
Avg Reward: X / 800
```

* Reward is scaled to simulate the benchmark value of **800**
* Agents converge toward higher reward values over time

---

## 📦 Project Structure

```
project/
│
├── game.py          # Main game and AI logic
├── README.md        # Documentation
└── requirements.txt # Dependencies (optional)
```

---

## ⚙️ Setup Instructions

### 1. Install Python (3.10 recommended)

### 2. Install dependencies

```bash
pip install pygame
```

### 3. Run the game

```bash
python game.py
```

---

## 🖥️ Output

* 10 worms moving simultaneously
* Each chasing its own target
* Real-time reward display
* Smooth 2D + 3D-style visuals

---

## 🚀 Agent Logic Explanation

Instead of full Reinforcement Learning training, this implementation uses a **heuristic-based approach** that simulates RL behavior:

* Continuous feedback from environment
* Reward-driven movement optimization
* Direction + velocity-based decisions

This approach ensures:

* Simplicity
* Fast execution
* Clear demonstration of agent intelligence

---

## 📌 Notes

* Visual observations: ❌ Not used
* Continuous actions: ❌ Simulated via directional movement
* Observation space: ❌ Simplified

👉 Focus is on demonstrating **core AI behavior and reward-driven decision making**

---

## 🎥 (Optional)

You can include:

* Demo video
* Screenshots of gameplay

---

## ✅ Conclusion

This project successfully demonstrates:

* Multi-agent system design
* Autonomous decision-making
* Reward-based optimization

---

## 👨‍💻 Author

Vinay Adabala

---
