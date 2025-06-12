'''
Name: Muhammad Ali Mosin Hasan
Date: 11/6/25
Problem: 771:Jewels and Stones
'''

# O(n*m) Brute Force Approach
def numJewelsInStonesBrute(jewels, stones):
    '''
    Counts how many stones are jewels using brute force.

    Args:
        jewels (str): String representing types of jewels.
        stones (str): String representing stones you have.

    Returns:
        int: Number of stones that are jewels.
    '''
    count = 0
    for stone in stones:
        if stone in jewels:  # Check if current stone is a jewel
            count += 1
    return count

# O(n+m) Optimized Approach using set
def numJewelsInStonesOptimized(jewels, stones):
    '''
    Counts how many stones are jewels using a set for faster lookup.

    Args:
        jewels (str): String representing types of jewels.
        stones (str): String representing stones you have.

    Returns:
        int: Number of stones that are jewels.
    '''
    count = 0
    s = set(jewels)  # Convert jewels to a set for O(1) lookups
    for stone in stones:
        if stone in s:  # Check if current stone is a jewel
            count += 1
    return count

# Example usage
jewels = "aA"
stones = "aAAbbbb"

# Test brute force approach
count = numJewelsInStonesBrute(jewels, stones)
print("Number of jewels in stones (Brute Force): " + str(count))

# Test optimized approach
count = numJewelsInStonesOptimized(jewels, stones)
print("Number of jewels in stones (Optimized): " + str(count))

