def sum_of_digits(n):
    # Assertion for positive integer input
    assert n >= 0 and int(n) == n, "The number must be a positive integer only."

    # Check for the base case
    if n == 0:
        return 0

    # Recursive case equation
    return n % 10 + sum_of_digits(n // 10)

# Test the function
print("Sum of digits for 4:", sum_of_digits(4))
print("Sum of digits for 12:", sum_of_digits(12))
print("Sum of digits for 112:", sum_of_digits(112))
print("Sum of digits for -11:", sum_of_digits(-11))  # Will raise an error due to the assertion
print("Sum of digits for 1234:", sum_of_digits(1234))
print("Sum of digits for 12345:", sum_of_digits(12345))
