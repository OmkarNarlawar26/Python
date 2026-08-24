# 🐢 Turtle Racing Game

A simple **Turtle Racing Game** built using Python's `turtle` graphics module.

The player selects a turtle color before the race starts, and six colored turtles compete by moving forward a random distance on every turn. When one turtle reaches the finish line, the game announces whether the player's prediction was correct.

## 🎮 Features

* 🐢 Six turtles with different colors
* 🎯 Player can bet on the winning turtle
* 🏁 Random movement for each turtle
* 🏆 Automatically detects the winning turtle
* ✅ Displays whether the player won or lost
* 🖥️ Uses Python Turtle Graphics for visualization

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**
* **Random module**

## 📁 Project Structure

```text
Turtle-Racing-Game/
│
├── main.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project

Open the project folder in **PyCharm**, **VS Code**, or any Python IDE.

### 3. Run the program

```bash
python main.py
```

A window will open and ask you to choose a turtle color.

## 🎯 How to Play

When the game starts, a dialog box asks:

```text
Which turtle will win the race?
Enter a colour:
red, orange, yellow, green, blue, purple
```

Enter one of the available colors.

The six turtles will then race toward the finish line.

The first turtle to cross the finish line wins.

### Example

If you enter:

```text
blue
```

and the blue turtle wins, the program displays:

```text
You have WON! The blue turtle is the winner.
```

If another turtle wins:

```text
You have LOST! The red turtle is the winner.
```

## 🧠 How It Works

### 1. Create the turtles

Six turtles are created using a loop:

```python
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
```

Each turtle receives a different color and starting position.

### 2. Random movement

During the race, every turtle moves a random distance:

```python
random_distance = random.randint(0, 10)
turtle.forward(random_distance)
```

This makes every race unpredictable.

### 3. Detect the winner

The program checks whether a turtle has crossed the finish line:

```python
if turtle.xcor() > 230:
```

The turtle that reaches this position first is declared the winner.

### 4. Check the player's prediction

The winning turtle's color is compared with the user's bet:

```python
if winning_color == user_bet:
```

The program then prints either a **WIN** or **LOSS** message.

## 📌 Turtle Colors

The available turtles are:

* 🔴 Red
* 🟠 Orange
* 🟡 Yellow
* 🟢 Green
* 🔵 Blue
* 🟣 Purple

## 📚 Concepts Practiced

This project helps practice:

* Python variables
* Lists
* `for` loops
* `while` loops
* Functions and modules
* Random number generation
* Object-oriented usage of the Turtle module
* User input with `textinput()`
* Conditional statements
* Comparing values
* Working with coordinates

## 👨‍💻 Author

**Omkar Narlawar**

---

⭐ If you found this project useful, consider giving the repository a star!
