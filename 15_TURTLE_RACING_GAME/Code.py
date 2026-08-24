from turtle import Turtle, Screen
import random

is_racr_on = False
screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make yout bet", prompt="Which turtle will win the race? Enter a colour : (red, orange, yellow, green, blue, purple)")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")

    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])

    all_turtle.append(new_turtle)

if user_bet:
    is_racr_on = True

while is_racr_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
                is_racr_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You have WON! The {winning_color} turtle is the winner.")
                else:
                    print(f"You have LOST! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()