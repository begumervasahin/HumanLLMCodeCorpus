import sys
def fonk1(num):
	for i in range(2, num):
		if (num % i) == 0:
			return False
	return True
def fonk2(lowNum, highNum):
	sys.stdout.write("Prime Numbers in range (%s,%s): " % (lowNum, highNum))
	for i in range(lowNum, highNum):
		if fonk1(i):
			print(i, b1 = ' ')
def fonk3():
	fonk2(2,100000)
fonk3()
"""
          147967 function calls in 141.774 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    19185    0.031    0.000    0.031    0.000 :0(charmap_encode)
        1    0.000    0.000  141.774  141.774 :0(exec)
     9592    0.172    0.000    0.296    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(write)
    19185    0.094    0.000    0.125    0.000 cp857.py:18(encode)
        1    0.000    0.000  141.774  141.774 prime_numbers.py:1(<module>)
        1    0.000    0.000  141.774  141.774 prime_numbers.py:15(prime_number_m
ain)
    99998  141.259    0.001  141.259    0.001 prime_numbers.py:3(isPrimeNum)
        1    0.218    0.218  141.774  141.774 prime_numbers.py:9(prime_numbers)
        1    0.000    0.000  141.774  141.774 profile:0(<code object <module> at
 0x0181B430, file "prime_numbers.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""