# key_takeaways.py

# Tershire
# 2023 SEP 27


import re
import collections

# string | list reverse ///////////////////////////////////////////////////////
a = "abcde"
# check simple palindrome
print(a == a[::-1])

# reverse
a = a[::-1]
print(a)

b = ["a", "b", "c", "d", "e"]
b.reverse()
print(b)


# sort key & lambda ///////////////////////////////////////////////////////////
# also, multiple criteria example (key=<criteria in priority>))
# following criteria are applied,
# when the results of the previous criterion are the same
def function(x: str) -> (str, str):
    x_split = x.split()
    return x_split[1:], x_split[0]


logs = ["zoey i love you", "lucas i love you", "rong i love you"]

# <M1> sort key & user-defined function
logs.sort(key=function)
print(logs)

# <M2> sort key & lambda function
logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(logs)


# ex) -------------------------------------------------------------------------
def first_then_last(x: str) -> (str, str):
    return x[0], x[-1]


codes = ["b0a", "a0b", "a1a"]

print(sorted(codes))

codes.sort(key=first_then_last)
print(codes)


# sort a string ///////////////////////////////////////////////////////////////
text = "bca"
print("".join(sorted(text)))


# re (regular expression) /////////////////////////////////////////////////////
# how to split a string with multiple delimiters:
paragraph = "Hi. My name* is, well;, 'HAPPY'?!"

# <M1> if the list of delimiters given
print(re.sub("[!?',;.]", " ", paragraph.lower()))

# <M2> if not given
#  ^: means "except"
# \w: means [a-zA-Z0-9_]
print(re.sub("[^\w]", " ", paragraph.lower()))


# max: usage with dict ////////////////////////////////////////////////////////
# how to find the key for the max value in a dict
letters = ["a", "b", "b", "b", "c", "c"]
counts = collections.Counter(letters)
print(counts)

# <M1> max on dict
max_key = max(counts, key=counts.get)
print(max_key, counts[max_key])

# <M2> .most_common() (Counter)
max_items = counts.most_common(1)
print(max_items)
