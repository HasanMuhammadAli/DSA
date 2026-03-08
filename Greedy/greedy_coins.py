# def greedy_choice(n):
#     coins = [200, 100, 50, 20, 10, 5, 2, 1]
#     ans = []
#     for coin in coins:
#         flag = True
#         while flag:
#             if coin <= n:
#                 print(coin, "  ", n)
#                 ans.append(coin)
#                 n -= coin
#             else:
#                 flag = False
#     return ans

# n = 520
# print(greedy_choice(n))


def greedy_choice(n):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    ans = []
    for coin in coins:
        res = n//coin
        ans.append(res)
        n %= coin
    return ans

n = 520
print(greedy_choice(n))

