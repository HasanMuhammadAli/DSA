'''
Name: Muhammad Ali Mosin Hasan
Date: 6/7/25
Problem: 844: Backspace String Compare
'''
def backspaceCompare(s,t):
    '''
    Compares two strings after applying backspace operations.
    
    A backspace character '#' deletes the previous character in the string.
    This function determines if both strings become equal after processing all backspaces.
    '''
    stk_s = []
    stk_t = []

    for ch in  s:
        if not ch == '#':
            stk_s.append(ch)
        elif stk_s and ch == '#':
            stk_s.pop()
    
    for ch in  t:
        if not ch == '#':
            stk_t.append(ch)
        elif stk_t and ch == '#':
            stk_t.pop()

    if stk_s == stk_t:
        return True
    else:
        return False

s = "ab#c" 
t = "ad#c"
print(backspaceCompare(s, t))

s = "ab##" 
t = "c#d#"
print(backspaceCompare(s, t))

s = "a#c"
t = "b"
print(backspaceCompare(s, t))