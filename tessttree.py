import turtle as t  
from turtle import *
import random as r
import time

n = 100.0

screen = Screen()
screen.register_shape("D:/img2GIF1.gif")


t.hideturtle()
speed("fastest") 
screensize(bg='skyblue')  
left(90)
forward(3 * n)
color("orange", "yellow")  
begin_fill()
left(126)

for i in range(5):  
    forward(n / 5)
    right(144)  
    forward(n / 5)
    left(72)  
end_fill()
right(126)


def drawlight():  
    if r.randint(0, 30) == 0:  
        color('tomato')  
        circle(6)  
    elif r.randint(0, 30) == 1:
        color('orange')  
        circle(3)  
    else:
        color('dark green')  


color("dark green")  
backward(n * 4.8)


def tree(d, s): 
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


# tree(15, n)
# backward(n / 3)

for i in range(10):  
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red") 
t.write("Merry Christmas ", align="center", font=("Comic Sans MS", 40, "bold"))  


def move_snowflakes():
    for flake in snowflakes:
        flake.sety(flake.ycor() - 5) 
        # Move the snowflake down by 1

    # After moving all the snowflakes, redraw the screen and set up the next call to this function
    screen.update()
    screen.ontimer(move_snowflakes, 5)  # Call this function every 10 ms

# Create a list of snowflakes (i.e., turtle objects)
snowflakes = [t.Turtle() for _ in range(100)]

# Set up each snowflake
    
for flake in snowflakes:
    flake.shape("D:/img2GIF1.gif")
    flake.penup()
    flake.shapesize(0.1, 0.1) 
    flake.color('white')
    flake.speed('fastest')
    flake.goto(r.randint(-350, 350), r.randint(-100, 350))  

# Start moving the snowflakes
move_snowflakes()

# Keep the window open
t.done()