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
        b4 = self.fonk6()
        if b4.lower() == 'y':
            self.b1 = input("What would you like 'o' to represent? ") or self.b1
            self.b2 = input("What would you like 'O' to represent? ") or self.b2
    def fonk3(self):
        b5 = []
        a1 = 50
        low, b6 = 0, 100
        one_sd, b7 = 68, 95
        for _ in range(a1):
            b8 = random.randint(low, b6)
            if b8 <= one_sd:
                b5.append('X')
            elif one_sd < b8 <= b7:
                b5.append('o')
            elif b8 > b7:
                b5.append('O')
        return ''.join(b5)
    def fonk4(self):
        print("The game starts now. Quick, press 'd' to advance or 'a' to dodge.")
        for b10 in self.b3:
            print(b10)
            signal.signal(signal.SIGALRM, self._handle_timeout)
            signal.alarm(2)
            try:
                b9 = self.fonk6()
                if b9 = = 'a':
                    if b10 not in ('o', 'O'):
                        raise ValueError("You've diverted from the right track! You lost!")
                elif b9 = = 'd':
                    if b10 != 'X':
                        raise ValueError(f"You hit a {self.b1 if b10 = = 'o' else self.b2}! You lost!")
                else:
                    raise ValueError("Please enter a valid command!")
            except ValueError as e:
                print(e)
                break
            except Exception:
                print("You're too slow! You lost!")
                break
            finally:
                signal.alarm(0)
    def fonk5(self, signum, frame):
        raise Exception()
    def fonk6(self):
        b11 = sys.stdin.fileno()
        b12 = termios.tcgetattr(b11)
        try:
            tty.setraw(b11)
            b13 = sys.stdin.read(1)
        finally:
            termios.tcsetattr(b11, termios.TCSADRAIN, b12)
        return b13
if b14 = = "__main__":
    class1()