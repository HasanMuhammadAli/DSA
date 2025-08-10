'''
Name: Muhammad Ali Mosin Hasan
Date: 10/8/25
Problem: 739: Daily Temperatures
Alternative stack-based approach
'''

def dailyTemperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []  # stores indices of days

    for i in range(n):
        # While current temperature is greater than the temperature at index on top of stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        stack.append(i)  # push current day index
    return ans

# Test cases
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
