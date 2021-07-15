# print(1.1 + 2.2) - 3.3000000000000003 avoid this kind of thing
from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 4 # Precision of 4 decimal places
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))
