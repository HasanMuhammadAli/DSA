'''
Name: Muhammad Ali Mosin Hasan
Date: 30/7/25
Problem: 504: Base 7
'''

def connvertToBase7(num):
    """
    Convert an integer to its base 7 representation.
    """
    
    if num == 0:
        return '0'

    orginal_num = num
    num = abs(num)
    remainders = []

    while num > 0:
        remainder = num % 7
        remainders.append(str(remainder))
        num //= 7
    
    if orginal_num < 0:
        remainders.append('-')
    remainders.reverse()

    return ''.join(remainders)

# Example usage:
num = 100
print(connvertToBase7(num))  # Output: '202'
num = -7
print(connvertToBase7(num))  # Output: '-10'