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
with open("file1.txt", "r") as file:
    file1_content = file.read().splitlines()

with open("file2.txt", "r") as file:
    file2_content = file.read().splitlines()

# Find common numbers
common_numbers = [num for num in file1_content if num in file2_content]

print(f"Common numbers: {common_numbers}")
