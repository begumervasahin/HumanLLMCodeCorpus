import math
def fonk1(b1, source, auxiliary, target):
    if b1 = = 1:
        print(f"Move disk from {source} to {target}")
    else:
        fonk1(b1 - 1, source, target, auxiliary)
        fonk1(1, source, auxiliary, target)
        fonk1(b1 - 1, auxiliary, source, target)
def fonk2(ndiscs):
    print(f"Executing Tower of Hanoi Algorithm with {ndiscs} discs:")
    fonk1(ndiscs, "A", "B", "C")
def fonk3():
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
if b2 = = "__main__":
    a1 = 10
    fonk2(a1)
    print("\nProfiling Results:")
    print(fonk3())