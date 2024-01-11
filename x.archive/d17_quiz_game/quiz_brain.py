class QuizBrain:
    """handles the logic of the quiz, keeps track of the score and the question number"""

    def __init__(self, ql):
        self.question_number = 0
        self.question_list = ql
        self.score = 0

    def __repr__(self):
        return f"QuizBrain(question_number={self.question_number}, score={self.score})"

    def still_has_questions(self):
        """returns True if there are still questions left in the question_list, False otherwise"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """prints the next question in the question_list and asks the user for an answer"""
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            guess = input(
                f"Q.{self.question_number}: {current_question.question}. True/False "
            )
            self.check_answer(guess, current_question.answer)

    def check_answer(self, guess, correct_answer):
        """checks if the user's guess is correct and updates the score accordingly"""
        print(guess.lower(), correct_answer.lower())
        if guess.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct! Your score is { self.score}/{self.question_number}\n")
        else:
            print(
                f"Wrong! It was {correct_answer}. Your score is { self.score}/{self.question_number}\n"
            )
