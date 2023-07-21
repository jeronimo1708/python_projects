import os 
import sys
from tkinter import *
from tkinter import messagebox

DATA_FILE = "/home/jeronimo/dev/python_projects/password_manager/data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
      



# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_website():
    '''This function fetches the website text the user has entered in the website entry box'''
    return website_entry_box.get()

def get_email():
    '''This function fetches the email text the user has entered in the email entry box'''
    return email_entry_box.get()

def get_password():
    '''This function fetches the password text the user has entered in the password entry box'''
    return password_entry_box.get()

def get_entry_data():
    '''This is a combination of the above functions'''
    website = get_website()
    email = get_email()
    password = get_password()
    return website, email, password    

def write_to_file(mode, website, email, password):
    '''This function writes the data the user has entered to data.csv file in a pipe delimited format'''
    with open(DATA_FILE, mode) as file:
        line = f"{website}|{email}|{password}\n"
        file.write(line)

def clear_text():
    '''This function clears the text from the website and password fields after the user has successfully saved the password to data.csv file''' 
    website_entry_box.delete(0, END)
    password_entry_box.delete(0, END)

def save_password():
    '''This function saves the password to data.csv file'''
    website, email, password = get_entry_data()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:        
        if os.path.isfile(DATA_FILE):
            write_to_file("a", website, email, password)
        else:
            write_to_file("w", website, email, password)
        clear_text()
    
    

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
website_entry_box = Entry(width=40)
website_entry_box.focus()
website_entry_box.grid(row=2, column=2, columnspan=2)

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
generate_password_button = Button(text="Generate", width=12)
generate_password_button.grid(row=4, column=3)

# Add button
add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()