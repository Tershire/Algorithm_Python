# Q07_two_sum.py
# LeetCode #1

# Tershire
# 2023 OCT 04


import collections

# KEY TAKEAWAY ****************************************************************
# can solve two_sum using two-pointer idea.
# for this specific case needing only two numbers, roster does not have to save all the indices.
# can sort indexed numbers using enumerate


# case ////////////////////////////////////////////////////////////////////////
nums = [2, 7, 11, 15]
target = 9

nums = [3, 2, 4]
target = 6

nums = [3, 3]
target = 6


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# defaultdict
# 70 [ms]
def f1(nums: list[int], target: int) -> list[int]:
    roster = collections.defaultdict(list[int])
    for i, num in enumerate(nums):
        roster[num].append(i)

    for num, indices in roster.items():
        other_num = target - num
        if other_num in roster:
            other_indices = roster[other_num]
            if num == other_num:
                if len(other_indices) == 2:
                    return other_indices
                else:
                    continue
            return [indices[0], other_indices[0]]

    return [-1]


# -----------------------------------------------------------------------------
# two-pointer
# 65 [ms]
def f2(nums: list[int], target: int) -> list[int]:
    idx_nums = sorted(enumerate(nums), key=lambda x: x[1])

    i_L, i_R = 0, len(nums) - 1
    idx_num_L, idx_num_R = idx_nums[i_L], idx_nums[i_R]
    while not idx_num_L[1] + idx_num_R[1] == target:
        if idx_num_L[1] + idx_num_R[1] < target:
            i_L += 1
            idx_num_L = idx_nums[i_L]
        else:
            i_R -= 1
            idx_num_R = idx_nums[i_R]

    return [idx_num_L[0], idx_num_R[0]]


# -----------------------------------------------------------------------------
# defaultdict
# 60 [ms]
def f1B(nums: list[int], target: int) -> list[int]:
    roster = {}
    for i, num in enumerate(nums):
        roster[num] = i

    for i, num in enumerate(nums):
        other_num = target - num
        if other_num in roster and i != roster[other_num]:
            return [i, roster[other_num]]

# comments: why better than mine?
# - since we're looping anyway, no need to store all indices,
# ex) for nums = [3, 3], roster will be {3:1} not {3:[0, 1]}
# but, at i = 0, by checking 0 != 1, we get the correct answer.


# -----------------------------------------------------------------------------
# defaultdict
# 68 [ms]
def f1Ba(nums: list[int], target: int) -> list[int]:
    roster = {}
    for i, num in enumerate(nums):
        other_num = target - num
        if other_num in roster:
            return [roster[other_num], i]
        roster[num] = i


# test ////////////////////////////////////////////////////////////////////////
print(f1(nums, target))
print(f1B(nums, target))
print(f1Ba(nums, target))
print(f2(nums, target))
