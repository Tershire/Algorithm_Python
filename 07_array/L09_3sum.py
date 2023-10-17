# Q09_3sum.py
# LeetCode #15

# Tershire
# 2023 OCT 06


import collections

# KEY TAKEAWAY ****************************************************************
# 3 nested loops O(n^3) -> i move & two-pointer O(n^2)
# sum(list) is much slower than manual + of elements
# minimize conditional checks

# case ////////////////////////////////////////////////////////////////////////
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 1, 1]
# nums = [0, 0, 0]
# nums = [-1, 0, 1, 0]
nums = [-2, 0, 0, 2, 2]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# brute-force and dict
# timeout [ms]
def f1(nums: list[int]) -> list[list[int]]:
    LENGTH = len(nums)

    # build roster
    roster = collections.defaultdict(list[int])
    for i, num in enumerate(nums):
        roster[num].append(i)

    # find combinations
    combinations = []
    for i in range(LENGTH):
        for j in range(i + 1, LENGTH):
            num_i, num_j = nums[i], nums[j]
            two_sum = num_i + num_j
            num_k = -two_sum
            if num_k in roster:
                # skip redundant numbers
                if (num_i == num_k or num_j == num_k) and len(roster[num_k]) < 2:
                    continue
                if (num_i == num_k and num_j == num_k) and len(roster[num_k]) < 3:
                    continue
                # build combination
                combination = sorted([num_i, num_j, num_k])
                if combination not in combinations:
                    combinations.append(combination)

    return combinations


# -----------------------------------------------------------------------------
# brute-force
# timeout [ms]
def f1B(nums: list[int]) -> list[list[int]]:
    nums.sort()

    LENGTH = len(nums)

    combinations = []
    for i in range(LENGTH - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, LENGTH - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, LENGTH):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                combination = [nums[i], nums[j], nums[k]]
                if sum(combination) == 0:
                    combinations.append(combination)

    return combinations


# -----------------------------------------------------------------------------
# two-pointer
# 2400 [ms]
def f2B(nums: list[int]) -> list[list[int]]:
    nums.sort()

    LENGTH = len(nums)

    combinations = []
    # move i
    for i in range(LENGTH - 2):
        num_i = nums[i]
        if i > 0 and num_i == nums[i - 1]:
            continue
        # move j_L, j_R closing in
        j_L, j_R = i + 1, LENGTH - 1
        while j_L < j_R:
            num_j_L, num_j_R = nums[j_L], nums[j_R]

            # check sum
            combination = [num_i, num_j_L, num_j_R]
            three_sum = sum(combination)
            # close in
            if three_sum == 0:
                combinations.append(combination)
                j_L += 1
                j_R -= 1
                while j_L > i + 1 and j_L < j_R and nums[j_L] == nums[j_L - 1]:
                    j_L += 1
                while j_R < LENGTH - 1 and j_L < j_R and nums[j_R] == nums[j_R + 1]:
                    j_R -= 1
            elif three_sum < 0:
                j_L += 1
                while j_L > i + 1 and j_L < j_R and nums[j_L] == nums[j_L - 1]:
                    j_L += 1
            else:
                j_R -= 1
                while j_R < LENGTH - 1 and j_L < j_R and nums[j_R] == nums[j_R + 1]:
                    j_R -= 1

    return combinations


# -----------------------------------------------------------------------------
# two-pointer (ver. 2)
# 1600 [ms] (why faster than f2B (?))
def f3B(nums: list[int]) -> list[list[int]]:
    nums.sort()

    LENGTH = len(nums)

    combinations = []
    # move i
    for i in range(LENGTH - 2):
        num_i = nums[i]
        if i > 0 and num_i == nums[i - 1]:
            continue
        # move j_L, j_R closing in
        j_L, j_R = i + 1, LENGTH - 1
        while j_L < j_R:
            num_j_L, num_j_R = nums[j_L], nums[j_R]

            # check sum
            combination = [num_i, num_j_L, num_j_R]
            three_sum = sum(combination)
            # close in
            if three_sum < 0:
                # while j_L < j_R and nums[j_L] == nums[j_L + 1]:  # slower if you do this, why (?)
                #     j_L += 1
                j_L += 1
            elif three_sum > 0:
                # while j_L < j_R and nums[j_R] == nums[j_R - 1]:  # slower if you do this, why (?)
                #     j_R -= 1
                j_R -= 1
            else:
                combinations.append(combination)
                # skip redundant numbers
                while j_L < j_R and nums[j_L] == nums[j_L + 1]:
                    j_L += 1
                while j_L < j_R and nums[j_R] == nums[j_R - 1]:
                    j_R -= 1
                # skip or not, we need to move on
                j_L += 1
                j_R -= 1

                # j_L += 1
                # j_R -= 1
                # while j_L > i + 1 and j_L < j_R and nums[j_L] == nums[j_L - 1]:
                #     j_L += 1
                # while j_R < LENGTH - 1 and j_L < j_R and nums[j_R] == nums[j_R + 1]:
                #     j_R -= 1

    return combinations


# -----------------------------------------------------------------------------
# two-pointer (ver. 3)
# 1085 [ms] (why faster than f3B (?))
def f4B(nums: list[int]) -> list[list[int]]:
    nums.sort()

    combinations = []
    # move i
    for i in range(len(nums) - 2):
        num_i = nums[i]
        if i > 0 and num_i == nums[i - 1]:
            continue
        # move j_L, j_R closing in
        j_L, j_R = i + 1, len(nums) - 1
        while j_L < j_R:
            num_j_L, num_j_R = nums[j_L], nums[j_R]

            # check sum
            three_sum = num_i + num_j_L + num_j_R
            # combination = [num_i, num_j_L, num_j_R]
            # three_sum = sum(combination)
            # close in
            if three_sum < 0:
                j_L += 1
            elif three_sum > 0:
                j_R -= 1
            else:
                combinations.append([num_i, num_j_L, num_j_R])
                # combinations.append(combination)
                # skip redundant numbers
                while j_L < j_R and nums[j_L] == nums[j_L + 1]:
                    j_L += 1
                while j_L < j_R and nums[j_R] == nums[j_R - 1]:
                    j_R -= 1
                # skip or not, we need to move on
                j_L += 1
                j_R -= 1

    return combinations


# test ////////////////////////////////////////////////////////////////////////
print(f1(nums))
print(f1B(nums))
print(f2B(nums))
print(f3B(nums))
print(f4B(nums))
