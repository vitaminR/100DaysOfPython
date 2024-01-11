class Question:
    """This class is used to create a question object""" ""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"Question(question={self.question}, answer={self.answer})"
