def calculate_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    hcf = calculate_hcf(a, b)
    lcm = (a * b) // hcf
    return lcm

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate HCF and LCM
hcf = calculate_hcf(num1, num2)
lcm = calculate_lcm(num1, num2)

# Display results
print("HCF of", num1, "and", num2, "is:", hcf)
print("LCM of", num1, "and", num2, "is:", lcm)
