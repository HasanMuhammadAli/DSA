'''
Name: Muhammad Ali Mosin Hasan
Date: 4/7/25
Problem: 1475: Final Prices With a Special Discount in a Shop
Alternative stack-based approach
'''

def finalPricesWithDiscount(prices):
    n = len(prices)
    ans = prices[:]  
    stack = []  # will store indices of prices

    for i in range(n):
        
        while stack and prices[stack[-1]] >= prices[i]:
            prev_index = stack.pop()
            ans[prev_index] -= prices[i]
        stack.append(i)
    return ans

# Test cases
print(finalPricesWithDiscount([8, 4, 6, 2, 3]))  # [4, 2, 4, 2, 3]
print(finalPricesWithDiscount([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(finalPricesWithDiscount([10, 1, 1, 6]))    # [9, 0, 1, 6]
