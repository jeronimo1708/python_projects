from tkinter import * 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):

        self.quiz = quiz

        # UI Setup
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)        

        # Score Label
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Canvas question text
        self.question_text = self.canvas.create_text(150, 120, text="Question Text", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)

        # True button
        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=lambda: self.check_answer("True"))
        self.true_button.grid(row=2, column=0)

        # False button
        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, command=lambda: self.check_answer("False"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        # the main loop
        self.window.mainloop() 

    def get_next_question(self):
        '''This function will display the next question in the UI'''
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():            
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())            
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Complete\nYou got {self.quiz.score} out of {len(self.quiz.question_list)} right")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def check_answer(self, true_or_false):
        '''This function check if the answer is correct and provide feedback to the user'''
        true_or_false = self.quiz.check_answer(true_or_false)
        if true_or_false:            
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
            self.score_label.config(text=f"Score : {str(self.quiz.score)}")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
            

