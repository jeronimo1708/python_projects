from tkinter import *

window = Tk()
window.title("Tkinter program")
window.minsize(width=500, height=300)

def button_click():
    entry_text = entry.get()
    label.config(text=entry_text)


label = Label(text="This is some text", font=("Arial", 24, "bold"))
label.pack()

button = Button(text="Click Me", command=button_click)
button.pack()

entry = Entry()
entry.pack()


window.mainloop()
