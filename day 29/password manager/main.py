from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt","a") as data_file:
        data_file.write(f"{website} , {email} , {password}\n")
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

generate_password_button =  Button(text="Generate Password")
generate_password_button.grid(column=1, row=3, columnspan=2, sticky="e")
add_button = Button(text="Add",width=38,command=save)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()