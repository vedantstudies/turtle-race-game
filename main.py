from tkinter import messagebox
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? ( Red/Yellow/green/blue/orange) \nEnter a color: ")

if user_bet:
    user_bet = user_bet.lower()
    is_on = True

    colors = ["red", "yellow", "green", "blue", "orange"]
    turtles = []
    yPos = 200

    for i in range(len(colors)):
        tim = Turtle(shape="turtle")
        tim.color(colors[i])
        tim.penup()
        tim.goto(x=-230, y=yPos)
        yPos -= 100
        turtles.append(tim)

    is_on = True

    while is_on:
        for turtle in turtles:
            dist = random.randint(0, 10)
            turtle.forward(distance=dist)

            if turtle.xcor() >= 230:
                winner = turtle.fillcolor()
                is_on = False
                break

    if winner == user_bet:
        res = f"You Won the Bet! {user_bet} turtle won the race!"
    else:
        res = f"You lost the Bet! {winner} turtle won the race!"

    messagebox.showinfo(title="Result", message=res)

screen.bye()
