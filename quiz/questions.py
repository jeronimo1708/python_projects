class QuestionItem:
    def __init__(self, question, answer, choices) -> None:
        self.question = question
        self.answer = answer
        self.choices = choices
        self.choices.append(answer)
        