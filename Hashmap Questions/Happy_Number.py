'''
Name: Muhammad Ali Mosin Hasan
Date: 25/6/25
Problem: 202: Happy Number
'''

#solution 1 using set to detect cycles
def isHappy1(n):
    '''
    Checks if a number is a happy number.
    A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
    '''
    seen = set()  # Track numbers we've seen to detect cycles
    
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate sum of squares of digits
        sum_squares = 0
        while n > 0:
            digit = n % 10
            sum_squares += digit ** 2
            n = n // 10
        n = sum_squares
    
    return n == 1


 
# Test Case 1: Happy number
n = 19
result = isHappy1(n)
print(f"Input: {n}")
print(f"Result: {result}")
print(f"Expected: True")
print()

# Test Case 2: Not a happy number
n = 2
result = isHappy1(n)
print(f"Input: {n}")
print(f"Result: {result}")
print(f"Expected: False")
print()

