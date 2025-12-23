# Tic-Tac-Toe (Python CLI)

A simple terminal-based **Tic-Tac-Toe** game written in Python.

This project was originally created as one of the assignments during a Python course and later refactored and packaged as a standalone CLI application.

---

## Features

- Two-player mode (X vs O)
- Runs directly in the terminal
- Input validation
- Win and draw detection
- Cross-platform (macOS, Windows, Linux)

---

## Requirements

- Python **3.9+**

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/KirylDorakh/tic-tac-toe.git
cd tic-tac-toe
```

### 2. (Recommended) Create a virtual environment
macOs:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install the project
```bash
pip install .
```

---

## How to Run

After installation, simply run:
```bash
tictactoe
```

---

## How to Play

- Players take turns entering:
  - a row number (1–3)
  - a column number (1–3)
- The first player to get three symbols in a row (row, column, or diagonal) wins.
- If the board is full and no player wins, the game ends in a draw.