import scipy.integrate as spi
import numpy as np

def integrand(x, expr):
    # Define the function to be integrated
    # expr: string expression to be evaluated at x
    return eval(expr)

# Ask the user for the expression to be integrated and the limits of integration
expr = input("Enter the expression to be integrated: ")
a_expr = input("Enter the lower limit of integration as an expression in x: ")
b_expr = input("Enter the upper limit of integration as an expression in x: ")

# Define lambda functions for the limits of integration
a = lambda x: eval(a_expr)
b = lambda x: eval(b_expr)

# Calculate the definite integral using the quad function
result, error = spi.quad(integrand, a, b, args=(expr,))

# Print the result and error
print(f"The definite integral of the expression '{expr}' from {a_expr} to {b_expr} is {result:.4f} with error {error:.4e}")
