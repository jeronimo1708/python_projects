import os
import json
import random
from tkinter import *
from tkinter import messagebox

# TO DO: Save passwords in database instead of using text files
DATA_FILE = "/home/jeronimo/dev/python_projects/password_manager/data.json"
LOWERCASE_LETTERS = [
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
]
UPPERCASE_LETTERS = [
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
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """This function generates a password with
    -> 8 lowercase letters
    -> 2 uppercase letters
    -> 3 numbers
    -> 2 special characters"""
    password = []
    #### TO DO: Change the for loops to list comprehension
    for i in range(8):
        character = LOWERCASE_LETTERS[random.randint(0, 25)]
        password.append(character)
    for i in range(2):
        character = UPPERCASE_LETTERS[random.randint(0, 25)]
        password.append(character)
    for i in range(3):
        character = NUMBERS[random.randint(0, 9)]
        password.append(character)
    for i in range(2):
        character = SYMBOLS[random.randint(0, 8)]
        password.append(character)
    random.shuffle(password)
    strong_password = "".join(password)
    return strong_password


def generate_password_in_entry_box():
    """This function displays the generated password in the password entry box"""
    strong_password = generate_password()
    password_entry_box.delete(0, END)
    password_entry_box.insert(0, strong_password)
    copy_password_to_clipboard(strong_password)


def copy_password_to_clipboard(strong_password):
    """This function copies the password that was generated to the clipboard"""
    window.clipboard_clear()
    window.clipboard_append(strong_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_website():
    """This function fetches the website text the user has entered in the website entry box"""
    return website_entry_box.get()


def get_email():
    """This function fetches the email text the user has entered in the email entry box"""
    return email_entry_box.get()


def get_password():
    """This function fetches the password text the user has entered in the password entry box"""
    return password_entry_box.get()


def get_entry_data():
    """This is a combination of the above functions"""
    website = get_website()
    email = get_email()
    password = get_password()
    return website, email, password


def create_data_for_json(website, email, password):
    data = {website.lower(): {"email": email, "password": password}}
    return data


def read_from_file():
    """This function reads from the data file. If the data file does not exist, then it will create a new one"""
    # try:
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return data
    # except FileNotFoundError:
    #     file = open(DATA_FILE, "w")
    #     file.close()


def write_to_file(website, email, password):
    """This function writes the data the user has entered to data.csv file in a pipe delimited format"""
    with open(DATA_FILE, "w") as file:
        data = create_data_for_json(website, email, password)
        json.dump(data, file)


def update_file(data, website, email, password):
    """This function updates the DATA FILE with new entries"""
    with open(DATA_FILE, "w") as file:
        new_data = create_data_for_json(website, email, password)
        data.update(new_data)
        json.dump(data, file)


def clear_text():
    """This function clears the text from the website and password fields after the user has successfully saved the password to data.csv file"""
    website_entry_box.delete(0, END)
    password_entry_box.delete(0, END)


def validate_input(website, email, password):
    """This function will display the website, email and password in a popup box and ask the user to check if the details are correct"""
    proceed = messagebox.askokcancel(
        title="Validate Input",
        message=f"Please check the input\nWebsite:{website}\nEmail:{email}\nPassword:{password}",
    )
    return proceed


def save_password():
    """This function saves the password to data.json file"""
    website, email, password = get_entry_data()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:
        # TO DO: Add functionality to give the user a chance to check the inputs (DONE)
        proceed = validate_input(website, email, password)
        if proceed:
            try:
                data = read_from_file()
            except FileNotFoundError:
                write_to_file(website, email, password)
            else:
                update_file(data, website, email, password)
            clear_text()
            messagebox.showinfo(
                title="Done", message="Password was saved successfully!"
            )


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #


def search():
    """This fucntion searches for a password in the database. If the password is found, then it copies it to the clipboard and clears the website text"""
    website = get_website()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Website field is empty")
    else:
        try:
            data = read_from_file()
            try:
                website, email, password = (
                    website.capitalize(),
                    data[website.lower()]["email"],
                    data[website.lower()]["password"],
                )
                messagebox.showinfo(
                    title=website, message=f"Email:{email}\nPassword:{password}"
                )
            except KeyError:
                messagebox.showinfo(
                    title="No Website found", message=f"{website}: No password found"
                )
            else:
                copy_password_to_clipboard(password)
                clear_text()
        except FileNotFoundError:
            messagebox.showinfo(
                title="No Website found", message=f"{website}: No password found"
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# setting the canvas with the image
lock_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=1, column=2)

# Website label
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

# Website entry box
website_entry_box = Entry(width=25)
website_entry_box.focus()
website_entry_box.grid(row=2, column=2)

# Email/Username label
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)

# Email/Username entry box
email_entry_box = Entry(width=40)
email_entry_box.insert(0, "dummy@dummy.com")
email_entry_box.grid(row=3, column=2, columnspan=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

# Password entry box
password_entry_box = Entry(width=25)
password_entry_box.grid(row=4, column=2)

# Generate Password button
generate_password_button = Button(
    text="Generate", width=12, command=generate_password_in_entry_box
)
generate_password_button.grid(row=4, column=3)

# Add button
add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(row=5, column=2, columnspan=2)

# Search button
search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=2, column=3)


window.mainloop()
