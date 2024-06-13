# Q11_product_of_array_except_self.py
# LeetCode 238

# Tershire
# 2024 MAY 29


# KEY TAKEAWAY ****************************************************************
"""
think about which computation is unnecessary.
"""


# case ////////////////////////////////////////////////////////////////////////
nums = [1, 2, 3, 4]
# nums = [-1, 1, 0, -3, 3]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# pre-calculation of cumulative multiplications: {from left, from right}
# 305 [ms]
def f1(nums: list[int]) -> list[int]:
    a = [nums[0]]
    b = [nums[-1]]
    c = []
    for i in range(len(nums) - 1):
        a.append(a[i] * nums[i + 1])
        b.append(b[i] * nums[-1 - (i + 1)])
    b.reverse()
    print(a)
    print(b)

    c.append(b[1])
    for i in range(1, len(nums) - 1):
        c.append(a[i - 1] * b[i + 1])
    c.append(a[-2])
    # print(c)

    return c


# -----------------------------------------------------------------------------
# similar to f1
# 269 [ms]
def f1B(nums: list[int]) -> list[int]:
    a = []
    p = 1
    for i in range(len(nums)):
        a.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        a[i] *= p  # direct multiplication to the "from left" products list
        p *= nums[i]

    return a

# comments:
"""
direct multiplication allows less spatial complexity.
also, the useless elements at each end of 'nums' are neglected.
accordingly, p = 1 due to the neglect.
"""


# test ////////////////////////////////////////////////////////////////////////
print(f1(nums))
print(f1B(nums))
