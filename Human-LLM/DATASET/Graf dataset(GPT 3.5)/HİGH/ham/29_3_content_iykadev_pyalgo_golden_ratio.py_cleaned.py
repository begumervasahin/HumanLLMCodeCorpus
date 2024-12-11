def fonk1(n):
	a1 = 1
	a2 = 1
	for i in range(2,n):
		b1 = a1 + a2
		a1 = a2
		a2 = b1
		b2 = (a2 * 1.0 / a1)
		print(b2)
def fonk2(n):
	fonk1(n)
fonk2(1476)
"""
         7376 function calls in 0.125 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2948    0.031    0.000    0.031    0.000 :0(charmap_encode)
        1    0.000    0.000    0.125    0.125 :0(exec)
     1474    0.078    0.000    0.125    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
     2948    0.016    0.000    0.047    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.125    0.125 golden_ratio.py:1(<module>)
        1    0.000    0.000    0.125    0.125 golden_ratio.py:1(golden_ratio)
        1    0.000    0.000    0.125    0.125 golden_ratio.py:11(golden_ratio_ma
in)
        1    0.000    0.000    0.125    0.125 profile:0(<code object <module> at
 0x01DCC2A0, file "golden_ratio.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""