def power(base, exponent):

    # Assertion for positive integer inputs
    assert base >= 0 and int(base) == base, "Base must be a positive integer."
    assert exponent >= 0 and int(exponent) == exponent, "Exponent must be a positive integer."

    # Base case: if the exponent is 0, return 1
    if exponent == 0:
        return 1

    # Recursive case: multiply the base by the result of the function with a reduced exponent
    return base * power(base, exponent - 1)

# Test the function
result = power(2, 3)
print("2^3 =", result)
