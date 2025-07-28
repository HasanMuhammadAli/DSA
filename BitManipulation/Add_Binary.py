'''
Name: Muhammad Ali Mosin Hasan
Date: 28/7/25
Problem: 67: Add Binary
'''

def addBinary(a, b):
    """
    Add two binary strings and return their sum as a binary string.
    """
    a, b = int(a, 2), int(b, 2)
    
    while b:
        without_carry = a ^ b  
        carry = (a & b) << 1

        a, b = without_carry, carry

    return bin(a)[2:]  # Convert to binary and remove the '0b' prefix

# Example usage:
a = "11"  # Binary: 11
b = "1"   # Binary: 1
print(addBinary(a, b))  # Output: "100"

a = "1111"
b = "0010"
print(addBinary(a, b))  # Output: "10001"