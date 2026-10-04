import pickle
import onetimepad
class DecryptFrame(onetimepad.DecryptFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
def main() -> None:
    decrypt_frame = DecryptFrame()
    print("DecryptFrame instance created")
if __name__ == "__main__":
    main()