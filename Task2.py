import math

# Ask user for input
num = float(input("Enter a number: "))

# Square root
sqrt_val = math.sqrt(num)

# Natural logarithm (only valid for positive numbers)
if num > 0:
    log_val = math.log(num)
else:
    log_val = "Undefined (logarithm only defined for positive numbers)"

# Sine (input is treated as radians)
sine_val = math.sin(num)

# Display results
print("\n--- Results ---")
print(f"Square root of {num} = {sqrt_val}")
print(f"Natural logarithm of {num} = {log_val}")
print(f"Sine of {num} radians = {sine_val}")

