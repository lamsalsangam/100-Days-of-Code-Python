# You can pass as many arguments as you want after initializing the variable with "**"
# Example "**kargs"
# def calculate(**kwargs):  # Dictionary
#     for key, value in kwargs.items():
#         print(key)
#         print(value)


# calculate(add=3, multiply=5)


def calculate(n, **kwargs):  # Dictionary
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)  # 25


calculate(2, add=3, multiply=5)
