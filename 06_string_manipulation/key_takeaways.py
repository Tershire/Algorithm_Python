# key_takeaways.py

# Tershire
# 2023 SEP 27


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
