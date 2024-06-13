# Q12_best_time_to_buy_and_sell_stock.py
# LeetCode 121

# Tershire
# 2024 MAY 31


import sys


# KEY TAKEAWAY ****************************************************************
"""
focus directly more on the output we want to achieve.
for extreme values, one could use:
> sys.maxsize
> -sys.maxsize
"""


# case ////////////////////////////////////////////////////////////////////////
prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
prices = [2, 4, 1]
prices = [3, 2, 6, 5, 0, 3]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# closing in from sides picking up possible candidates. then brute-force.
# 4135 [ms]
def f1(prices: list[int]) -> int:
    mins, maxs = [(0, prices[0])], [(len(prices) - 1, prices[len(prices) - 1])]
    for i, price in enumerate(prices):
        if price < mins[-1][1]:
            mins.append((i, price))

    for i, price in enumerate(prices[::-1]):
        if price > maxs[-1][1]:
            maxs.append((len(prices) - i - 1, price))

    # print(mins)
    # print(maxs)
    highest_revenue = 0
    for i, min in mins:
        for j, max in maxs:
            if i < j:
                revenue = max - min
                if revenue > highest_revenue:
                    highest_revenue = revenue

    return highest_revenue


# -----------------------------------------------------------------------------
# brute-force
# timeout [ms]
# O(n^2)
def f1B(prices: list[int]) -> int:
    highest_revenue = 0
    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            highest_revenue = max(prices[j] - price, highest_revenue)

    return highest_revenue


# Kadane's algorithm variant
# 779 [ms]
# O(n)
def f2B(prices: list[int]) -> int:
    min_price = sys.maxsize
    highest_revenue = 0
    for price in prices:
        min_price = min(min_price, price)
        highest_revenue = max(highest_revenue, price - min_price)

    return highest_revenue

# comments:
"""
this is close to my initial approach but what was wrong about mine is that
I tried to update max_price too.
this does not work because it may lose the best opportunity,
while trying to update both min_price and max_price.
here, it focuses on maximizing the revenue directly,
and so, this approach gladly avoids the problem of my approach.
"""


# test ////////////////////////////////////////////////////////////////////////
print(f1(prices))
print(f1B(prices))
print(f2B(prices))
