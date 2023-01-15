############ DEBUGGING#####################

############ SOLVED#####################

# Describe Problem
# def my_function():
#     #Range stop at 19 so just add +1 to the end value
#   for i in range(1, 20+1):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# Start form 0 to 5
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# convert age to int
# age = int(input("How old are you?"))
# if age > 18:
# Indent the print statement
#     print(f"You can drive at age {age}.")
# print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# There was == which I changed to = to fix it
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     #just needed to indent the b_list so not to cause the distortation in the final output
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
