import file_operations as file_op
import additive_shares
import threshold_shares
import time
def refresh_additive_shares():
    current_additive_shares = file_op.read_list("FadditiveShares")
    modulus = file_op.read_list("FmodulusRSA")[0]
    new_shares = [0] * len(current_additive_shares)
    for share in current_additive_shares:
        divided_shares = additive_shares.additive_sharing(share, len(current_additive_shares))
        new_shares = [sum(pair) for pair in zip(new_shares, divided_shares)]
    file_op.write_list("FadditiveShares", new_shares)
    print("Updating shares...")
    threshold_shares.threshold_additive_shares()
    print("Update complete.")
def proactive_refresh_timer():
    while True:
        refresh_additive_shares()
        try:
            perform_signature_operations()
        except Exception as e:
            print(f"An error occurred during signature operations: {e}")
        time.sleep(15)
def perform_signature_operations():
    print("Original shares: ", additive_shares)
if __name__ == '__main__':
    refresh_additive_shares()