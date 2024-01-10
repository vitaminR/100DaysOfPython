class QuizBrain:
    
    def __init__(self, ql):
        
        self.question_number = 0
        self.question_list = ql
        self.score = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        
    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            self.guess = input(f"Q.{self.question_number}: {current_question.text}. True/False")
            check_answer(self)

    def check_answer(self):
        if self.guess == self.current_question.answer:
            self.score += 1
            print(f"correct, your score is {self.score}/{self.question_number}")
            print("\n")
        else:
            print(F"Wrong, score: {self.score}/{self.question_number}")
            
