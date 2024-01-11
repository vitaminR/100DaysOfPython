from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


# print(answer["answer"])

# new_q = Question(question,answer )

# print(new_q)


# print (question_data[0])
# print (question_data[0]["text"])
# print (question_data[0]["answer"])
# print (question_data[1])
# print (question_data[1]["text"])
# print (question_data[1]["answer"])

# print(len(question_data))


#     print()(0,len(question_data)-1)]["answer"]
# print(question["text"])
# new_question
# question = question_data[random.randint(0,len(question_data)-1)]["text"]
# answer = question_data[random.randint


question_bank = []

for q in question_data:
    new_question = Question(q["question"], q["correct_answer"])
    question_bank.append(new_question)


print("are you ready to play Quiznite?")

# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"you are done, your total score is {quiz.score}/12")
