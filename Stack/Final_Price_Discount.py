'''
Name: Muhammad Ali Mosin Hasan
Date: 4/7/25
Problem: 1475: Final Prices With a Special Discount in a Shop
'''

def finalPricesWithDiscount(prices):
    '''
    Calculates the final prices after applying a special discount for each item in a shop.

    For each item, the discount is the price of the first subsequent item that is less than or equal to the current item's price.
    If no such item exists, no discount is applied.

    '''
    n = len(prices)
    ans = prices
    stk = []

    for i, price in enumerate(prices):
        while stk and stk[-1][0] >= price:
            stk_p, stk_i = stk.pop()
            ans[stk_i] = stk_p - price
        
        stk.append((price, i))
    return ans

prices = [8, 4, 6, 2, 3]
print(finalPricesWithDiscount(prices))

prices = [1,2,3,4,5]
print(finalPricesWithDiscount(prices))

prices = [10,1,1,6]
print(finalPricesWithDiscount(prices))