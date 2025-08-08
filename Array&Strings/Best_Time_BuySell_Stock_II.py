'''
Name: Muhammad Ali Mosin Hasan
Date: 25/7/25
Problem: 122: Best Time to Buy and Sell Stock II
'''

def maxProfit(prices):
    """
    Given a list of prices where prices[i] is the price of a given stock on day i, return the maximum profit you can achieve from multiple transactions.
    You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    Note: You cannot engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    """

    

    i = 0
    low = prices[0]
    high = prices[0]
    profit = 0
    n = len(prices)

    while i < n - 1:
        #look where to buy
        while i < n-1 and prices[i] >= prices[i + 1]:
            i += 1
        low = prices[i]

        #look where to sell
        while i < n-1 and prices[i] <= prices[i + 1]:
            i += 1
        high = prices[i]        

        profit += high - low
    
    return profit

prices = [7, 6, 4, 3, 1, 5, 8, 3, 6, 4]
print(maxProfit(prices))