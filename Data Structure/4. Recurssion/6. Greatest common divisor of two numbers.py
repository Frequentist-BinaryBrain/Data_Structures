def gcd(a, b):

    # Assertion for positive integer inputs
    assert isinstance(a, int) and isinstance(b, int), "Both numbers must be integers."
    assert a >= 0 and b >= 0, "Both numbers must be non-negative."

    # Base case: If b is 0, then the GCD is found, and we return a.
    if b == 0:
        return a
    else:
        # Recursive case: Apply the Euclidean algorithm.
        # Replace a with b, and replace b with the remainder of a divided by b.
        return gcd(b, a % b)

# Example: Find GCD(48, 18)
result = gcd(48, 18)
print("GCD(48, 18) =", result)
