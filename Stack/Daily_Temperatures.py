'''
Name: Muhammad Ali Mosin Hasan
Date: 30/6/25
Problem: 739: Daily Temperatures
'''

def dailyTemperatures(temperatures):
    """
    Calculate the number of days until a warmer temperature for each day in the list.
    """
    temps = temperatures
    n = len(temps)
    ans = [0] * n
    stk = []

    for i, t in enumerate(temps):
        #print(t, i)
        while stk and stk[-1][0] < t:
            stk_t, stk_i = stk.pop()
            ans[stk_i] = i - stk_i

        stk.append((t, i))
    return ans


print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))