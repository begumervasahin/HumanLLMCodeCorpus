import random
import signal
import getch
class StepsMiniGame:
    def __init__(self):
        self.customize_obstacles()
        self.path = self.generate_path()
        self.start_game()
    def customize_obstacles(self):
        print("Would you like to customize the obstacles? [Enter Y/N]")
        customize = getch.getch().lower()
        if customize == 'y':
            self.pebble = input("What would you like 'o' to represent? ")
            self.rock = input("What would you like 'O' to represent? ")
        else:
            self.pebble = "pebble"
            self.rock = "rock"
    def generate_path(self):
        path_array = []
        path_length = 50
        low, high = 0, 100
        one_sd, two_sd = 68, 95
        for _ in range(path_length):
            step_int = random.randint(low, high)
            if step_int <= one_sd:
                path_array.append('X')
            elif step_int <= two_sd:
                path_array.append('o')
            else:
                path_array.append('O')
        return ''.join(path_array)
    def start_game(self):
        print("The game starts now. Quick, press 'd' to advance or 'a' to dodge.")
        for next_step in self.path:
            print(next_step)
            signal.signal(signal.SIGALRM, self._handle_timeout)
            signal.alarm(2)
            try:
                user_input = getch.getch()
                self.process_input(user_input, next_step)
            except ValueError as e:
                print(e)
                break
            except Exception:
                print("You're too slow! You lost!")
                break
            finally:
                signal.alarm(0)
    def process_input(self, user_input, next_step):
        if user_input == 'a':
            if next_step not in ['o', 'O']:
                raise ValueError("You've diverted from the right track! You lost!")
        elif user_input == 'd':
            if next_step != 'X':
                obstacle = self.pebble if next_step == 'o' else self.rock
                raise ValueError(f"You hit a {obstacle}! You lost!")
        else:
            raise ValueError("Please enter a valid command!")
    def _handle_timeout(self, signum, stack):
        raise Exception()
if __name__ == "__main__":
    game = StepsMiniGame()