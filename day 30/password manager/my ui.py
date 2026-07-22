from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="lightblue")

#LOGO
canvas = Canvas(width=400, height=400, bg="lightblue", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image= logo_img, anchor = "center")
canvas.grid(column=1, row=0, pady=10)

#WEBSITE
website_label = Label(window,text="Website",font=("Arial", 15) ,bg = "lightblue", fg="black", highlightthickness=0)
website_label.grid(column=0, row=1, sticky="e", padx=5, pady=5)
website_entry = Entry(window, width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w", padx=5, pady=5)
#EMAIL
email_label = Label(window,text="Email",font=("Arial", 15) ,bg = "lightblue", fg="black", highlightthickness=0)
email_label.grid(column=0, row=2, sticky="e", padx=5, pady=5)
email_entry = Entry(window, width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w", padx=5, pady=5)
#PASSWORD
password_label = Label(window, text="Password:", font=("Arial", 15), bg="lightblue")
password_label.grid(column=0, row=3, sticky="e", padx=5, pady=5)
password_entry = Entry(window, width=21)
password_entry.grid(column=1, row=3, sticky="w", padx=5, pady=5)
password_button = Button(text="Generate Password", font=("Arial", 13),bg="beige")
password_button.grid(column=2, row=3, sticky="w", padx=5, pady=5)
#ADD
add_button = Button(text= "Add",font=("Arial", 13) ,bg = "beige", fg="black", highlightthickness=0, width=36)
add_button.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()