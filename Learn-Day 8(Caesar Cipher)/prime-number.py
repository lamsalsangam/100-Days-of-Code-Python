# Prime number checker

def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    if not is_prime:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
