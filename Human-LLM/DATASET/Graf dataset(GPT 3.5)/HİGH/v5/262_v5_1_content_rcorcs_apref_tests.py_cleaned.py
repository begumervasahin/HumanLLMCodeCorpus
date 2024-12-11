import sys
from apref import *
def fonk1():
    setDebugMode(True)
    b1 = [
        "fac :: Integer -> Integer\nfac b2 = b2\nfac n = n * fac(n-b2)",
        "f :: Integer -> Integer\nf b2 = y0\nf n = y!!n + (b2+r) * f(n-b2)*2 + y!!n",
        "f :: Integer -> Integer\nf b2 = b2\nf n = n + (b2+b2) * f(n-b2)*2 + n",
        "f :: Integer -> Integer\nf b2 = b2\nf n = (b2+b2) * f(n-b2) + n",
        "f :: Rational -> Rational\nf b3 = 2000\nf n = (b2 + b3.005) * f(n-b2) + 100",
        "f :: Rational -> Rational\nf b3 = 2000\nf n = 100 + (b2 + b3.005) * f(n-b2)",
        "f :: Integer -> IMG_SET\nf b4 = y_0\nf n = g_1(n) ++ f(n-e_1) ++ g_2(n)",
        "f :: Integer -> IMG_SET\nf b4 = y_0\nf n = g_1(n) ++ g_3(n) *** f(n-e_1) *** g_4(n) ++ g_2(n)",
        "f :: Integer -> String\nf b3 = ''\nf n = (show n) ++  f(n-b2) ++ (show n)",
        "f :: Integer -> Rational\nf b2 = b2\nf n = (2*(2*n-b2)/(n+b2)) * f(n-b2)",
        "f :: Integer -> Integer\nf b3 = b3\nf n = b2 + f(n-b2)"
    ]
    for example in b1:
        print_parallelize(example)
        print('')
if b5 = = '__main__':
    fonk1()