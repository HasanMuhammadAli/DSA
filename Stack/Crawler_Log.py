def minOperations(logs):
    stk = []
    count = 0
    for s in logs:
        if s == "../" and stk:
            stk.pop()
            count -= 1
        elif s == "./":
            continue
        elif s == "../" and not stk:
            count = 0
        else:
            stk.append(s)
            count += 1
    return count


logs = ["./","../","./"]
print(minOperations(logs))