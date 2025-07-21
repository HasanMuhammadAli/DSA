'''
Name: Muhammad Ali Mosin Hasan
Date: 21/7/25
Problem: 6: ZigZag Conversion
'''

def conversion(s, numRows):
    '''
    Converts the input string s into a zigzag pattern on a given number of rows, then reads line by line to produce the final string.
    '''

    if numRows == 1:
        return s
    
    i = 0 
    d = 1 # direction 1 -> downward, -1 -> upward

    rows = [ [] for _ in range(numRows)]

    for char in s:
        rows[i].append(char)
        if i == 0:
            d = 1
        if i == numRows - 1:
            d = -1
        i += d
    
    ret = ''
    for i in range(numRows):
        ret += ''.join(rows[i])
    
    return ret

s1 = "PAYPALISHIRING"
numRows1 = 3
print(conversion(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

s2 = "HELLOWORLD"
numRows2 = 4
print(conversion(s2, numRows2))  # Output: "HOEWRLLLOD"