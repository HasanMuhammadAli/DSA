def removeStars(s):
    stk = []
    for char in s:
        if stk and char == "*":
            stk.pop()
        else:
            stk.append(char)

    return "".join(stk)
            
s = "leet**cod*e"
print(removeStars(s))
s = "erase*****"
print(removeStars(s))