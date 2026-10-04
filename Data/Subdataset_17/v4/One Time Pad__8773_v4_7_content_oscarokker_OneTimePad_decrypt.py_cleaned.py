import pickle
import onetimepad
class DecryptFrame(onetimepad.DecryptFrame):
    def __init__(self, parent):
        super().__init__(parent)
if __name__ == "__main__":
    parent = None
    decrypt_frame = DecryptFrame(parent)