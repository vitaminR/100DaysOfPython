class QuizBrain:
    
    def __init__(self, ql):
        
        self.question_number = 0
        self.question_list = ql
    def next_question(self):
        # input(f"Q.{qn}: {ql[qn]["text"]}. True/False")
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text}. True/False")