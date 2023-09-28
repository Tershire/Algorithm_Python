# Q04_most_common_word.py
# LeetCode #819

# Tershire
# 2023 SEP 28


import re
import collections


# KEY TAKEAWAY ****************************************************************
# > re
# \w means [a-zA-Z0-9_]


# case ////////////////////////////////////////////////////////////////////////
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# paragraph = "a."
# banned = []

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# simple append & dict Counter
# 40 [ms]
def f1(paragraph: str, banned: list[str]) -> str:
    # pre-processing
    paragraph = re.sub("[!?',;.]", " ", paragraph.lower())
    # paragraph = re.sub("[^a-z0-9 ]", "", paragraph.lower())

    # remove banned words
    clean_words = []
    words = paragraph.split()
    for word in words:
        if word not in banned:
            clean_words.append(word)

    # word histogram
    word_counts = collections.Counter(clean_words)

    # find the max
    return word_counts.most_common(1)[0][0]

# -----------------------------------------------------------------------------
# list comprehension & dict Counter
# 48 [ms]
def f1B(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub("[^\w]", " ", paragraph)
        .lower().split() if word not in banned]

    word_counts = collections.Counter(words)

    return word_counts.most_common(1)[0][0]


# test ////////////////////////////////////////////////////////////////////////
print(f1(paragraph, banned))
print(f1B(paragraph, banned))
