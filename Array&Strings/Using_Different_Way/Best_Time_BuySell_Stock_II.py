'''
Name: Muhammad Ali Mosin Hasan
Date: 8/8/25
Problem: 122: Best Time to Buy and Sell Stock II
'''

def maxProfit(prices):
    """
    Given a list of prices where prices[i] is the price of a given stock on day i, return the maximum profit you can achieve from multiple transactions.
    You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    Note: You cannot engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    """

    
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


prices = [7, 6, 4, 3, 1, 5, 8, 3, 6, 4]
print(maxProfit(prices))