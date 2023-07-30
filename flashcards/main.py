import json
import random
from time import sleep
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE = "./data/french_words.json"
DATA = None

correct_words = set()
incorrect_words = []

current_language_word = None
current_english_word = None

language_to_english_flag = False


# -------------------- Read data on startup --------------------#

def read_data():
    """Return a dictionary read from the JSON data file which has the
    language as key and the values of that is key value pairs of the
    words in that language and its English meaning"""
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
    return data

# Get the data from DATA FILE on start up
DATA = read_data()


# -------------------- Load words on the card --------------------#

def start_process(button_name):
    '''Starts the process whenever the user clicks on the yes or no buttons'''
    if button_name == "yes":
        current_language_word, current_english_word = next_card("french", DATA)
        DATA["french"].pop(current_language_word)
        with open("./data/to_learn.json", "w") as file:
            json.dump(DATA, file)
    elif button_name == "no":
        next_card("french", DATA)


def next_card(language, data):
    '''Creates a key:value pair of the language and it english traslations'''
    global current_language_word, current_english_word, flip_timer, language_to_english_flag  

    language_to_english_flag = True
    window.after_cancel(flip_timer)
    words = data[language]
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(front_card_title_text, text=language, fill='black')
    current_language_word, current_english_word = random.choice(list(words.items()))
    canvas.itemconfig(front_card_word_text, text=current_language_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)
    return current_language_word, current_english_word
    

def flip_card():
    '''This function flips the card and displays the english meaning of the word'''    
    global language_to_english_flag

    # Set the background title text to english
    canvas.itemconfig(front_card_title_text, text="Language", fill="white")
    
    if language_to_english_flag:        
        canvas.itemconfig(front_card_title_text, text="English", fill="white")
    # Back of the Card  
    # Set the image of the card background to show the back of the card image  
    canvas.itemconfig(card_background, image=card_back_image)
    
    # Set the background word to the english meaning of the language word
    canvas.itemconfig(front_card_word_text, text=current_english_word, fill="white")

        

# -------------------- UI SETUP --------------------#

window = Tk()
window.title("Learn with Flashcards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Card Images
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

# Creating the canvas object
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

# Apply front card image to the canvas background
card_background = canvas.create_image(400, 300, image=card_front_image)

# Front Card Text
front_card_title_text = canvas.create_text(
    400, 150, text="Language", font=("Arial", 40, "italic")
)
front_card_word_text = canvas.create_text(400, 250, text="Word", font=("Arial", 60, "bold"))

# Back of the Card


# placing the canvas on the GRID
canvas.grid(row=0, column=0, columnspan=2)

# Yes Button
yes_button_image = PhotoImage(file="./images/right.png")
button = Button(image=yes_button_image, highlightthickness=0, command=lambda: start_process("yes"))
button.grid(row=1, column=1)

# No Button
no_button_image = PhotoImage(file="./images/wrong.png")
button = Button(image=no_button_image, highlightthickness=0, command=lambda: start_process("no"))
button.grid(row=1, column=0)



# Run the application
window.mainloop()
