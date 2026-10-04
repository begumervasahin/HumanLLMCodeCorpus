from prf import *
id = Proj(1, 0)
one = C(S, zero)
def addition(x, y):
    return x + y
S3 = C(S, Proj(3, 0))
add = PR(id, S3)
add = accel(add, addition, 2)
def predecessor(x):
    return x - 1 if x > 0 else 0
pred = C(PR(id, Proj(3, 1)), Proj(1, 0), Proj(1, 0))
pred = accel(pred, predecessor, 1)
pred3 = C(pred, Proj(3, 0))
def subtraction(x, y):
    return x - y if x >= y else 0
rsub = PR(id, pred3)
sub = C(rsub, Proj(2, 1), Proj(2, 0))
sub = accel(sub, subtraction, 2)
def multiplication(x, y):
    return x * y
mul_step = C(add, Proj(3, 0), Proj(3, 2))
mul = PR(zero, mul_step)
mul = accel(mul, multiplication, 2)
def exponentiation(x, y):
    return x ** y
pow_step = C(mul, Proj(3, 0), Proj(3, 2))
rpow = PR(one, pow_step)
pow = C(rpow, Proj(2, 1), Proj(2, 0))
pow = accel(pow, exponentiation, 2)
if __name__ == "__main__":
    print("Addition of 3 and 5:", add(3, 5))
    print("Subtraction of 7 and 2:", sub(7, 2))
    print("Multiplication of 4 and 6:", mul(4, 6))
    print("Exponentiation of 2 to the power 3:", pow(2, 3))
