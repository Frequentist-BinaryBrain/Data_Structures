def decimalToBinary(n):

    # Base case: if n is 0, return 0 as its binary representation
    if n <= 0:
        return 0
    else:
        # Recursive case:
        # 1. Calculate the remainder when n is divided by 2 (this is the current bit)
        # 2. Multiply the result of the recursive call (n // 2) by 10 and add the remainder
        return int(n)%2 + 10*decimalToBinary(int(n/2))

print(decimalToBinary(13))
