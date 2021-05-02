from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


# ----------------------
# ------ PASSWORD GENERATOR ------------------------------- #

# ---------------------------- Generate Unique Password ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- Delete Entries from the entry box  ------------------------------- #
def delete_entries():
    entry_email.delete(0, END)
    entry_website.delete(0, END)
    entry_password.delete(0, END)


# ---------------------------- SAVE ACCOUNT DATA ------------------------------- #
def write_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        try:
            with open("logs.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("logs.json", "w") as file:
                # Create the data file and store data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("logs.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            delete_entries()


# ---------------------------- Find Password for Saved Account ------------------------------- #
def find_password():
    try:
        with open("logs.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        website = entry_website.get()
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Website:  {website} \n"
                f"Email:    {email} \n"
                f"Password: {password}",
            )
        else:
            messagebox.showinfo(
                title=website,
                message=f"No details for the website named '{website}' exists.",
            )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
label_website = Label(text="Website: ")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username: ")
label_email.grid(row=2, column=0)

label_password = Label(text="Password: ")
label_password.grid(row=3, column=0)

label_info = Label(
    text="[Note: Generating a password automatically copies it to your clipboard.]",
    pady=20,
)
label_info.grid(row=5, column=1, columnspan=3, sticky=W)

# Entries
entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(row=1, column=1, sticky=W)

entry_email = Entry(width=57)
entry_email.grid(row=2, column=1, columnspan=2, sticky=W)

entry_password = Entry(width=35)
entry_password.grid(row=3, column=1, sticky=W)

# Buttons
button_generate = Button(text="Generate Password", width=20, command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Save", width=58, command=write_data)
button_add.grid(row=4, column=1, columnspan=2, sticky=W)

button_search = Button(text="Search", width=20, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()
