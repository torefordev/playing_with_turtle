from turtle import Turtle, Screen
from random import randint,choice

leo = Turtle()

screen = Screen()
screen.colormode(255)
leo.speed(0)

def randomRGB():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

def draw_spirograf(steps):
    for _ in range(steps):
        leo.color(randomRGB())
        leo.circle(150)
        leo.setheading(leo.heading() + 360/steps)
draw_spirograf(30)

def random_Walk(steps,distance):
    leo.pensize(5)
    direction_angles = [0,90,180,270]
    for _ in range(steps):
        leo.color(randomRGB())
        leo.right(choice(direction_angles))
        leo.forward(distance)
random_Walk(50,25)

def shape(turtle, corner, distance, direction):
    angle = 180-((corner-2)/corner *180)
    turtle.pencolor(randomRGB())
    for _ in range(corner):
        if direction == "f":
            turtle.forward(distance)
            turtle.right(angle)
        elif direction == "b":
            turtle.forward(distance)
            turtle.left(angle)
for i in range(3,11):
    shape(leo,i,100,"f")

screen.exitonclick()