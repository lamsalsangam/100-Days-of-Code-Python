# Class should be named with the concept of the "PascalCase"
class User:
    # pass in python help to continue with the line of code if at the moment you don't want to define it.
    # "pass" is used in both function and classes as choice may occur
    # pass

    # self is the actuual object that is being initialized
    # after that we can add as many parameter as we desire
    # def __init__(self, user_id, username) -> None:
    def __init__(self, user_id, username) -> None:
        #### Attributes####
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    #### Methods####
    # A Method unlike a Function always need to have the "self" keyword as the first parameter
    def follow(self, user):
        user.followers += 1  # This one is for the one that we followed
        self.following += 1  # This one is our own count

        # user_1 = User()
        # Attribute is the variables that is associated with an object
        # user_1.id = "001"
        # --> It is totally valid but can be error prone for lots of data to be hardcoded
        # user_1.username = "kubi"


        # Now we can add the attributes at the time of construction only
user_1 = User("001", "のう")  # Brain
user_2 = User("002", "かお")  # Face

print(user_1.username)  # Now we can just print the attribute like this

user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
