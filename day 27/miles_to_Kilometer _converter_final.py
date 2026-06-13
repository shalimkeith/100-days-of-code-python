from tkinter import *

def miles_to_kilometers():
    try:
        miles = float(miles_input.get())
        kilometers = miles * 1.609
        kilometers_result_label.config(text=f"{kilometers:.2f}")
    except ValueError:
        kilometers_result_label.config(text="Invalid input")

window = Tk()
window.title("Miles To Kilometers Converter")

miles_input = Entry()
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is Equal")
is_equal_label.grid(column=0, row=1)

kilometers_result_label = Label(text="0")
kilometers_result_label.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()