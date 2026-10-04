import pickle
import onetimepad
class EncryptFrame(onetimepad.EncryptFrame):
    def __init__(self, parent):
        super().__init__(parent)
def main() -> None:
    parent = None
    encrypt_frame = EncryptFrame(parent)
    print("EncryptFrame instance created")
if __name__ == "__main__":
    main()