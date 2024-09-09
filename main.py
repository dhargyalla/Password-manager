from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        website:{
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="title", message=f"Please don't leave the fields empty.")

    else:
        try:
            with open("data.json", "r") as file:
                # loading the old data
                data = json.load(file) # should open in "r" mode

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # updating the old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # saving the updated data
                json.dump(data, file, indent=4) # should open in "W" mode
        finally:
            website_entry.delete(0,"end")
            password_entry.delete(0, "end")

# ---------------------------- FIND PASSWORD FUNCTION ------------------------------- #
def find_password():
    search_key = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if search_key in data:
            username = data[search_key]['username']
            password = data[search_key]['password']
            messagebox.showinfo(title=search_key, message=f"Username: {username}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_key} found.")



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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "tsering@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2,row=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()