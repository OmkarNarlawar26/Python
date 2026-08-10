# 🎮 Hangman Game

A simple command-line **Hangman game built using Python**. The player has to guess the hidden word one letter at a time before running out of lives.

## 📌 About the Project

This project is a console-based implementation of the classic Hangman game.

A random word is selected from a predefined word list, and the player attempts to guess it by entering one letter at a time. For every incorrect guess, the player loses a life and the Hangman figure progresses.

The project was created to practice **Python fundamentals, loops, conditional statements, lists, functions/modules, user input, and the `random` module**.

## ✨ Features

* 🎲 Random word selection
* ❤️ 6 lives for each game
* 🔤 Letter-by-letter guessing
* 🔁 Handles repeated letters in words
* ⚠️ Input validation
* ❌ Tracks incorrect guesses
* 🏆 Win and lose conditions
* 🎨 ASCII Hangman graphics
* 📚 Large collection of words

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Python lists
* Loops and conditional statements
* User input

## 📂 Project Structure

```text
Hangman-Game/
│
├── Code.py
├── hangman_art.py
├── hangman_words.py
├── README.md
└── .gitignore
```

### File Description

| File               | Description                                 |
| ------------------ | ------------------------------------------- |
| `Code.py`          | Contains the main game logic                |
| `hangman_art.py`   | Contains Hangman stages and game logo       |
| `hangman_words.py` | Contains the list of words used in the game |
| `README.md`        | Project documentation                       |
| `.gitignore`       | Specifies files Git should ignore           |

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Hangman-Game.git
```

### 2. Open the project directory

```bash
cd Hangman-Game
```

### 3. Run the game

```bash
python Code.py
```

## 🎮 How to Play

1. Run the program.
2. A random word will be selected.
3. Enter one letter when prompted.
4. If the letter exists in the word, it will be revealed.
5. If the letter is incorrect, you lose one life.
6. Continue guessing until:

   * You reveal the complete word → **You Win 🎉**
   * You lose all 6 lives → **Game Over 💀**

## 🖥️ Example

```text
****************************6/6 LIVES LEFT****************************

Guess a letter: a

Word to guess: _ a _ _ _

****************************5/6 LIVES LEFT****************************

Guess a letter: z

You guessed z, that's not in the word. You lose a life.

Word to guess: _ a _ _ _

****************************YOU WIN****************************
```

## 🧠 Concepts Practiced

This project helped practice:

* Variables and data types
* Lists
* `for` and `while` loops
* `if-elif-else` conditions
* String manipulation
* User input
* Random selection
* Modules and imports
* Basic game logic

## 🔮 Future Improvements

Possible improvements for future versions:

* Add difficulty levels
* Add a score system
* Add multiple categories of words
* Add replay functionality
* Add hints
* Create a graphical user interface using Tkinter
* Add sound effects

## 👨‍💻 Author

**Omkar Narlawar**

If you found this project useful, feel free to ⭐ the repository.
