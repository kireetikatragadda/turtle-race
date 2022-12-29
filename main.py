from turtle import Turtle,Screen
import random

is_race_on = False
red = Turtle()
orange = Turtle()
indigo = Turtle()
green = Turtle()
blue = Turtle()
violet = Turtle()
yellow = Turtle()
#######
turtles_list = [red,orange,indigo,green,blue,violet,yellow]
colors = ["red","orange","indigo","green","blue","violet","yellow"]
screen = Screen()
screen.setup(500,400)
#user_bet
user_bet = screen.textinput("turtle race", "which color tuurtle will win the race?:",)
if user_bet:
    is_race_on = True




x = -230
y = -90
number =0
for i in turtles_list:
    i.shape("turtle")
    i.penup()
    i.goto(x,y)
    y += 30
    i.color(colors[number])
    number += 1
#moving turtles
while is_race_on:
    for i in turtles_list:
        i.forward(random.randint(10,30))
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"you have won.{winning_color} turle won the race")
            else:
                print(f"you have lost.{winning_color} turtle won the race")















screen.exitonclick()
