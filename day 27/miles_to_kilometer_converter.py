from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()

window.title("Miles To Kilometer Converter")
window.minsize(100, 200)
window.config(padx=5, pady=5)


my_label = Label(text="My First GUI", font=("Arial", 12,"bold") )
my_label.config(text="Equal To")
my_label.grid(column=1, row=1)
my_label.config(padx=20, pady=20)

my_label = Label(text="My First GUI", font=("Arial", 12,"bold") )
my_label.config(text="Miles")
my_label.grid(column=3, row=0)
my_label.config(padx=20, pady=20)


input = Entry(width=10)
print(input.get())
input.grid(column=2, row=0)

my_label = Label(text="My First GUI", font=("Arial", 12,"bold") )
my_label.config(text="Equal To")
my_label.grid(column=2, row=1)
my_label.config(padx=20, pady=20)

my_label = Label(text="My First GUI", font=("Arial", 12,"bold") )
my_label.config(text="Km")
my_label.grid(column=3, row=1)
my_label.config(padx=20, pady=20)

button = Button(text="Button", command=button_clicked)
button.grid(column=2, row=2)



window.mainloop()