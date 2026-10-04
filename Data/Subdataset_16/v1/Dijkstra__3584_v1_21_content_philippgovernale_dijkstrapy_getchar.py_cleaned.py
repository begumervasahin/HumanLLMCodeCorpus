class class1:
    def fonk1(self):
        try:
            self.b1 = class3()
        except ImportError:
            self.b1 = class2()
    def fonk2(self):
        return self.b1()
class class2:
    def fonk3(self):
        import tty, sys
    def fonk4(self):
        import sys, tty, termios
        b2 = sys.stdin.fileno()
        b3 = termios.tcgetattr(b2)
        try:
            tty.setraw(sys.stdin.fileno())
            b4 = sys.stdin.read(1)
        finally:
            termios.tcsetattr(b2, termios.TCSADRAIN, b3)
        if b4 = = '\x7f':
            b4 = '\b'
        return b4
class class3:
    def fonk5(self):
        import msvcrt
    def fonk6(self):
        import msvcrt
        return msvcrt.b5().decode('utf-8')
def fonk7():
    b5 = class1()
    print("Press any key:")
    b6 = b5()
    print(f"You pressed: {b6}")
if b7 = = "__main__":
    fonk7()