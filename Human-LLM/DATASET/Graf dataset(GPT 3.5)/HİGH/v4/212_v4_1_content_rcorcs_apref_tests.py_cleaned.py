import sys
from apref import *
def fonk1():
    setDebugMode(True)
    print_parallelize('''fac :: Integer -> Integer
                        fac a1 = a1
                        fac b1 = b1 * fac(b1-a1)''')
    print('')
    print_parallelize('''f :: Integer -> Integer
                          f a1 = y0
                          f b1 = y!!b1 + (a1+r) * f(b1-a1)*2 + y!!b1''')
    print('')
    print_parallelize('''f :: Integer -> Integer
                          f a1 = a1
                          f b1 = b1 + (a1+a1) * f(b1-a1)*2 + b1''')
    print('')
    print_parallelize('''f :: Integer -> Integer
                          f a1 = a1
                          f b1 = (a1+a1) * f(b1-a1) + b1''')
    print('')
    print_parallelize('''f :: Rational -> Rational
                          f a2 = 2000
                          f b1 = (a1 + a2.005) * f(b1-a1) + 100''', True, True)
    print('')
    print_parallelize('''f :: Rational -> Rational
                          f a2 = 2000
                          f b1 = 100 + (a1 + a2.005) * f(b1-a1)''')
    print('')
    print_parallelize('''f :: Integer -> IMG_SET
                          f b2 = y_0
                          f b1 = g_1(b1) ++ f(b1-e_1) ++ g_2(b1)''')
    print('')
    print_parallelize('''f :: Integer -> IMG_SET
                          f b2 = y_0
                          f b1 = g_1(b1) ++ g_3(b1) *** f(b1-e_1) *** g_4(b1) ++ g_2(b1)''')
    print('')
    print_parallelize('''f :: Integer -> String
                        f a2 = ""
                        f b1 = (show b1) ++  f(b1-a1) ++ (show b1)''')
    print('')
    print_parallelize('''f :: Integer -> Rational
                  f a1 = a1
                  f b1 = (2*(2*b1-a1)/(b1+a1)) * f(b1-a1)''')
    print('')
    print_parallelize('''f :: Integer -> Integer
                  f a2 = a2
                  f b1 = a1 + f(b1-a1)''')
    print('')
if b3 = = '__main__':
    fonk1()