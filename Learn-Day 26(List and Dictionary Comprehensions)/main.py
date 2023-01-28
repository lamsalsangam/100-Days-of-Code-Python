import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_dict = data.to_dict()
# print(data_dict)
'''
{'letter': {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'},
 'code': {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', 3: 'Delta', 4: 'Echo', 5: 'Foxtrot', 6: 'Golf', 7: 'Hotel', 8: 'India', 9: 'Juliet', 10: 'Kilo', 11: 'Lima', 12: 'Mike', 13: 'November', 14: 'Oscar', 15: 'Papa', 16: 'Quebec', 17: 'Romeo', 18: 'Sierra', 19: 'Tango', 20: 'Uniform', 21: 'Victor', 22: 'Whiskey', 23: 'X-ray', 24: 'Yankee', 25: 'Zulu'}}
'''

# data_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dict)
# phonetic = [data_dict[key] for key in data_dict]
# print(phonetic)

user_input = input("Enter the word: ").strip().upper()
# alphabets = [alpha for alpha in user_input]
# print(alphabets)

# result = [data_dict[alpha] for alpha in alphabets]
result = [data_dict[alpha] for alpha in user_input]
print(result)
