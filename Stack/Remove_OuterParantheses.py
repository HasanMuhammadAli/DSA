'''
Name: Muhammad Ali Mosin Hasan
Date: 5/7/25
Problem: 1021: Remove Outermost Parentheses
'''

#using stack

def removeOuterParentheses(s):
    stack = []
    result = []
    for char in s:
        if char == '(':
            if stack:
                result.append(char)
            stack.append(char)
        else:
            stack.pop()
            if stack:
                result.append(char)
    return ''.join(result)

# example
print(removeOuterParentheses("(()())(())"))

