# data_type.py

# Tershire
# 2023 SEP 19


import copy


# set /////////////////////////////////////////////////////////////////////////
a = set()
print(a)
print(type(a))

b = {3, 1, 2, 2}
print(b)
print(type(b))

# sequence ////////////////////////////////////////////////////////////////////
# str =========================================================================
a = "apple"
print(id(a))
a = "banana"
print(id(a))
a = "apple"
print(id(a))

# immutable ///////////////////////////////////////////////////////////////////
a = 10
print(id(a))
b = a
print(id(a))
a += 1
print(a, b)
print(id(a), id(b))
a = 10
print(id(a), id(b))
c = 10
print(id(c))

# is and == ///////////////////////////////////////////////////////////////////
a = [3, 1, 2]
b = [3, 1, 2]
print(id(a), id(b))
b = a
print(id(a), id(b))
b = list(a)
print(a is b, a == b)
b = copy.deepcopy(a)
print(a is b, a == b)
