from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=350, height=100)
window.config(padx=20, pady=20)

# User can input miles here
miles_entry = Entry(text="0", width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("System", 15))
miles_label.config(padx=10)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("System", 15))
is_equal_to_label.config(padx=10)
is_equal_to_label.grid(column=0, row=1)

# Result is shown here
km_result_label = Label(text="0", font=("System", 15))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("System", 15))
km_label.config(padx=10)
km_label.grid(column=2, row=1)

# Result calculation function
def convert_to_km():
    ''' This function converts miles inputed by the user to kilometers'''
    miles = int(miles_entry.get())
    km = round(miles * 1.60934, 3)
    km_result_label.config(text=f"{str(km)}")

# This button triggers the function
calculate_button = Button(text="Calculate", command=convert_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
