'''
Name: Muhammad Ali Mosin Hasan
Date: 31/7/25
Problem: 231: Power of Two
'''
def isPowerOfTwo(n):
    """
    Check if a number is a power of two.
    """
    
    if n <= 0:
        return False
    
    # A number is a power of two if it has only one bit set in its binary representation.
    return (n & (n - 1)) == 0

# Example usage:
n = 16  # Binary: 10000
print(isPowerOfTwo(n))  # Output: True
n = 18  # Binary: 10010
print(isPowerOfTwo(n))  # Output: False