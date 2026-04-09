import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")


answer_state = screen.textinput(title = "Guess The State: ", prompt = "What's another state's name? ")
print(answer_state)

#if answer_state is one of state in all of the states




turtle.mainloop()