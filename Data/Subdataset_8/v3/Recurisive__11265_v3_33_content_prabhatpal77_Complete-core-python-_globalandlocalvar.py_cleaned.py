
GLOBAL_A = 1000
GLOBAL_B = 2000
def f1():
    local_p = 3000
    local_q = 4000
    print("Inside f1:")
    print("Global A:", GLOBAL_A)
    print("Global B:", GLOBAL_B)
    print("Local P:", local_p)
    print("Local Q:", local_q)
def f2():
    local_x = 5000
    local_y = 6000
    print("Inside f2:")
    print("Global A:", GLOBAL_A)
    print("Global B:", GLOBAL_B)
    print("Local X:", local_x)
    print("Local Y:", local_y)
f1()
f2()