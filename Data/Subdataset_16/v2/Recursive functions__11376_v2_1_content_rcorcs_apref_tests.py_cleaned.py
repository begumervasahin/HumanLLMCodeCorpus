import sys
from apref import *
def fonk1():
    setDebugMode(True)
    b1 = [
        '''fac :: Integer -> Integer
           fac a1 = a1
           fac b2 = b2 * fac(b2-a1)''',
        '''f :: Integer -> Integer
           f a1 = y0
           f b2 = y!!b2 + (a1+r) * f(b2-a1)*2 + y!!b2''',
        '''f :: Integer -> Integer
           f a1 = a1
           f b2 = b2 + (a1+a1) * f(b2-a1)*2 + b2''',
        '''f :: Integer -> Integer
           f a1 = a1
           f b2 = (a1+a1) * f(b2-a1) + b2''',
        '''f :: Rational -> Rational
           f a2 = 2000
           f b2 = (a1 + a2.005) * f(b2-a1) + 100''',
        '''f :: Rational -> Rational
           f a2 = 2000
           f b2 = 100 + (a1 + a2.005) * f(b2-a1)''',
        '''f :: Integer -> IMG_SET
           f b3 = y_0
           f b2 = g_1(b2) ++ f(b2-e_1) ++ g_2(b2)''',
        '''f :: Integer -> IMG_SET
           f b3 = y_0
           f b2 = g_1(b2) ++ g_3(b2) *** f(b2-e_1) *** g_4(b2) ++ g_2(b2)''',
        '''f :: Integer -> String
           f a2 = ""
           f b2 = (show b2) ++  f(b2-a1) ++ (show b2)''',
        '''f :: Integer -> Rational
           f a1 = a1
           f b2 = (2*(2*b2-a1)/(b2+a1)) * f(b2-a1)''',
        '''f :: Integer -> Integer
           f a2 = a2
           f b2 = a1 + f(b2-a1)'''
    ]
    for example in b1:
        print(parallelize(example))
        print('')
if b4 = = '__main__':
    fonk1()