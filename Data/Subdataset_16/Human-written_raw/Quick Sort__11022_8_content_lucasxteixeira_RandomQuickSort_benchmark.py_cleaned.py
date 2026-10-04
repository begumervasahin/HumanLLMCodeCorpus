import timeit
print( "Quick Sort" )
print( "One thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(1000)]
from quickSort import quickSort
'''
print( min( timeit.Timer('b3 = b2[:]; quickSort(0, 1000, b3)', b1=b1).repeat(10, 100) ) )
print( "Ten thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(10000)]
from quickSort import quickSort
'''
print( min( timeit.Timer('b3 = b2[:]; quickSort(0, 10000, b3)', b1=b1).repeat(10, 100) ) )
print( "One hundred thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(100000)]
from quickSort import quickSort
'''
print( min( timeit.Timer('b3 = b2[:]; randomQuickSort(0, 100000, b3)', b1=b1).repeat(10, 100) ) )
print( "Random Quick Sort" )
print( "One thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(1000)]
from randomQuickSort import randomQuickSort
'''
print( min( timeit.Timer('b3 = b2[:]; randomQuickSort(0, 1000, b3)', b1=b1).repeat(10, 100) ) )
print( "Ten thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(10000)]
from randomQuickSort import randomQuickSort
'''
print( min( timeit.Timer('b3 = b2[:]; randomQuickSort(0, 10000, b3)', b1=b1).repeat(10, 100) ) )
print( "One hundred thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(100000)]
from randomQuickSort import randomQuickSort
'''
print( min( timeit.Timer('b3 = b2[:]; randomQuickSort(0, 100000, b3)', b1=b1).repeat(10, 100) ) )
print( "Median Random Quick Sort" )
print( "One thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(1000)]
from medianRandomQuickSort import medianRandomQuickSort
'''
print( min( timeit.Timer('b3 = b2[:]; medianRandomQuickSort(0, 1000, b3)', b1=b1).repeat(10, 100) ) )
print( "Ten thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(10000)]
from medianRandomQuickSort import medianRandomQuickSort
'''
print( min( timeit.Timer('b3 = b2[:]; medianRandomQuickSort(0, 10000, b3)', b1=b1).repeat(10, 100) ) )
print( "One hundred thousand elements" )
b1 = '''
import random
random.seed('12345')
b2 = [random.random() for i in range(100000)]
from medianRandomQuickSort import medianRandomQuickSort
'''
print( min( timeit.Timer('b3 = b2[:]; medianRandomQuickSort(0, 100000, b3)', b1=b1).repeat(10, 100) ) )