for number in range(1, 101):
    # Remove the or operator and replace it with and operator
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        # Remove the [] from the number
        print(number)
