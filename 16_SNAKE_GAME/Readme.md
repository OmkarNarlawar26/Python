# 🐍 Snake Game

A classic **Snake Game built using Python's Turtle graphics module**.

The player controls a snake that moves around the game window, eats randomly positioned food, grows in length, and increases the score. The game ends when the snake collides with the wall or with its own tail.

---

## 📌 Project Overview

This project is a simple implementation of the classic Snake Game using **Python** and the built-in **Turtle graphics library**.

The project is organized into separate Python files to keep the code modular and easy to understand.

The game window is set to **600 × 600 pixels** with a black background, and the game uses keyboard arrow keys for controlling the snake.

---

## ✨ Features

* 🐍 Classic Snake gameplay
* ⬆️⬇️⬅️➡️ Arrow-key controls
* 🍎 Randomly generated food
* 📈 Score tracking
* 🐍 Snake grows after eating food
* 💥 Wall collision detection
* 💥 Snake tail collision detection
* 🎮 Game Over message
* 🖥️ Simple graphical interface using Turtle

---

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Object-Oriented Programming**
* **Random module**
* **Time module**

No external packages are required because the project uses Python's built-in libraries.

---

## 📂 Project Structure

```text
Snake-Game/
│
├── Main.py
├── snake.py
├── food.py
├── scoreboard.py
└── README.md
```

### `Main.py`

The main game controller.

It:

* Creates the game window
* Creates the Snake, Food, and Scoreboard objects
* Handles keyboard controls
* Runs the main game loop
* Detects food collisions
* Detects wall collisions
* Detects tail collisions
* Ends the game when a collision occurs

The main game loop moves the snake continuously and checks for collisions.

### `snake.py`

Contains the `Snake` class.

The snake:

* Starts with three segments
* Uses square Turtle objects
* Moves continuously
* Changes direction using arrow keys
* Grows when food is eaten

The initial snake consists of three segments positioned at `(0,0)`, `(-20,0)`, and `(-40,0)`.

The movement system updates each segment based on the position of the segment in front of it, while the head moves forward by a fixed distance.

### `food.py`

Contains the `Food` class.

The food:

* Appears as a small yellow circle
* Is positioned randomly on the screen
* Moves to a new random location whenever the snake eats it

The food position is randomly generated between `-280` and `280` on both the X and Y axes.

### `scoreboard.py`

Contains the `Scoreboard` class.

It:

* Displays the current score
* Increases the score after eating food
* Displays `GAME OVER!` when the game ends

The initial score is `0`, and the scoreboard is displayed at the top of the game window.

---

## 🎮 How to Play

### Controls

| Key            | Action     |
| -------------- | ---------- |
| ⬆️ Up Arrow    | Move Up    |
| ⬇️ Down Arrow  | Move Down  |
| ⬅️ Left Arrow  | Move Left  |
| ➡️ Right Arrow | Move Right |

The game registers the four arrow keys as controls for changing the snake's direction.

---

## 🕹️ Game Rules

1. The snake starts with three segments.
2. The snake continuously moves forward.
3. Use the arrow keys to change direction.
4. When the snake touches the food:

   * The food moves to a new random position.
   * The snake grows by one segment.
   * The score increases by 1.
5. The game ends if:

   * The snake hits the wall.
   * The snake collides with its own tail.

The food collision logic is handled in `Main.py`, where the snake is extended and the score is increased after eating food.

---

## 🚀 How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

You can check your Python version using:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

### 3. Open the Project

```bash
cd Snake-Game
```

### 4. Run the Game

```bash
python Main.py
```

The Snake Game window will open.

---

## 🧠 Concepts Practiced

This project helped practice several important Python concepts:

* Classes and Objects
* Object-Oriented Programming
* Inheritance
* Functions and Methods
* Lists
* Loops
* Conditional Statements
* Keyboard Event Handling
* Collision Detection
* Random Number Generation
* Python Modules
* Code Organization
* Turtle Graphics

---

## 🏗️ Program Architecture

The project follows a simple modular structure:

```text
                 ┌───────────────┐
                 │    Main.py    │
                 │ Game Controller│
                 └───────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
   ┌────────────┐ ┌────────────┐ ┌──────────────┐
   │  snake.py  │ │  food.py   │ │ scoreboard.py│
   │    Snake   │ │    Food    │ │  Scoreboard  │
   └────────────┘ └────────────┘ └──────────────┘
```

`Main.py` coordinates the three main components of the game.

---

## 📸 Game Features

The game provides:

* A black game window
* White snake segments
* Yellow food
* Score displayed at the top
* Real-time snake movement
* Game-over detection

---

## 📚 What I Learned

Through this project, I practiced building a complete interactive Python application using multiple modules.

The project particularly helped me understand how to:

* Break a program into multiple files
* Create reusable classes
* Use inheritance with the Turtle class
* Manage objects through lists
* Handle keyboard events
* Implement a continuous game loop
* Detect collisions between objects
* Update a graphical scoreboard

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* Add increasing difficulty
* Add a high-score system
* Add different levels
* Add sound effects
* Add a start/restart screen
* Add pause functionality
* Add a game-over restart option
* Add better food placement to avoid spawning directly on the snake
* Add a maximum score/high-score display

---

## 👨‍💻 Author

**Omkar Narlawar**

---

## ⭐ Acknowledgement

This project was created as a Python practice project to understand **Object-Oriented Programming, Turtle Graphics, game loops, keyboard controls, and collision detection**.

If you found this project useful, consider giving the repository a ⭐.
