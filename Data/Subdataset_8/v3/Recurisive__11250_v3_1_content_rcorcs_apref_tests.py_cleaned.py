import sys
from apref import *
if __name__ == '__main__':
    setDebugMode(True)
    recursive_func_1 = '''
                        fac :: Integer -> Integer
                        fac 1 = 1
                        fac n = n * fac(n-1)
                        '''
    recursive_func_2 = '''
                        f :: Integer -> Integer
                        f 1 = y0
                        f n = y!!n + (1+r) * f(n-1)*2 + y!!n
                        '''
    recursive_func_3 = '''
                        f :: Integer -> Integer
                        f 1 = 1
                        f n = n + (1+1) * f(n-1)*2 + n
                        '''
    recursive_func_4 = '''
                        f :: Integer -> Integer
                        f 1 = 1
                        f n = (1+1) * f(n-1) + n
                        '''
    print(parallelize(recursive_func_1))
    print('')
    print(parallelize(recursive_func_2))
    print('')
    print(parallelize(recursive_func_3))
    print('')
    print(parallelize(recursive_func_4))
    print('')
    rational_func_1 = '''
                        f :: Rational -> Rational
                        f 0 = 2000
                        f n = (1 + 0.005) * f(n-1) + 100
                        '''
    rational_func_2 = '''
                        f :: Rational -> Rational
                        f 0 = 2000
                        f n = 100 + (1 + 0.005) * f(n-1)
                        '''
    print(parallelize(rational_func_1, True, True))
    print('')
    print(parallelize(rational_func_2))
    print('')
    custom_type_func_1 = '''
                            f :: Integer -> IMG_SET
                            f e_0 = y_0
                            f n = g_1(n) ++ f(n-e_1) ++ g_2(n)
                            '''
    custom_type_func_2 = '''
                            f :: Integer -> IMG_SET
                            f e_0 = y_0
                            f n = g_1(n) ++ g_3(n) *** f(n-e_1) *** g_4(n) ++ g_2(n)
                            '''
    print(parallelize(custom_type_func_1))
    print('')
    print(parallelize(custom_type_func_2))
    print('')
    string_func = '''
                    f :: Integer -> String
                    f 0 = ""
                    f n = (show n) ++  f(n-1) ++ (show n)
                    '''
    print(parallelize(string_func))
    print('')
    series_func = '''
                    f :: Integer -> Rational
                    f 1 = 1
                    f n = (2*(2*n-1)/(n+1)) * f(n-1)
                    '''
    print(parallelize(series_func))
    print('')
    addition_func = '''
                        f :: Integer -> Integer
                        f 0 = 0
                        f n = 1 + f(n-1)
                        '''
    print(parallelize(addition_func))
    print('')