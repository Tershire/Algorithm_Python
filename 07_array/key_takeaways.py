# key_takeaways.py

# Tershire
# 2023 OCT 04


# sort on enumerate ///////////////////////////////////////////////////////////
# case: need to sort numbers while keeping their indices in the original list
nums = [3, 12, 0]
idx_nums = sorted(enumerate(nums), key=lambda x: x[1])
print(idx_nums)

# /////////////////////////////////////////////////////////////////////////////
# use two-pointer to reduce "dimension" of the problem
# 3 nested loops O(n^3) -> i move & two-pointer O(n^2)

# sum(list) is much slower than manual + of elements

# minimize conditional checks
