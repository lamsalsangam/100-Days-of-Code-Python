def VowelsinWord(string):
    lower_string = string.lower()
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(lower_string)):
        for j in range(len(vowels)):
            if lower_string[i] == vowels[j]:
                count += 1
    if count == 0:
        print("There are no vowles in the character you have provided")
    else:
        print(f"There are {count} vowels in the string you have provided")


user_input = input("Which string do you want to perform the check for:\n")
VowelsinWord(user_input)
