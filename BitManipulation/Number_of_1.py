'''
Name: Muhammad Ali Mosin Hasan
Date: 27/7/25
Problem: 191: Number of 1 Bits
'''

def hammingWeight(n):
    """
    Calculate the Hamming weight (number of 1 bits) in the binary representation of an integer.
    """
    ans = 0
    while n != 0:
        ans += 1
        n = n & (n - 1)
    
    return ans

# Example usage:
n = 11  # Binary: 1011
print(hammingWeight(n))  # Output: 3
n = 128  # Binary: 10000000
print(hammingWeight(n))  # Output: 1