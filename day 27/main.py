from tkinter import *



window = Tk()

window.title("My First GUI")
window.minsize(width=400,height= 500)

input = Entry(width=30)
input.pack()

# Button function
def button_clicked():
    new_text = input.get()
    print(new_text)
    my_label.config(text=new_text)

#label

# my_label = Label(text="I am a label made by Keith.", font=("Times new roman", 12))
# my_label.config(text="My first GUI")
# my_label.place(x=0, y=0)

# def button_clicked():
#     new_text = input.get()
#     print(input.get())
#     my_label.config(text= new_text )
#
# button = Button(text = "Click me!", command = button_clicked)
# button.pack(side = BOTTOM)

# input = Entry(width= 30)
# input.pack()
# print(input.get())

my_label = Label(text="I am a label made by Keith.", font=("Times new roman", 12, "bold"))
my_label.config(text="My first GUI")
my_label.place(x=0, y=0)

button = Button(text="Click me!", command=button_clicked)

input = Entry(width= 30)
print(input.get())

window.mainloop()