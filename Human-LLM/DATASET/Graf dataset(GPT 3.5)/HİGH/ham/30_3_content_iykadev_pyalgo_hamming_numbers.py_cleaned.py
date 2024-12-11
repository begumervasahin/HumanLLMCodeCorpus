import sys
sys.setrecursionlimit(10000)
def fonk1(b1):
	if b1 = = 1:
		return 1
	if b1 % b2 = = 0:
		return fonk1(b1/b2)
	if b1 % b3 = = 0:
		return fonk1(b1/b3)
	if b1 % b4 = = 0:
		return fonk1(b1/b4)
	return 0
def fonk2(b1):
	if b1 = = 1:
		return 1
	fonk2(b1-1)
	if fonk1(b1) == True:
		print("%s" % b1, b5 = ' ')
def fonk3():
	sys.stdout.write("Hamming Numbers: ")
	fonk2(9830)
fonk3()
"""
         37722 function calls (10704 primitive calls) in 0.156 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      347    0.000    0.000    0.000    0.000 :0(charmap_encode)
        1    0.000    0.000    0.140    0.140 :0(exec)
      173    0.000    0.000    0.000    0.000 :0(print)
        1    0.016    0.016    0.016    0.016 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(setrecursionlimit)
        1    0.000    0.000    0.000    0.000 :0(write)
      347    0.000    0.000    0.000    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.140    0.140 hamming_numbers.py:1(<module>)
   9830/1    0.062    0.000    0.140    0.140 hamming_numbers.py:15(hamming_numb
ers)
        1    0.000    0.000    0.140    0.140 hamming_numbers.py:22(hamming_numb
ers_main)
27018/9829    0.078    0.000    0.078    0.000 hamming_numbers.py:4(is_hamming_n
umbers)
        1    0.000    0.000    0.156    0.156 profile:0(<code object <module> at
 0x0178C390, file "hamming_numbers.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""