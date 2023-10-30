# Q10_array_partition.py
# LeetCode #561

# Tershire
# 2023 OCT 30


# KEY TAKEAWAY ****************************************************************
# I first thought about the mathematics.
# while not proven, it gave me an idea that to achieve this request,
# the distance of each pair of numbers should be minimized,
# meaning that they better to be sorted, then paired up.


# case ////////////////////////////////////////////////////////////////////////
nums = [1, 4, 3, 2]
nums = [6, 2, 6, 5, 1, 2]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# sort and make partition
# 238 [ms]
def f1(nums: list[int]) -> int:
    nums.sort()

    # add numbers at even indices
    sum = 0
    for i in range(0, int(len(nums)), 2):
        # sum += min(nums[i:i + 1])  # 255 [ms]
        sum += nums[i]  # 238 [ms]

    return sum


# -----------------------------------------------------------------------------
# sort and make partition
# 240 [ms]
def f1B(nums: list[int]) -> int:
    nums.sort()

    # add numbers at even indices
    sum = 0
    for i, num in enumerate(nums):
        if i % 2 == 0:
            sum += num

    return sum


# -----------------------------------------------------------------------------
# sort and make partition with slicing
# 235 [ms]
def f2B(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])


# test ////////////////////////////////////////////////////////////////////////
print(f1(nums))
print(f1B(nums))
print(f2B(nums))
