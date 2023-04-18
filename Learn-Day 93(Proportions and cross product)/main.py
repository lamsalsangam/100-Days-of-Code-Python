def are_fractions_equal(num1, den1, num2, den2):
    """Check if two fractions are equal using cross products."""
    cross_product1 = num1 * den2
    cross_product2 = num2 * den1
    if cross_product1 == cross_product2:
        return True
    else:
        return False

# Get input from the user
num1 = int(input("Enter numerator of the first fraction: "))
den1 = int(input("Enter denominator of the first fraction: "))
num2 = int(input("Enter numerator of the second fraction: "))
den2 = int(input("Enter denominator of the second fraction: "))

# Call the function to check if the fractions are equal
equal = are_fractions_equal(num1, den1, num2, den2)

# Display the result
if equal:
    print("The two fractions are equal.")
else:
    print("The two fractions are not equal.")
