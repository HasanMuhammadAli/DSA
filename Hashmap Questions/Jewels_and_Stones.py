'''
Name: Muhammad Ali Mosin Hasan
Date: 11/6/25
Problem: 771:Jewels and Stones
'''

#O(n*m)
def numJewelsInStonesBrute(jewels,stones):
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count

#O(n+m)
def numJewelsInStonesOptimized(jewels,stones):
    count = 0
    # create a set
    s = set(jewels)
    for stone in stones:
        if stone in s:
            count += 1
    return count

jewels = "aA"
stones = "aAAbbbb"

count = numJewelsInStonesBrute(jewels, stones)
print("Number of jewels in stones (Brute Force):" + str(count))

count = numJewelsInStonesBrute(jewels, stones)
print("Number of jewels in stones (Optimized):" + str(count))

