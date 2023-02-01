# Errors
# FileNotFoundError
# KeyError
# IndexError
# TypeError
# Keywords >>>> try:   except:   else:    finally:

# try:  # Some thing that might cause exception
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["happy"])
# # except:  # Too broad exception clause
# except FileNotFoundError:  # Do this if there was an exception
#     # print("There was an error.")
#     open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     # print("That key doesn't exist.")
#     print(f"The {error_message} key doesn't exist.")
# # else:  # If the things that we are trying all succeed then this else block will execute
# else:  # Do this if there were no exceptions
#     content = file.read()
#     print(content)
# # finally:  # Code that will run no matter what will happen
# finally:  # DO this no matter what happens
#     # file.close()
#     # print("File was closed.")
#     ##############################################################
#     # Generating our own Exception
#     raise TypeError("This is an error that I made up")
#     # raise KeyError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
