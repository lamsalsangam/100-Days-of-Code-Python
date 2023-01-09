print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is the other one name? \n")

combined_string = name1+name2
fullname = combined_string.lower()

t = fullname.count("t")
r = fullname.count("r")
u = fullname.count("u")
e = fullname.count("e")

true = t+r+u+e

l = fullname.count("l")
o = fullname.count("o")
v = fullname.count("v")
e = fullname.count("e")

love = l+o+v+e

x = int(str(true) + str(love))

if x < 10 or x > 90:
    print(f"Your score is {x}, you go together like coke and mentos.")
elif 40 >= x <= 50:
    print(f"Your score is {x}, you are alright together.")
else:
    print(f"Your score is {x}")
