# Q08_trapping_rain_water.py
# LeetCode #42

# Tershire
# 2023 OCT 04


# case ////////////////////////////////////////////////////////////////////////
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

heights = [4, 2, 0, 3, 2, 5]

# heights = [1, 0, 0, 0, 3]
# heights = [3, 0, 0, 0, 1]
# heights = [2, 1, 3, 0, 1]

heights = [0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2]
# expected: 26

# heights = [2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# search both walls
# timeout [ms]
def f1(heights: list[int]) -> int:
    volume = 0
    LENGTH = len(heights)
    i = 0
    while i < LENGTH:
        h = heights[i]
        i_L, i_R = i, i
        delta_h_L_max, delta_h_R_max = 0, 0
        i_L_limit, i_R_limit = 0, 0

        # search both sides each to detect the highest walls
        # for this current index.
        # 1) search left side
        while i_L > 0:
            i_L -= 1
            delta_h_L = heights[i_L] - h
            if delta_h_L > delta_h_L_max:
                delta_h_L_max = delta_h_L
                i_L_limit = i_L

        # 2) search right side
        while i_R < LENGTH - 1:
            i_R += 1
            delta_h_R = heights[i_R] - h
            if delta_h_R > delta_h_R_max:
                delta_h_R_max = delta_h_R
                i_R_limit = i_R

        # print("indices:", i_L_limit, i_R_limit)
        # print("delta_hs:", delta_h_L_max, delta_h_R_max)

        # if there are walls, fill in
        if delta_h_L_max > 0 and delta_h_R_max > 0:
            h_target = h + min(delta_h_L_max, delta_h_R_max)
            for j in range(i_L_limit + 1, i_R_limit):
                h_deficit = h_target - heights[j]
                if h_deficit > 0:
                    heights[j] = h_target
                    volume += h_deficit
        i += 1

        # print("i:", i)
        # print(heights)

    return volume


# -----------------------------------------------------------------------------
# rising water
# timeout [ms]
def f2(heights: list[int]) -> int:
    volume = 0

    # increase water level
    for h in range(min(heights), max(heights) + 1):
        # reset i_L
        i_L = None

        # scan for trough detection
        for i in range(1, len(heights)):
            # keep the index for the start of trough
            if heights[i] < heights[i - 1] and i_L is None:
                i_L = i

            if heights[i] > heights[i - 1] and i_L is not None:
                # fill up to the current water level
                for j in range(i_L, i):
                    if heights[j] < h:
                        volume += 1
                        heights[j] = h

                # reset i_start
                i_L = None

    return volume


# -----------------------------------------------------------------------------
# two-pointer
# 108 [ms]
def f1B(heights: list[int]) -> int:
    if not heights:
        return 0

    volume = 0
    i_L, i_R = 0, len(heights) - 1
    h_L_max, h_R_max = heights[i_L], heights[i_R]

    while i_L < i_R:
        h_L_max, h_R_max = max(heights[i_L], h_L_max), max(heights[i_R], h_R_max)

        if h_L_max <= h_R_max:
            volume += h_L_max - heights[i_L]
            i_L += 1
        else:
            volume += h_R_max - heights[i_R]
            i_R -= 1

    return volume


# -----------------------------------------------------------------------------
# stack
# 112 [ms]
def f2B(heights: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            i_L = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            depth = min(heights[i], heights[stack[-1]]) - heights[i_L]

            volume += distance * depth

        stack.append(i)

    return volume


# test ////////////////////////////////////////////////////////////////////////
print(f1(heights.copy()))
print(f2(heights.copy()))
print(f1B(heights.copy()))
print(f2B(heights.copy()))
