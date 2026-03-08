def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stk =[]

    for i, temp in enumerate(temperatures):
        while stk and temperatures[stk[-1]] < temp:
            prev = stk.pop()
            ans[prev] = i - prev
        
        stk.append(i)
   
    return ans

temperatures = [73, 74, 75, 71]
print(dailyTemperatures(temperatures))