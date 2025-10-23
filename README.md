# Dice Rolling Game 🎲

A simple command-line game written in Python that simulates the rolling of two standard six-sided dice. The game allows the user to roll the dice repeatedly until they choose to stop.

---

## 🚀 Getting Started

### Prerequisites

You'll need **Python 3** installed on your system to run this game.

### How to Run

1.  **Clone the repository** to your local machine:

    ```bash
    git clone [https://github.com/YourUsername/dice-rolling-game.git](https://github.com/YourUsername/dice-rolling-game.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd dice-rolling-game
    ```

3.  Run the script using the Python interpreter:

    ```bash
    python dice.py
    ```

---

## 🎮 How to Play

The game runs in a continuous loop, prompting you before each roll.

1.  When prompted **"Roll the dice? (y/n):"**:
    * Enter **`y`** (or just press **Enter**) to roll the two dice. The results (e.g., "Dice 1: 3, Dice 2: 5") will be displayed.
    * Enter **`n`** to stop the game. The program will print **"Thanks for playing!"** and exit.
    * If you enter anything else, the program will print **"invalid choice!"** and prompt you again.

---

## 💻 Code Overview

The script is contained in a single file, `dice.py`, and utilizes the following key Python features:

* **import random**: Necessary for generating random numbers to simulate the dice rolls.
* **while True:**: Creates the main game loop that continues until the user explicitly enters **`n`**.
* **random.randint(1, 6)**: Generates a random integer between 1 and 6 (inclusive) for each of the two dice.
* **Input Handling**: The input is normalized using `.lower().strip()` to handle variations in user input (e.g., 'Y ', 'y').
* **Conditional Logic**: The `if/elif/else` block checks the user's input (`choice`) to determine whether to roll the dice, quit the game, or notify the user of an invalid entry.
