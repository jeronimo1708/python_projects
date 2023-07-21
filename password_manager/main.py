from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry_box.grid(row=2, column=2, columnspan=2)

# Email/Username label
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)

# Email/Username entry box
email_entry_box = Entry(width=40)
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
add_button = Button(text="Add", width=37)
add_button.grid(row=5, column=2, columnspan=2)



window.mainloop()