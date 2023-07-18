import tkinter
import math
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

TIMER_ON = False
# TO DO: Add support for user to control reps.
# Right now the timer will run twice
REPS = 1
CHECKMARK = "✔" 
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(padx=10, fg=GREEN, bg=YELLOW, text="Timer")
    checkmark_label.config(text = "")
    global REPS
    REPS = 1



# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    ''' This fucntion starts the timer. It will call the countdowns for work, short break and long break'''
    global REPS
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(padx=10, fg=RED, bg=YELLOW, text="BREAK")
        countdown(5)
        REPS += 1
    elif REPS % 2 == 0:
        timer_label.config(padx=10, fg=PINK, bg=YELLOW, text="BREAK")
        countdown(3)
        REPS += 1
    else:
        timer_label.config(padx=10, fg=GREEN, bg=YELLOW, text="WORK")
        countdown(10)
        REPS += 1


def calculate_minutes_and_seconds(seconds):
    ''' This function calculates minutes and seconds from seconds and returns them'''
    minutes = math.floor(seconds / 60)
    if minutes < 10:
        minutes = f"0{str(minutes)}"
    seconds = seconds % 60
    if seconds < 10:
        seconds = f"0{str(seconds)}"

    return minutes, seconds


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(time_label):
    """This function is the countdown function. When the start button is clicked, the pomodoro timer starts using this function"""
    global timer
    # Get minutes and seconds for the countdown
    minutes, seconds = calculate_minutes_and_seconds(time_label)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time_label > 0:
        timer = window.after(1000, countdown, time_label - 1)
    else:        
        start_timer()
        # add_checkmark_after_work()
        

# TO DO: Correct this function and add it in the countdown function to display checkmarks on completion of work
def add_checkmark_after_work():
    '''This fucntion adds a checkmark when one work session is completed'''
    global REPS
    marks = ""
    work_session = math.floor(REPS % 2)
    print(work_session)
    for i in range(work_session):        
        marks += CHECKMARK
        checkmark_label.config(text = marks)




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
# Store canvas text in variable to use it later in countdown function
timer_text = canvas.create_text(
    100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
# pack, grid puts things on the UI
canvas.grid(row=1, column=1)

# start button
start_button = tkinter.Button(
    text="Start", bg=YELLOW, highlightthickness=0, command=start_timer
)
start_button.grid(row=2, column=0)

# reset button
reset_button = tkinter.Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmarks
checkmark_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmark_label.grid(row=3, column=1)

# This has to run at the end of the program
window.mainloop()
