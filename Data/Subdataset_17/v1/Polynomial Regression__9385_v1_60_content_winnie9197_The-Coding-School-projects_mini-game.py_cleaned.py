import random
import signal
import sys
import tty
import termios
class StepsMiniGame:
    def __init__(self):
        self.launch()
        self.path = self.generate_path()
        self.game_start()
    def launch(self):
        print("Would you like to customize the obstacles? [Enter Y/N]")
        customize = self.getch()
        if customize.lower() == 'y':
            self.pebble = input("What would you like 'o' to represent? ")
            self.rock = input("What would you like 'O' to represent? ")
        if customize.lower() != 'y' or not self.pebble:
            self.pebble = "pebble"
            self.rock = "rock"
    def generate_path(self):
        path_array = []
        path_length = 50
        low = 0
        high = 100
        one_sd = 68
        two_sd = 95
        for _ in range(path_length):
            step_int = random.randint(low, high)
            if step_int <= one_sd:
                path_array.append('X')
            elif one_sd < step_int <= two_sd:
                path_array.append('o')
            elif step_int > two_sd:
                path_array.append('O')
            else:
                print("something isn't right")
        path = ''.join(path_array)
        return path
    def game_start(self):
        print("The game starts now. Quick, press 'd' to advance or 'a' to dodge.")
        for next_step in self.path:
            print(next_step)
            signal.signal(signal.SIGALRM, self._handle_timeout)
            signal.alarm(2)
            try:
                user_input = self.getch()
                if user_input == 'a':
                    if next_step not in ('o', 'O'):
                        raise ValueError("You've diverted from the right track! You lost!")
                elif user_input == 'd':
                    if next_step != 'X':
                        raise ValueError(f"You hit a {self.pebble if next_step == 'o' else self.rock}! You lost!")
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
    def _handle_timeout(self, signum, frame):
        raise Exception()
    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
if __name__ == "__main__":
    game = StepsMiniGame()