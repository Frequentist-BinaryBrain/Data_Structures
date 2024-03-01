#   Example: Factorial

#   1. Identify the Recursive Case - The Flow:
#   2. Base Case - The Stopping Criteria:
#   3. Unintentional Case - The Constraint:

#   1. Identify the Recursive Case - The Flow:

#    Define the general expression for factorial: n!=n×(n−1)!n!=n×(n−1)!
#    Identify the recursive case by expressing the right side of the equation as n−1n−1 factorial.

def factorial(n):
    return n * factorial(n-1)

#   2. Base Case - The Stopping Criteria:
#
#     Implement a base case to prevent infinite recursion.
#     Use conditions for when n=0n=0 or n=1n=1, return 1.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#   3. Unintentional Case - The Constraint:
#
#     Why Constraints?
#
#     Recursive functions may lead to infinite loops if not handled carefully.
#     Constraints help ensure that the function is called with valid inputs, preventing unexpected behavior.
#
# Using Assertions:
#
#     Assertions are checks placed in the code to ensure specific conditions are met.
#     If the condition is not satisfied, an AssertionError is raised, halting the program.
#     In this case, assertions are used to enforce that n is both greater than or equal to zero and an integer.

def factorial(n):
    assert n >= 0 and isinstance(n, int), "The number must be a positive integer only." # isinstance() checks whether a given object (variable n) belongs to a specified class (int).
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#   Behind the Scenes - Example: Calculating Factorial for n=4n=4
#
#     The control goes through each recursive call:
#         4×factorial(3)4×factorial(3)
#         3×factorial(2)3×factorial(2)
#         2×factorial(1)2×factorial(1)
#         factorial(1)factorial(1) returns 1
#         2×1=22×1=2
#         3×2=63×2=6
#         4×6=244×6=24

#   Conclusion:
#
#     Recursive method writing involves identifying the flow, setting stopping criteria with a base case, and adding constraints to prevent unintended cases.
#     Using these steps, a bugless recursive function for factorial calculation is implemented.
#     Understanding the recursive calls helps visualize how the function operates behind the scenes.
