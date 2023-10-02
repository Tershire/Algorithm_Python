# Q05_group_anagrams.py
# LeetCode #49

# Tershire
# 2023 SEP 30


import collections

# case ////////////////////////////////////////////////////////////////////////
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# defaultdict
# 95 [ms]
def f1(strs: list[str]) -> list[list[str]]:
    roster = collections.defaultdict(list[str])
    for text in strs:
        roster["".join(sorted(text))].append(text)

    return list(roster.values())


# test ////////////////////////////////////////////////////////////////////////
print(f1(strs))
