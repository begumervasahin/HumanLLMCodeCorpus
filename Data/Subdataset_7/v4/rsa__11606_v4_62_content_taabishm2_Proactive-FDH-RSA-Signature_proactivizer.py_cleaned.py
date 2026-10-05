import file_operations as file_op
import b1
import threshold_shares
import time
def fonk1():
    '''Refreshes all b7 in the list b3, share field size is f'''
    b1 = file_op.read_list("FadditiveShares")
    b2 = file_op.read_list("FmodulusRSA")[0]
    b3 = b1
    b4 = len(b3)
    b5 = [0] * b4
    for share in b3:
        b6 = b1.additive_sharing(share, b4)
        b5 = [(a + b) for a, b in zip(b5, b6)]
    file_op.write_list("FadditiveShares", b5)
    print("Running")
    threshold_shares.threshold_additive_shares()
    print("Done")
def fonk2():
    '''f is field size for b7 = = n = p.q'''
    global b2
    global b1
    while True:
        fonk1()
        additive_signature()
        print("Original:", b1)
        time.sleep(15)
        b8 = signature_verify()
        if not b8:
            additive_signature_verify()
            invoke_backup()
if b9 = = '__main__':
    fonk1()