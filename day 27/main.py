import tkinter

window = tkinter.Tk()

window.title("My First GUI")
window.minsize(400, 500)

#label

my_label = tkinter.Label(text="I am a label made by Keith.", font=("Times new roman", 25))
my_label.pack()



window.mainloop()
import turtle

tim = turtle.Turtle()

tim.write("provided by Keith", font=("Times new roman", 25, "bold"))

