import pandas as pd


def get_phonetic_dict(csv_file):
    # Read the CSV file into a pandas DataFrame
    phonetic = pd.read_csv(csv_file)
    # Convert the DataFrame into a dictionary where the keys are the letters and the values are the codes
    return {phonetic.letter[i]: phonetic.code[i] for i in range(len(phonetic))}


# print(get_phonetic_dict("nato_phonetic_alphabet.csv"))


user_input = input("Give me a word to spell phonetically:\n")

# split the word into letters
user_input = user_input.upper()
for letter in user_input:
    print(f"{letter} : {get_phonetic_dict('nato_phonetic_alphabet.csv')[letter]}")
