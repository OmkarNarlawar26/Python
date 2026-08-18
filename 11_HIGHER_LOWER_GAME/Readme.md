# 🎮 Higher Lower Game

A simple **Higher Lower guessing game built with Python**. The player is shown two random accounts and must guess which account has more followers. The game continues until the player makes an incorrect guess.

## 📌 About the Project

The **Higher Lower Game** is a console-based Python project that demonstrates fundamental programming concepts such as:

* Functions
* Loops
* Conditional statements
* Lists and dictionaries
* Random selection
* User input
* Variable scope
* Game state management
* Modular and reusable code

The project also allows the player to **restart the game after losing**.

## 🎯 How the Game Works

1. The game displays two accounts:

   * **A**
   * **B**
2. The player guesses which account has more followers.
3. If the guess is correct:

   * The score increases by 1.
   * Account B becomes the next Account A.
   * A new Account B is selected.
4. If the guess is incorrect:

   * The game ends.
   * The final score is displayed.
5. The player can choose to play again.

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* `os` module

## 📂 Project Structure

```text
Higher-Lower-Game/
│
├── main.py
├── Art.py
├── game_data.py
└── README.md
```

### File Description

| File           | Description                                      |
| -------------- | ------------------------------------------------ |
| `main.py`      | Contains the main game logic and functions       |
| `Art.py`       | Contains the game logo and VS artwork            |
| `game_data.py` | Contains account information and follower counts |
| `README.md`    | Project documentation                            |

## ⚙️ Main Functions

### `format_data(account)`

Formats the account information into a readable sentence.

```python
format_data(account)
```

Example output:

```text
Instagram, a Social Media Platform, from United States
```

### `check_answer(user_guess, a_followers, b_followers)`

Compares the follower counts of Account A and Account B and checks whether the player's guess is correct.

```python
check_answer(user_guess, a_followers, b_followers)
```

### `play_game()`

Contains the complete game logic including:

* Score management
* Random account selection
* User input
* Answer checking
* Game continuation
* Game-over handling

The function can be called again to start a fresh game.

## 🧠 Concepts Learned

This project helped practice:

* Creating and using Python functions
* Passing arguments to functions
* Returning values from functions
* Working with dictionaries
* Accessing dictionary values
* Using `random.choice()`
* Using `while` loops
* Using `if-else` conditions
* Managing game state
* Using local variables inside functions
* Creating reusable game logic
* Handling repeated gameplay

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Higher-Lower-Game.git
```

### 2. Navigate to the project directory

```bash
cd Higher-Lower-Game
```

### 3. Run the game

```bash
python main.py
```

## 🎮 Example Gameplay

```text
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

VS

Against B: Taylor Swift, a Musician, from United States.

Who has more followers? Type 'A' or 'B': A

You're right! Current score: 1
```

The game continues until the player makes an incorrect guess.

```text
Sorry, that's wrong. Final score: 3.
Do you want to play again? Type 'y' or 'n':
```

## 🔄 Replay Feature

After the game ends, the player is asked:

```text
Do you want to play again? Type 'y' or 'n':
```

If the player chooses `y`, `play_game()` is called again and a **new game starts with a score of 0**.

If the player chooses `n`, the program exits.

## 🚀 Future Improvements

Possible improvements for the project:

* Add input validation for invalid guesses
* Add difficulty levels
* Add high-score tracking
* Add more account data
* Add graphical user interface
* Add sound effects
* Store high scores permanently

## 👨‍💻 Author

**Omkar Narlawar**

Computer Engineering Student
Interested in Software Development and Programming.

## 📄 License

This project is created for **learning and educational purposes**.
