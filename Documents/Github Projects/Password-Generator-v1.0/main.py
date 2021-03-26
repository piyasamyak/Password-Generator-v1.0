from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ----------------------
# ------ PASSWORD GENERATOR ------------------------------- #
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

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_entries():
    entry_email.delete(0, END)
    entry_website.delete(0, END)
    entry_password.delete(0, END)


# Write the data to a text file
def write_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        dataset = website + " | " + email + " | " + password + '\n'
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} "
                                               f"\nIs it ok to save?")
        if is_ok:
            with open('logs.txt', 'a') as file:
                file.writelines(dataset)
            delete_entries()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
label_website = Label(text="Website: ")
label_website.grid(row=1, column=0, sticky=W)

label_email = Label(text="Email/Username: ")
label_email.grid(row=2, column=0, sticky=W)

label_password = Label(text="Password: ")
label_password.grid(row=3, column=0, sticky=W)

label_info = Label(text="[Note: Generating a password automatically copies the password to your clipboard.]", pady=20)
label_info.grid(row=4, column=0, columnspan=3)

# Entries
entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2, sticky=W)

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2, sticky=W)

entry_password = Entry(width=35)
entry_password.grid(row=3, column=1, columnspan=2, sticky=W)

# Buttons
button_generate = Button(text="Generate Password", width=35, command=generate_password)
button_generate.grid(row=5, column=0, sticky=W)

button_add = Button(text="Add", width=35, command=write_data)
button_add.grid(row=5, column=1, sticky=E)

window.mainloop()
