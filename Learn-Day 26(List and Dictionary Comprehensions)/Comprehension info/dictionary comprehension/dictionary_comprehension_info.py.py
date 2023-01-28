'''
Dictionary comprehension is a method for transforming one dictionary into another dictionary. 
During this transformation, items within the original dictionary can be conditionally included in the new dictionary and each item can be transformed as needed.
'''

# Example: new_dict = {new_key : new_value for item in list}
# Example: new_dict = {new_key : new_value for (key, value) in dict.items()}
# Example: new_dict = {new_key : new_value for (key, value) in dict.items() if test}

####################
# import random
# names = ['Ram', 'Hari', 'Krishna', "Shiva", "Utsav"]

# student_scores = {student: random.randint(1, 100) for student in names}

# print(student_scores)

# # dictionary.item() conver the dictionary to the list for us to make it easier for us to loop through it.

# passed_students = {student: score for (
#     student, score) in student_scores.items() if score >= 60}

# print(passed_students)
