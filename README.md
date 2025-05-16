# Conway’s Game of Life – Interactive Python Visualizer 🧬

![Game Demo](https://github.com/LAKSHYAMARODIA01/Conway-s-Game-of-Life/blob/main/demo.gif?raw=true)

A feature-rich, interactive implementation of **Conway's Game of Life** in Python using **Pygame**, with support for:

- 🟩 Custom patterns (save/load from `.txt`)
- ⏯️ Simulation control
- 💾 Pattern persistence
- 📸 GIF recording
- 🖱️ Real-time cell editing

---

## 📌 What is Conway’s Game of Life?

Conway’s Game of Life is a **zero-player game** — a cellular automaton where cells on a grid live, die, or reproduce based on mathematical rules.

You provide the **initial pattern**, and the game evolves by itself!

### 🌱 Core Rules

1. Any live cell with **fewer than 2** live neighbors dies (underpopulation).
2. Any live cell with **2 or 3** live neighbors lives on.
3. Any live cell with **more than 3** live neighbors dies (overpopulation).
4. Any dead cell with **exactly 3** live neighbors becomes alive (reproduction).

---

## 📁 Project Structure

```

conway\_game\_of\_life/
│
├── life.py             # Main driver script
├── board.py            # Grid state and update logic
├── draw\.py             # Renders the grid and UI
├── controls.py         # Handles user inputs
├── persistence.py      # Load/save pattern files
├── gif\_recorder.py     # Records gameplay into a GIF
├── README.md           # This file
├── requirements.txt    # Dependencies
└── patterns/
└── glider.txt      # Sample glider pattern

````

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/LAKSHYAMARODIA01/Conway-s-Game-of-Life.git
cd Conway-s-Game-of-Life/conway_game_of_life
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python life.py
```

---

## 🎮 Controls

| Key         | Action                       |
| ----------- | ---------------------------- |
| `SPACE`     | Pause / Resume simulation    |
| `N`         | Step forward 1 generation    |
| `C`         | Clear the board              |
| `R`         | Randomly fill board          |
| `S`         | Save current pattern to file |
| `L`         | Load pattern from file       |
| `G`         | Start/Stop GIF recording     |
| `Mouse`     | Toggle cell alive/dead       |
| `ESC`/Close | Exit the game                |

---

## 🖼️ Sample Pattern

### 📂 `/patterns/glider.txt`

```
0 1 0
0 0 1
1 1 1
```

You can save your own patterns in similar `.txt` files using the in-game `S` key.

---

## 📸 GIF Output Example

Below is a sample GIF generated using the in-app recording feature (`G` key):

![Demo](https://github.com/LAKSHYAMARODIA01/Conway-s-Game-of-Life/blob/main/demo.gif?raw=true)

---

## 💡 Highlights

* Fully modular Python codebase
* Pattern editor and file-based persistence
* Clean, resizable grid rendering
* Built-in `.txt` parser for patterns
* Easy export of evolving patterns as GIFs

---

## 📦 Requirements

```
pygame
imageio
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Feel free to fork, add more patterns, enhance UI, or optimize performance!

> Star 🌟 the project if you find it useful or fun.

---

## 🧑‍💻 Author

**Lakshya Marodia**
🔗 [GitHub Profile](https://github.com/LAKSHYAMARODIA01)

---

## 📜 License

This project is licensed under the MIT License — use it freely for personal and educational projects.


