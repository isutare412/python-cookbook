from decimal import Decimal
from decimal import localcontext
import math

a = 2.1
b = 4.2
c = a + b
print(c)
print(c == 6.3)

a = Decimal('2.1')
b = Decimal('4.2')
c = a + b
print(c)
print(c == Decimal('6.3'))

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
print(math.fsum(nums))
