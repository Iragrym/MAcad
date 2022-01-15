age = 100000000000000000000000000000000000000000000

# print(type(age))

# age = int("")

# 2/0


age = 1.0
my_inf = float('inf')

print(age, type(age))

# eps = 0.0000001
eps = 1e-7

a = 0.1
b = 0.2
c = 0.3

print(
    abs((a + b) - c) < eps
)

from decimal import Decimal
a = Decimal('0.1')
b = 