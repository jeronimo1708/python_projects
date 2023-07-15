import tkinter
from time import sleep

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(t = 25):
    while t:
        mins, secs = divmod(25, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer text
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 30, "bold"))
timer_label.config(padx=10, fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# The clock
# getting the image using PhotoImage
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 95, image=tomato_image)
canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# pack, grid puts things on the UI
canvas.grid(row=1, column=1)

# start button
start_button = tkinter.Button(text="Start", bg=YELLOW, highlightthickness=0, command=countdown)
start_button.grid(row=2, column=0)

# reset button
reset_button = tkinter.Button(text="Reset", bg=YELLOW, highlightthickness=0)
reset_button.grid(row=2, column=2)

# Checkmarks
checkmark_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmark_label.grid(row=3, column=1)

# This has to run at the end of the program
window.mainloop()

