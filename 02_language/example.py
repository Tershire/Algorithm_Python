# example.py

# Tershire
# 2023 SEP 05


# M1
num = 0
for i in range(1, 10 + 1):
    num += i
print(num)

# M2
num = sum(i for i in range(1, 10 + 1))
print(num)

# M3
num = sum(range(1, 10 + 1))
print(num)
