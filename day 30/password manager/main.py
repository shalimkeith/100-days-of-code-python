import json
from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                email:email,
                password:password
            }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error","Email or Password are Empty")
    else:
        with open("data.json","r") as data_file:
            # reading old data
            data = json.load(data_file)
            # updating new data
            data.update(new_data)

        with open("data.json","w") as data_file:
            # saving new data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="lightblue")

#LOGO
canvas = Canvas(width=200, height=200, bg="lightblue", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img, anchor = "center")
canvas.grid(column=1, row=0)


#labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1,columnspan=2,sticky=W)
website_entry.focus_set()


email_entry = Entry(width=45)
email_entry.grid(column=1, row=2,columnspan=2,sticky=W)
email_entry.insert(0,"hellothere@gmail.com")

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3,sticky=W)


#Buttons

generate_password_button =  Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=1, row=3, columnspan=2, sticky="e")
add_button = Button(text="Add",width=38,command=save)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()