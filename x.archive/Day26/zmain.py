# name = "Johnathon"
# new_list = [letter for letter in name]

# print(new_list)

# double = [n * 2 for n in range(1, 5)]
# print(double)


# # list conprehension with conditional
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [name for name in names if len(name) < 5]

# print(short_names)

# Open both files and read their content
# with open("file1.txt", "r") as file:
#     file1_content = file.read().splitlines()

# with open("file2.txt", "r") as file:
#     file2_content = file.read().splitlines()

# # Find common numbers
# common_numbers = [num for num in file1_content if num in file2_content]

# print(f"Common numbers: {common_numbers}")

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random

# students_scores = {student: random.randint(1, 100) for student in names}

# print(students_scores)

# passed = {student: score for (student, score) in students_scores.items() if score > 59}

# print(passed)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # 🚨 Don't change code above 👆
# # Write your code below 👇
# word_list = sentence.split()

# words = {word: len(word) for (word) in word_list}

# print(words)

# # students_scores = {student: random.randint(1, 100) for student in names}

# # print(students_scores)

# # passed = {student: score for (student, score) in students_scores.items() if score > 59}

# # print(passed)


# # print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:

# weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

# print(weather_f)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# # Using dictionary comprehension
# result = {word: len(word) for word in sentence.split()}

# print(result)
