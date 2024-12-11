import file_operations as file_op
import additive_shares
import threshold_shares
import time
def fonk1():
    b1 = file_op.read_list("FadditiveShares")
    b2 = file_op.read_list("FmodulusRSA")[0]
    b3 = [0] * len(b1)
    for share in b1:
        b4 = additive_shares.additive_sharing(share, len(b1))
        b3 = [sum(pair) for pair in zip(b3, b4)]
    file_op.write_list("FadditiveShares", b3)
    print("Updating shares...")
    threshold_shares.threshold_additive_shares()
    print("Update complete.")
def fonk2():
    while True:
        fonk1()
        try:
            fonk3()
        except Exception as e:
            print(f"An error occurred during signature operations: {e}")
        time.sleep(15)
def fonk3():
    print("Original shares: ", additive_shares)
if b5 = = '__main__':
    fonk1()