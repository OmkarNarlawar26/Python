# 🏓 Pong Game

A classic **Pong Game** built using Python's `turtle` graphics module.

This project is a two-player game where players control paddles and try to hit the ball past their opponent. The first player to reach **5 points** wins the game.

## 🎮 Features

* 🏓 Two-player Pong gameplay
* ⚪ Moving ball with automatic bouncing
* 🧱 Ball bounces off the top and bottom walls
* 🎯 Paddle collision detection
* ⚡ Ball speed increases after paddle collisions
* 🛡️ Paddles stay within the game boundaries
* 🏆 First player to reach **5 points** wins
* 📊 Live scoreboard
* 🎉 Winner message displayed directly on the game screen
* 🔄 Ball resets to the center after a player misses

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Time module**

## 📁 Project Structure

```text
Pong-Game/
│
├── Main.py
├── ball.py
├── paddle.py
├── scoreboard.py
└── README.md
```

## 🧩 Project Components

### `Main.py`

The main file that controls the game.

It is responsible for:

* Creating the game window
* Creating both paddles
* Creating the ball
* Creating the scoreboard
* Handling keyboard controls
* Running the game loop
* Detecting wall and paddle collisions
* Detecting when a player misses the ball
* Checking the winning score

### `ball.py`

Contains the `Ball` class.

The ball:

* Is displayed as a white circle
* Moves automatically
* Changes direction when it hits the top or bottom wall
* Changes horizontal direction when it hits a paddle
* Becomes faster after paddle collisions
* Resets to the center when a player loses a point

### `paddle.py`

Contains the `Paddle` class.

The paddles:

* Are displayed as white rectangles
* Can move up and down
* Have movement boundaries so they cannot leave the screen

### `scoreboard.py`

Contains the `Scoreboard` class.

It handles:

* Left player score
* Right player score
* Updating the scoreboard
* Displaying the winner when a player reaches 5 points

## 🎮 Controls

| Player       | Move Up | Move Down |
| ------------ | ------- | --------- |
| Left Player  | `W`     | `S`       |
| Right Player | `↑`     | `↓`       |

## 🏆 Game Rules

1. The game starts with both players at **0 points**.
2. The ball starts from the center.
3. Players move their paddles to hit the ball.
4. If the right player misses the ball, the left player gets **1 point**.
5. If the left player misses the ball, the right player gets **1 point**.
6. The ball resets to the center after a point.
7. The ball becomes faster after successful paddle collisions.
8. The first player to reach **5 points** wins.
9. The winner is displayed on the game screen and the game ends.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project

Open the project in **PyCharm**, **VS Code**, or another Python IDE.

### 3. Run the main file

```bash
python Main.py
```

The Pong game window will open.

## 📚 Python Concepts Practiced

This project helped practice:

* Object-Oriented Programming
* Python Classes and Objects
* Inheritance
* Functions and Methods
* Loops
* Conditional Statements
* Lists and Variables
* Keyboard Event Handling
* Collision Detection
* Coordinate System
* Turtle Graphics
* Game Loops
* Basic Game Logic

## 🖥️ Game Window

The game uses an **800 × 600** Turtle graphics window with a black background.

The scoreboard is displayed at the top, while the paddles and ball are positioned in the playing area.

## 🔮 Future Improvements

Possible improvements for future versions:

* Add a start/restart button
* Add sound effects
* Add a pause button
* Add different difficulty levels
* Add a single-player mode with AI
* Add a main menu
* Add improved visual effects

## 👨‍💻 Author

**Omkar Narlawar**

---

⭐ If you enjoyed this project, consider giving the repository a star!
