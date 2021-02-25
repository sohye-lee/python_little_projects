from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_ready = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enther the color \n(red, orange, yellow, green, blue, purple: ")
colors = ["red","orange","yellow","green","blue","navy","purple"]
y_positions = [-120, -80, -40, 0, 40, 80, 120]
turtles = []

if user_bet:
    is_ready = True

for index in range(0,7):
    t = Turtle(shape="turtle")
    t.pensize(40)
    t.penup()
    t.color(colors[index])
    t.goto(x=-230, y=y_positions[index])
    turtles.append(t)


while is_ready:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_ready = False
            winner = turtle.pencolor()
            if winner == user_bet:
                # screen.
                print(f"You've won! the {winner} turtle in.")
            else:
                print(f"You've lost the bet! The winner is {winner}!")

        distance = random.randint(0, 15)
        turtle.forward(distance)

screen.exitonclick()

# def move_forwards():
#     t.forward(10)
#
# def move_backwards():
#     t.backward(10)
#
# def move_clockwise():
#     t.right(10)
#
# def move_counterclock():
#     new_heading = t.heading() + 10
#     t.penup()
#     t.setheading(new_heading)
#     t.pendown()
#
# def clear():
#     t.clear()
#     t.home()
#
# def drawing():
#     screen.onkey(move_forwards, "w")
#     screen.onkey(move_backwards, "s")
#     screen.onkey(move_clockwise, "a")
#     screen.onkey(key="d", fun=move_counterclock)
#     screen.onkey(key="c", fun=clear)
#
# screen.listen()
# drawing()
# screen.exitonclick()