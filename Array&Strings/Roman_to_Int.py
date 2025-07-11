'''
Name: Muhammad Ali Mosin Hasan
Date: 11/7/25
Problem: 13:  Roman to Integer
'''

def romanToInt(str):
    '''
    Convert a Roman numeral string to an integer.
    '''
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(str)
    sum = 0
    i = 0

    while i < n:
        if i < n-1 and vals[str[i]] < vals[str[i+1]]:
            sum += vals[str[i+1]] - vals[str[i]] # right - left
            i += 2
        
        else: 
            sum += vals[str[i]]
            i += 1
        
    return sum

print(romanToInt("MCMXCIV"))  # Output: 1994
print(romanToInt("XL"))       # Output: 40