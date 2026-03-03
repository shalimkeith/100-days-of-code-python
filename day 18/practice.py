import turtle as t
import random

tim = t.Turtle()

colours = [
"gold", "silver", "maroon", "navy",
 "teal", "indigo", "violet","red", "blue", "green", "yellow", "black",
"orange", "purple"
]

directions = [0,90,180,270]
tim.speed(19)
tim.pensize(14)

for _ in range(300):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


