# from turtle import Turtle

# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# from turtle import *

# tom.backward(100)
# terry.forward(100)
# tim.setheading(90)
# tim.forward(100)

# import turtle as t
#
# tim = t.Turtle()

# import heroes
#
# print(heroes.gen())

# from turtle import Turtle,Screen
#
# timberly = Turtle()
# screen = Screen()
#
# for _ in range(10):
#     timberly.pendown()
#     timberly.forward(10)
#     timberly.penup()
#     timberly.forward(10)
#
# screen.exitonclick()

from turtle import Turtle,Screen
import random


jason = Turtle()
screen = Screen()
#
# jason.forward(100)
# jason.right(120)
# jason.forward(100)
# jason.right(120)
# jason.forward(100)
# jason.right(120)
# jason.forward(100)
# jason.right(90)
# jason.forward(100)
# jason.right(90)
# jason.forward(100)
# jason.right(90)
# jason.forward(100)
# jason.right(90)
# jason.forward(100)
# jason.right(72)
# jason.forward(100)
# jason.right(72)
# jason.forward(100)
# jason.right(72)
# jason.forward(100)
# jason.right(72)
# jason.forward(100)
# jason.right(72)
# jason.forward(100)
# jason.right(60)
# jason.forward(100)
# jason.right(60)
# jason.forward(100)
# jason.right(60)
# jason.forward(100)
# jason.right(60)
# jason.forward(100)
# jason.right(60)
# jason.forward(100)
# jason.right(60)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(51.42)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(45)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(40)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)
# jason.right(36)
# jason.forward(100)

colours = [
"gold", "silver", "maroon", "navy",
 "teal", "indigo", "violet","red", "blue", "green", "yellow", "black",
"orange", "purple"
]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        jason.forward(100)
        jason.right(angle)

for shape_side_n in range(3,11):
    jason.color(random.choice(colours))
    draw_shape(shape_side_n)
