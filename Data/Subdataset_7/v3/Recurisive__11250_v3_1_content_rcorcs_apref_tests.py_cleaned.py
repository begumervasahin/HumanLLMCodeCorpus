import sys
from apref import *
if b1 = = '__main__':
    setDebugMode(True)
    b2 = '''
                        fac :: Integer -> Integer
                        fac a1 = a1
                        fac b3 = b3 * fac(b3-a1)
                        '''
    b4 = '''
                        f :: Integer -> Integer
                        f a1 = y0
                        f b3 = y!!b3 + (a1+r) * f(b3-a1)*2 + y!!b3
                        '''
    b5 = '''
                        f :: Integer -> Integer
                        f a1 = a1
                        f b3 = b3 + (a1+a1) * f(b3-a1)*2 + b3
                        '''
    b6 = '''
                        f :: Integer -> Integer
                        f a1 = a1
                        f b3 = (a1+a1) * f(b3-a1) + b3
                        '''
    print(parallelize(b2))
    print('')
    print(parallelize(b4))
    print('')
    print(parallelize(b5))
    print('')
    print(parallelize(b6))
    print('')
    b7 = '''
                        f :: Rational -> Rational
                        f a2 = 2000
                        f b3 = (a1 + a2.005) * f(b3-a1) + 100
                        '''
    b8 = '''
                        f :: Rational -> Rational
                        f a2 = 2000
                        f b3 = 100 + (a1 + a2.005) * f(b3-a1)
                        '''
    print(parallelize(b7, True, True))
    print('')
    print(parallelize(b8))
    print('')
    b9 = '''
                            f :: Integer -> IMG_SET
                            f b10 = y_0
                            f b3 = g_1(b3) ++ f(b3-e_1) ++ g_2(b3)
                            '''
    b11 = '''
                            f :: Integer -> IMG_SET
                            f b10 = y_0
                            f b3 = g_1(b3) ++ g_3(b3) *** f(b3-e_1) *** g_4(b3) ++ g_2(b3)
                            '''
    print(parallelize(b9))
    print('')
    print(parallelize(b11))
    print('')
    b12 = '''
                    f :: Integer -> String
                    f a2 = ""
                    f b3 = (show b3) ++  f(b3-a1) ++ (show b3)
                    '''
    print(parallelize(b12))
    print('')
    b13 = '''
                    f :: Integer -> Rational
                    f a1 = a1
                    f b3 = (2*(2*b3-a1)/(b3+a1)) * f(b3-a1)
                    '''
    print(parallelize(b13))
    print('')
    b14 = '''
                        f :: Integer -> Integer
                        f a2 = a2
                        f b3 = a1 + f(b3-a1)
                        '''
    print(parallelize(b14))
    print('')