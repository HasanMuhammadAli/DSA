'''
Name: Muhammad Ali Mosin Hasan
Date: 5/7/25
Problem: 1021: Remove Outermost Parentheses
'''

#using stack

def removeOuterParentheses(str):
    stk = []
    ans = []
    if str == "" :
        return ""
    for ch in str:
        if ch == '(':
            if not stk:
                stk.append(ch)
                continue
            if stk:    
                ans.append(ch)
                stk.append(ch)
        else: 
            stk.pop()
            if stk:
                ans.append(ch)
    
    return ''.join(ans)

print(removeOuterParentheses("(()(()))"))
