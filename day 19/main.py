from turtle import Turtle,Screen

men = Turtle()
screen = Screen()

def move_forward():
    men.forward(10)

screen.listen()
screen.onkey(key = "space",fun = move_forward)
screen.exitonclick()
