import random
from question_model import Question
from  data import question_data
from quiz_brain import QuizBrain


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
    
    new_question = Question(q["text"],q["answer"])
    question_bank.append(new_question)   


print("are you ready to play Quiznite?")

# print(question_bank)
quiz = QuizBrain(question_bank)
quiz.next_question()