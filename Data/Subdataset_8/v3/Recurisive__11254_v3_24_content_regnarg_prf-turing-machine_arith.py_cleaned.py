from prf import *
id_func = Proj(1, 0)
one = C(S, zero)
S3 = C(S, Proj(3, 0))
def accelerate(function, operation, arity):
    accelerated_func = function
    for _ in range(arity):
        accelerated_func = PR(accelerated_func, Proj(arity + 1, _))
    accelerated_func = accel(accelerated_func, operation, arity)
    return accelerated_func
addition = accelerate(id_func, lambda x, y: x + y, 2)
def predecessor_operation(x):
    return x - 1 if x > 0 else 0
predecessor = C(PR(id_func, Proj(3, 1)), Proj(1, 0), Proj(1, 0))
predecessor = accelerate(predecessor, predecessor_operation, 1)
pred3 = C(predecessor, Proj(3, 0))
def subtraction_operation(x, y):
    return x - y if x >= y else 0
subtraction = accelerate(id_func, subtraction_operation, 2)
def multiplication_operation(x, y):
    return x * y
multiplication = accelerate(zero, multiplication_operation, 2)
def power_operation(x, y):
    return x ** y
power = accelerate(one, power_operation, 2)