# Q06_longest_palindromic_substring.py
# LeetCode #5

# Tershire
# 2023 OCT 02


# KEY TAKEAWAY ****************************************************************
# divide cases:
# if nested functions are designed to work for len(list) >= 2,
# simple pre-filtering of cases len(list) < 2 will do the work.


# case ////////////////////////////////////////////////////////////////////////
s = "babad"
s = "aaaab"
s = "ab"
s = "a"


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# expanding two-pointer
# 95 [ms]
def f1(s: str) -> str:
    if s == s[::-1]:
        return s

    LENGTH = len(s)

    def check_even_palindrome(i, s):
        i_L, i_R = i, i + 1
        while i_L >= 0 and i_R < LENGTH:
            if s[i_L] != s[i_R]:
                return s[i_L + 1:i_R]
            if i_L == 0 or i_R == LENGTH - 1:
                return s[i_L:i_R + 1]
            i_L -= 1
            i_R += 1
        return ""

    def check_odd_palindrome(i, s):
        i_L, i_R = i, i
        while i_L >= 0 and i_R < LENGTH:
            if s[i_L] != s[i_R]:
                return s[i_L + 1:i_R]
            if i_L == 0 or i_R == LENGTH - 1:
                return s[i_L:i_R + 1]
            i_L -= 1
            i_R += 1
        return ""

    substring = ""
    for i in range(len(s)):
        even_palindrome = check_even_palindrome(i, s)
        odd_palindrome = check_odd_palindrome(i, s)
        if len(even_palindrome) > len(substring):
            substring = even_palindrome
        if len(odd_palindrome) > len(substring):
            substring = odd_palindrome

    return substring


# -----------------------------------------------------------------------------
# expanding two-pointer
# 90 [ms]

LENGTH = len(s)

def f1B(s: str) -> str:
    def expand(i_L: int, i_R: int) -> str:
        while i_L >= 0 and i_R < LENGTH and s[i_L] == s[i_R]:
            i_L -= 1
            i_R += 1
        return s[i_L + 1:i_R]

    if len(s) < 2 or s == s[::-1]:
        return s

    LENGTH = len(s)

    substring = ""
    for i in range(LENGTH - 1):  # why LENGTH - 1
        substring = max(substring,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key=len)
    return substring

# comments: why better than mine?
# - divided cases: 1) len(s) < 2 and 2) len(s) >= 2
# - function expand() works where len(s) >= 2
#   good condition which makes slicing simple
# - checks only up to LENGTH - 1 because don't have to


# test ////////////////////////////////////////////////////////////////////////
print(f1(s))
print(f1B(s))
