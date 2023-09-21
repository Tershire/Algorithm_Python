# Q01_valid_palindrome.py

# Tershire
# 2023 SEP 21


from typing import Deque
import collections
import re


# case ////////////////////////////////////////////////////////////////////////
s = "A man, a plan, a canal: Panama"
# s = "a"
# s = ""

# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# two-pointer
# 50 [ms]
def f1(s: str) -> bool:
    # pre-processing
    chars = []
    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    # exception
    if len(chars) == 0:
        return True

    # main
    i = 0
    while i <= len(chars) / 2:
        if chars[i] != chars[-1 - i]:
            return False
        i += 1

    return True


# -----------------------------------------------------------------------------
# list, pop
# 231 [ms]
def f1B(s: str) -> bool:
    # pre-processing
    chars = []
    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    # main
    while len(chars) > 1:
        if chars.pop(0) != chars.pop():
            return False

    return True


# -----------------------------------------------------------------------------
# deque, pop
# 47 [ms]
def f2B(s: str) -> bool:
    # pre-processing
    chars: Deque = collections.deque()
    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    # main
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False

    return True


# -----------------------------------------------------------------------------
# slicing
# 36 [ms]
def f3B(s: str) -> bool:
    # pre-processing
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)

    # main
    return s == s[::-1]  # flip (written in C internally)


# test ////////////////////////////////////////////////////////////////////////
print(f1(s))
print(f1B(s))
print(f2B(s))
print(f3B(s))
