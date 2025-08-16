# Program to calculate factorial of a number

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample number
num = 5

# Calling the function
print(f"The factorial of {num} is: {factorial(num)}")
