
from db import cursor
from finders import find_user, find_product
user_id = 123
user = find_user(cursor, user_id)
product_id = 456
product = find_product(cursor, product_id)
