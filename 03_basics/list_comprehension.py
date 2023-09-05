# list_comprehension.py

# Tershire
# 2023 SEP 05


import sys
import pprint


# list comprehension //////////////////////////////////////////////////////////
# list ========================================================================
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)
print(a)

a = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
print(a)

# dictionary ==================================================================
date = {"year": 2023, "month": "SEP", "day": 5}
b = {}
for key, value in date.items():
    b[key] = value
print(b)

b = {key: value for key, value in date.items()}
print(b)

# generator ///////////////////////////////////////////////////////////////////
def natural_number_generator():
    n = 0
    while True:
        n += 1
        yield n

print(natural_number_generator())

natural_number_generator = natural_number_generator()
for _ in range(0, 7):
    n = next(natural_number_generator)
    print(n)

def multi_type_generator():
    yield 7
    yield "my"
    yield True

multi_type_generator = multi_type_generator()
for _ in range(0, 3):
    print(next(multi_type_generator))

# range ///////////////////////////////////////////////////////////////////////
a = [n for n in range(int(1E6))]
b = range(int(1E6))

print(len(a), len(b))
print(sys.getsizeof(a), sys.getsizeof(b))

# enumerate ///////////////////////////////////////////////////////////////////
a = ['a1', 'b2', 'c3']
b = [(i, val) for (i, val) in enumerate(a)]
for i, val in enumerate(a):
    print(i, val)

# int division ////////////////////////////////////////////////////////////////
print(5 / 3)
print(5 // 3, 5 % 3)
print(divmod(5, 3))

# print ///////////////////////////////////////////////////////////////////////
a = ['A', 'B', 'C', 'D', 'E']
b = [(i, val) for (i, val) in enumerate(a)]
for element in b:
    print(element, end=" ") # print in line
print()

# list
print(' '.join(a))

# fstring
for i, val in enumerate(a):
    print(f"{i + 1}: {val}", end=', ')
print()

# pass ////////////////////////////////////////////////////////////////////////
class Edge_Reprojection():
    def compute_error(self):
        a = 3
        pprint.pprint(locals()) # print all local variables
        pass

# locals //////////////////////////////////////////////////////////////////////
edge_reporjection = Edge_Reprojection()
edge_reporjection.compute_error()
