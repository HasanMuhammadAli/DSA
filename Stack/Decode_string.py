def decodeString(s):
    stk = []
    ans = ""
    temp_old = ""
    for char in s:
        temp_new = ""
        
        
        if char != "]":
            stk.append(char)
        else:
            while stk and stk[-1] != "[":
                temp_new += stk.pop()

            stk.pop()
            curr_m = int(stk.pop())
            temp_new = temp_new[::-1]
            temp_old = temp_new + temp_old
            temp_old *= curr_m
            ans = temp_old 
           

    return ans

s= "3[a]2[bc]"
# s = "3[a2[c]]"
print(decodeString(s))