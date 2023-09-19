# list.py

# Tershire
# 2023 SEP 19


# slicing /////////////////////////////////////////////////////////////////////
a = [1, "hi", True, False, 2, "bye"]
print(a[::2])

# delete & remove /////////////////////////////////////////////////////////////
a = [7, "hi", True, "hi", False, "bye" , 3, 2, 7]
print(a.remove("hi"))
print(a)
print(a.pop(4))
print(a)
del a[2]
print(a)
