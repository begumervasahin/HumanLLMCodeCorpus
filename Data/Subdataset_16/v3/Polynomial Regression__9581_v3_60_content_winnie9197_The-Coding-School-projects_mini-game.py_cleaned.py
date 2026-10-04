import random
import signal
import sys
import tty
import termios
class class1:
    def fonk1(self):
        self.b1 = "b1"
        self.b2 = "b2"
        self.fonk2()
        self.b3 = self.fonk3()
        self.fonk4()
    def fonk2(self):
        print("Would you like to b4 the obstacles? [Enter Y/N]")
        b4 = self.fonk7()
        if b4.lower() == 'y':
            self.b1 = input("What would you like 'o' to represent? ") or self.b1
            self.b2 = input("What would you like 'O' to represent? ") or self.b2
    def fonk3(self):
        a1 = 50
        a2 = 68
        a3 = 95
        return ''.join(
            'X' if (step := random.randint(0, 100)) <= a2 else 'o' if step <= a3 else 'O'
            for _ in range(a1)
        )
    def fonk4(self):
        print("The game starts now. Quick, press 'd' to advance or 'a' to dodge.")
        for b6 in self.b3:
            print(b6)
            signal.signal(signal.SIGALRM, self._handle_timeout)
            signal.alarm(2)
            try:
                b5 = self.fonk7()
                if not self.fonk5(b5, b6):
                    break
            except Exception:
                print("You're too slow! You lost!")
                break
            finally:
                signal.alarm(0)
    def fonk5(self, b5, b6):
        try:
            if b5 = = 'a':
                if b6 not in ('o', 'O'):
                    raise ValueError("You've diverted from the right track! You lost!")
            elif b5 = = 'd':
                if b6 != 'X':
                    raise ValueError(f"You hit a {self.b1 if b6 = = 'o' else self.b2}! You lost!")
            else:
                raise ValueError("Please enter a valid command!")
            return True
        except ValueError as e:
            print(e)
            return False
    def fonk6(self, signum, frame):
        raise Exception()
    def fonk7(self):
        b7 = sys.stdin.fileno()
        b8 = termios.tcgetattr(b7)
        try:
            tty.setraw(b7)
            b9 = sys.stdin.read(1)
        finally:
            termios.tcsetattr(b7, termios.TCSADRAIN, b8)
        return b9
if b10 = = "__main__":
    class1()