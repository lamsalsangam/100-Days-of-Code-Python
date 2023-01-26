PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # It outputs the name as this ['Shiva\n', 'Narayan\n', 'Brahma\n', 'Ganesh\n', 'Kartik\n', 'BholeNath\n', 'Kal\n', 'Samaya']

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
