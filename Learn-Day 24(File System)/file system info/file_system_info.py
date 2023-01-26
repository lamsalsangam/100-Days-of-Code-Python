# Reading the file

# opening the file
# file = open("my_file.txt")
# with open("my_file.txt") as file:
#     # In this case we don't have to remember to close our file
#     content = file.read()
#     print(content)
# We need to close the file after the task is done because when file is opened it will take some of the computer resources
# file.close()


#############################

# r = readonly
# w = write
# a = append

#############################

# Writing in the file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text.")


# While writing the file in write mode if the file doesn't exist then its ging to actually create it for us.
with open("new_file.txt", mode="w") as file:
    file.write(
        "Hello! this is alpha reporting that the new file system has been created.")
