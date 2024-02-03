import pandas as pd


class Phonetic:
    def __init__(self, csv_file):
        self.phonetic = pd.read_csv(csv_file)
        self.phonetic_dict = {key: value for (key, value) in self.phonetic.items()}


# student_data_frame = pd.DataFrame(student_dict)

# # Loop through rows of a data frame
# for index, row in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
phon_alph = Phonetic("nato_phonetic_alphabet.csv")

# for key, value in phon_alph.phonetic_dict.items():
#     # Your code here


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# print(student_data_frame)
print(phon_alph.phonetic_dict.items())


# # Looping through dictionaries:
# for key, value in student_dict.items():
#     # Access key and value
#     pass
