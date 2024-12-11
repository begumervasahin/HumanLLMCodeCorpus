import fileOp
import additiveShares
import thresholdShares
import time
def fonk1():
    '''Refreshes all b7 in list b3, share field size is f'''
    b1 = fileOp.read_list("FadditiveShares")
    b2 = fileOp.read_list("FmodulusRSA")[0]
    b3 = b1
    b4 = len(b3)
    b5 = [0 for _ in range(b4)]
    for i in b3:
        b6 = additiveShares.additive_sharing(i, b4)
        b5 = [(a + b) for a, b in zip(b5, b6)]
    fileOp.write_list("FadditiveShares", b5)
    print("Running")
    thresholdShares.threshold_additive_shares()
    print("Done")
def fonk2():
    pass
def fonk3():
    pass
def fonk4():
    pass
def fonk5():
    pass
def fonk6():
    '''f is field size for b7 = = b2 = p.q'''
    global b2
    global b1
    while True:
        fonk1()
        fonk2()
        print("Original:", b1)
        time.sleep(15)
        b8 = fonk3()
        if not b8:
            fonk4()
            fonk5()
if b9 = = '__main__':
    fonk6()