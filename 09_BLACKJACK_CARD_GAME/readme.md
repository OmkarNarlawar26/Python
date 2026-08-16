# 🃏 Blackjack Game

A simple **console-based Blackjack game built using Python**. The player competes against the computer while following the basic rules of Blackjack.

## ✨ Features

* Random card dealing
* Player vs Computer gameplay
* Blackjack detection
* Automatic Ace handling (`11` → `1`)
* Computer draws cards until reaching 17
* Win, lose, and draw detection
* Option to play multiple rounds

## 🛠️ Technologies Used

* **Python**
* `random` module
* `os` module

## 📂 Project Structure

```text
Blackjack/
│
├── Code.py
├── Art.py
└── README.md
```

## 🎮 How to Play

1. Run the program.
2. Type `y` to start the game.
3. You and the computer receive two cards.
4. Type:

   * `y` → Draw another card
   * `n` → Pass
5. Try to get as close to **21** as possible without going over.
6. The computer automatically draws cards until its score reaches at least **17**.
7. The final scores are compared and the winner is displayed.

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python Code.py
```

No external libraries are required.

## 🧠 Concepts Used

* Functions
* Lists
* Loops
* Conditional statements
* Random module
* User input
* Function arguments and return values

## 📌 Blackjack Rules Implemented

* A score of exactly **21 with two cards** is considered Blackjack.
* An Ace (`11`) is automatically converted to `1` when needed to prevent the score from exceeding 21.
* A score above **21** results in a loss.

## 👨‍💻 Author

**Omkar Narlawar**
