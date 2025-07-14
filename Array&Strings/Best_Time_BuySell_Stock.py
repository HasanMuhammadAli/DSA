'''
Name: Muhammad Ali Mosin Hasan
Date: 14/7/25
Problem: 121: Best Time to Buy and Sell Stock
'''

def maxProfit(prices):
    """
    Given a list of prices where prices[i] is the price of a given stock on day i, return the maximum profit you can achieve from a single buy and sell.
    If you cannot achieve any profit, return 0.
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        
    return max_profit

print(maxProfit([7,1,5,3,6,4]))  # Buy at 1, sell at 6  # 5
print(maxProfit([7,6,4,3,1]))    # No profit possible   # 0
print(maxProfit([1,2,3,4,5]))    # Buy at 1, sell at 5  # 4
print(maxProfit([2,4,1]))        # Buy at 2, sell at 4  # 2
