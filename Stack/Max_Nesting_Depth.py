def maxDepth(s):
    stk = []
    curr = 0
    maxx = 0

    for char in s:
        if char == "(":
            stk.append(char)
            curr += 1
        elif char == ")":
            maxx = max(maxx, curr)
            stk.pop()
            curr -= 1
        else:
            continue

    return maxx

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))
s = "(1)+((2))+(((3)))"
print(maxDepth(s))
s = "()(())((()()))"
print(maxDepth(s))
