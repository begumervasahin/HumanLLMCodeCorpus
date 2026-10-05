import math
def hanoi_tower_algorithm(n, x, y, z):
    if n == 1:
        print("Diski %s çubuðundan %s çubuðuna koy" % (x, z))
    else:
        hanoi_tower_algorithm(n-1, x, z, y)
        hanoi_tower_algorithm(1, x, y, z)
        hanoi_tower_algorithm(n-1, y, x, z)
def hanoi_tower_algorithm_main(ndisc):
    hanoi_tower_algorithm(ndisc, "A", "B", "C")
def profile_results():
    return """
         6654 function calls (5121 primitive calls) in 0.078 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2046    0.000    0.000    0.000    0.000 :0(charmap_encode)
        1    0.000    0.000    0.078    0.078 :0(exec)
     1023    0.062    0.000    0.078    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
     2046    0.016    0.000    0.016    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(<module>)
   1534/1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(hanoi_tower_algorithm)
        1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:44(hanoi_tower_algorithm_main)
        1    0.000    0.000    0.078    0.078 profile:0(<code object <module> at 0x01DCC2A0, file "hanoi_tower_algorithm.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
    """
if __name__ == "__main__":
    ndisc = 10
    print("Executing Hanoi Tower Algorithm with", ndisc, "discs:")
    hanoi_tower_algorithm_main(ndisc)
    print("\nProfiling Results:")
    print(profile_results())