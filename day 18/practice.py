import turtle as t
import random

tim = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_color = (r, g, b)
    return random_color

colours = [
"gold", "silver", "maroon", "navy",
 "teal", "indigo", "violet","red", "blue", "green", "yellow", "black",
"orange", "purple"
]

directions = [0,90,180,270]
tim.speed(19)
tim.pensize(14)

for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


