#   Step 1: Recursive Case - The Flow
#
#     Definition of Recursive Case:
#         The Fibonacci sequence is defined by the sum of the two preceding numbers.
#         Recursive case: f(n)=f(n−1)+f(n−2)f(n)=f(n−1)+f(n−2)

#   Step 2: Base Case - The Stopping Criteria
#
#     Base Cases for Fibonacci:
#         Fibonacci of 0 is 0, and Fibonacci of 1 is 1.
#         Return these values when the parameter is 0 or 1.

#   Step 3: Unintentional Case - The Constraint
#
#     Additional Constraints:
#         Ensure the parameter is a non-negative integer.
#         Use assert to check n≥0n≥0 and isinstance(n,int)isinstance(n,int).

def fibonacci(n):
    assert n >= 0 and isinstance(n, int), "Fibonacci number cannot be negative or non-integer."

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

#   initial Call: Fibonacci(4)
#
#     Initial Check:
#         4≥0 (True)
#         n=4 is an integer.
#
#     Recursive Calls:
#         fibonacci(3) and fibonacci(2)
#
# Recursive Call 1: Fibonacci(3)
#
#     Initial Check:
#         3≥0 (True)
#         n=3 is an integer.
#
#     Recursive Calls:
#         fibonacci(2) and fibonacci(1)
#
# Recursive Call 1.1: Fibonacci(2)
#
#     Initial Check:
#         2≥0 (True)
#         n=2 is an integer.
#
#     Recursive Calls:
#         fibonacci(1) and fibonacci(0)
#
# Recursive Call 1.1.1: Fibonacci(1)
#
#     Base Case:
#         n=1, returns 1.
#
# Recursive Call 1.1.2: Fibonacci(0)
#
#     Base Case:
#         n=0, returns 0.
#
# Return to Recursive Call 1.1: Fibonacci(2)
#
#     Return Values:
#         fibonacci(1) returns 1
#         fibonacci(0) returns 0
#     Calculation:
#         1+0=11+0=1
#
# Return to Recursive Call 1: Fibonacci(3)
#
#     Return Values:
#         fibonacci(2) returns 1
#         fibonacci(1) returns 1
#     Calculation:
#         1+1=2
#
# Recursive Call 2: Fibonacci(2)
#
#     Initial Check:
#         2≥0 (True)
#         n=2 is an integer.
#
#     Recursive Calls:
#         fibonacci(1) and fibonacci(0)
#
# Recursive Call 2.1: Fibonacci(1)
#
#     Base Case:
#         n=1, returns 1.
#
# Recursive Call 2.2: Fibonacci(0)
#
#     Base Case:
#         n=0, returns 0.
#
# Return to Recursive Call 2: Fibonacci(2)
#
#     Return Values:
#         fibonacci(1) returns 1
#         fibonacci(0) returns 0
#     Calculation:
#         1+0=1
#
# Return to Initial Call: Fibonacci(4)
#
#     Return Values:
#         fibonacci(3) returns 2
#         fibonacci(2) returns 1
#     Calculation:
#         2+1=3
