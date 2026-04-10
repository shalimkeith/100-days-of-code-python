import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)}/ 50 States correct", prompt = "What's another state's name? ").title()
    print(answer_state)

    #if answer_state is one of state in all of the states
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)




turtle.mainloop()