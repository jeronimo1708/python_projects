from flask import Flask
import random
from art import logo

app = Flask(__name__)

NUMBER = random.randint(0, 9)
print(NUMBER)

# def make_h1(func):
#     def wrapper():
#         h1 = func()
#         return f"<h1>{h1}</h1>"
#     return wrapper
    
# './media/guess_number.webp'
@app.route('/')
# @make_h1
def home():
    return "<h1>Guess the number between 0 and 9</h1><br>" \
    "<br>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<int:num>")
def guessed_num(num):
    if num == NUMBER:
        return "<h1 style='color:green'>You are right<br>" \
    "<br>" \
    "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"
    elif num > NUMBER:
        return "<h1 style='color:red'>Thats not right<br>" \
    "<br>" \
    "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif num < NUMBER:
        return "<h1 style='color:red'>Thats not right<br>" \
    "<br>" \
    "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"





if __name__ == '__main__':
    app.run(debug=True)