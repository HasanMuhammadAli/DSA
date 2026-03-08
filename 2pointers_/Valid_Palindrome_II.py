def isValid(strr):
    left, right = 0, len(strr)-1
    lflag = True
    rflag = True
    ans = True
    while left <= right:
        if strr[left] == strr[right]:
            left += 1
            right -= 1

        elif strr[left] != strr[right] and lflag:
            #skip left 
            left += 1
            lflag = False 
            continue

        elif strr[left] != strr[right] and rflag:
            #skip left 
            right -= 1
            rflag = False 
            continue

        

