
from db import cursor
from finders import find_user, find_product
a1 = 123
b1 = find_user(cursor, a1)
a2 = 456
b2 = find_product(cursor, a2)
