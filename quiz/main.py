import os
import sys
import requests

from data import question_data
from questions import QuestionItem

questions = []
score = 0
game_on = True
answer_mapping = {"t": "True", "f": "False"}

for question in question_data:
    questions.append(QuestionItem(question["question"]["text"], question["correctAnswer"], question["incorrectAnswers"]))


while True:
    for idx, question in enumerate(questions):
        user_input = ""
        answer_mapping = {}
        for index, answer in enumerate(question.choices):
            answer_mapping[str(index + 1)] = answer

        while user_input not in ("1", "2", "3", "4"):
            user_input = input(f'Q.{idx+1}: {question.question}\n1:{answer_mapping["1"]}\n2:{answer_mapping["2"]}\n3:{answer_mapping["3"]}\n4:{answer_mapping["4"]}\n(1, 2, 3 or 4)')

        if answer_mapping[user_input] == question.answer:
            score += 1
            print(f"That is correct. Current score is {score}/{idx+1}")
        else:
            print(f"Incorrect answer. Correct answer is {question.answer}. Score is {score}/{idx+1}")

    print(f"Your final score is {score}")
    play_on = ""
    while play_on not in ("y", "n"):
        play_on = input("Do you want to play again? (y/n)").lower()
    if play_on == "n":
        sys.exit()

    os.system("clear")
