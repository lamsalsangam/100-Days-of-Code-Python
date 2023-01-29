# Unlimited Positional Arguments or the Unlimited Arguments


# You can pass as many arguments as you want after initializing the variable with "*"
# Example "*args"
# def add(*args):
#     for n in args:
#         print(n)
# add(2,3,5,6)


def add(*args):  # Tuple
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 5, 6))
