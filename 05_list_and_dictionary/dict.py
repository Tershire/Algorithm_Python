# dict.py

# Tershire
# 2023 SEP 19


import collections


# key error ///////////////////////////////////////////////////////////////////
a = {"yellow": 1, "blue": 2, "red": 3}
a["purple"] = 4
print(a)
del a["red"]
print(a)
print(a["blue"])

# print(a["orange"])
# <M1> exception
try:
    print(a["orange"])
except KeyError:
    print("no such key!")

# <M2> pre-check
if "orange" in a:
    print(a["orange"])
else:
    print("no such key!")

# module //////////////////////////////////////////////////////////////////////
# defaultDict =================================================================
a = collections.defaultdict(int)
a["yellow"] = 1
a["blue"] = 2
a["red"] = 3
a["purple"] = 4
print(a)
del a["red"]
print(a)

a["orange"] += 5
print(a["orange"])
print(a)

# Counter =====================================================================
a = ['a', 'b', 'b', 'a', 't', 'h', 'a', 'n', 'k', 'y', 'o', 'u']
b = collections.Counter(a)
print(b)
print(b.most_common(3))
