from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI")
window.minsize(width=400, height=500)
window.config(padx=20, pady=20)


my_label = Label(text="My First GUI", font=("Arial", 25,"bold") )
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="Logical", command=button_clicked)
button.grid(column=2, row=0)

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
