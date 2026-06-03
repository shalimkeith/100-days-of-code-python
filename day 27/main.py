from tkinter import *

window = Tk()

window.title("My First GUI")
window.minsize(400, 500)

#label

my_label = Label(text="I am a label made by Keith.", font=("Times new roman", 25))
my_label.pack()

def button_clicked():
    new_text = input.get()
    print(input.get())
    my_label.config(text= new_text )

button = Button(text = "Click me!", command = button_clicked)
button.pack()

input = Entry(width= 30)
input.pack()
print(input.get())

window.mainloop()

