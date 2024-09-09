from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WHITE = "#FFFFFF"
BLACK = "#000000"

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

    password = "".join(password_list)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(username) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="title", message=f"Please don't leave the fields empty.")

    else:
        is_ok = messagebox.showinfo(title="title", message=f"These are the details they entered \n Email:{username} \n "
                                                   f"Website:{website} \n Password: {password} \n Is it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n ")
                website_entry.delete(0,"end")
                username_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)


# Canvas
canvas = Canvas(background=WHITE, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:", background=WHITE)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username", background=WHITE)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", background=WHITE)
password_label.grid(column=0, row=3)
# Entry
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "tsering@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=add)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()