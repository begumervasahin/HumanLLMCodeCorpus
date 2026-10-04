import onetimepad
class EncryptFrame(onetimepad.EncryptFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
def main() -> None:
    encrypt_frame = EncryptFrame()
    print("EncryptFrame instance created")
if __name__ == "__main__":
    main()