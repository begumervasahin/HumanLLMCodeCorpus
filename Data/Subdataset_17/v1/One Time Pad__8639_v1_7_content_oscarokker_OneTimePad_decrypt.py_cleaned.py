import pickle
import onetimepad
class DecryptFrame(onetimepad.DecryptFrame):
    def __init__(self, parent):
        super().__init__(parent)
def main():
    parent = None
    decrypt_frame = DecryptFrame(parent)
    print("DecryptFrame instance created")
if __name__ == "__main__":
    main()