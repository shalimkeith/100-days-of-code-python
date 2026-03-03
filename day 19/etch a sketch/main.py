from turtle import Turtle,Screen

men = Turtle()
screen = Screen()

def move_forward():
    men.forward(10)

def move_backward():
    men.backward(10)

def turn_right():
    new_heading = men.heading() - 10
    men.setheading(new_heading)

def turn_left():
    new_heading = men.heading() + 10
    men.setheading(new_heading)

def clear():
    men.clear()
    men.penup()
    men.home()
    men.pendown()

screen.listen()

screen.onkey(move_forward , "w")
screen.onkey(move_backward , "s")
screen.onkey(turn_left , "a")
screen.onkey(turn_right , "d")
screen.onkey(clear , "c")
screen.exitonclick()