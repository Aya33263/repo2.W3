# 1. Define the bonus multiplier
RAISE_FACTOR = 2400.00

# 2. Get the rating from the user
rating = float(input("Enter the employee rating (0.0, 0.4, or 0.6+): "))

# 3. Use an if-elif-else structure to handle each case directly
if rating == 0.0:
    print("Performance: Unacceptable performance")
    print(f"Employee Raise: ${0.0 * RAISE_FACTOR:.2f}")

elif rating == 0.4:
    print("Performance: Acceptable performance")
    print(f"Employee Raise: ${0.4 * RAISE_FACTOR:.2f}")

elif rating >= 0.6:
    print("Performance: Meritorious performance")
    print(f"Employee Raise: ${rating * RAISE_FACTOR:.2f}")

else:
    # This catches 0.1, 0.2, 0.5, etc.
    print("Error: The rating entered is invalid.")