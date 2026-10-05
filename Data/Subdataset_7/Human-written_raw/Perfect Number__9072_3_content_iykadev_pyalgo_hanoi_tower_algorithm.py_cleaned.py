def fonk1(b1, x, y, z):
	if b1 = = 1:
		print("Diski %s Ã§ubuÄundan %s Ã§ubuÄuna koy" % (x,z))
	else:
		fonk1(b1-1, x, z, y)
		fonk1(1, x, y, z)
		fonk1(b1-1, y, x, z)
def fonk2(ndisc):
	fonk1(ndisc, "A", "B", "C")
fonk2(10)
"""
         6654 function calls (5121 primitive calls) in 0.078 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2046    0.000    0.000    0.000    0.000 :0(charmap_encode)
        1    0.000    0.000    0.078    0.078 :0(exec)
     1023    0.062    0.000    0.078    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
     2046    0.016    0.000    0.016    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(<module
>)
   1534/1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(hanoi_t
ower_algorithm)
        1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:44(hanoi_
tower_algorithm_main)
        1    0.000    0.000    0.078    0.078 profile:0(<code object <module> at
 0x01DCC2A0, file "hanoi_tower_algorithm.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""