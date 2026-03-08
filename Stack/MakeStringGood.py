def makeGood(s):
    stk = []
    for char in s:
        if stk and stk[-1].lower() == char.lower() and stk[-1] != char:
            stk.pop()
            continue
        stk.append(char)
        
    return "".join(stk)

s = "abBAcC"
print(makeGood(s))
s = "leEeetcode"
print(makeGood(s))
