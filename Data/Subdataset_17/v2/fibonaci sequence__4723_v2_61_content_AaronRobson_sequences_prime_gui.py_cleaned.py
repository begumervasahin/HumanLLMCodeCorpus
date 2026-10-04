import threading
from time import sleep
import itertools
class PrintRewritable:
    def print(self, message, rewrite=False):
        print(message, end='\r' if rewrite else '\n')
class PrimeCollection:
    def __init__(self, initial_data=None):
        self.cache = initial_data or []
        self.current = 2
    @property
    def last(self):
        return self.cache[-1] if self.cache else None
    def __iter__(self):
        return self
    def __next__(self):
        while not self._is_prime(self.current):
            self.current += 1
        self.cache.append(self.current)
        prime = self.current
        self.current += 1
        return prime
    @staticmethod
    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
prw = PrintRewritable()
polling_time = 0.042
OUTPUT_FILE = 'primelist.txt'
class PrimeGUI:
    def __init__(self, *args):
        self._helper_threads = ()
        self.reset(*args)
    def _setup_threads(self):
        prime_thread = threading.Thread(target=self._prime_finder, name='PrimeThread')
        display_thread = threading.Thread(target=self._display_thread, name='CheckerThread')
        self._helper_threads = (prime_thread, display_thread)
    def reset(self):
        self.stop()
        self._pc = PrimeCollection()
    def start(self):
        self.stop()
        self._setup_threads()
        self._queuing_finished = False
        for thread in self._helper_threads:
            if not thread.is_alive():
                thread.start()
    def stop(self):
        self._queuing_finished = True
        for thread in self._helper_threads:
            if thread.is_alive():
                thread.join()
    def save(self, filepath):
        self.stop()
        self._save_enumeration_to_file(filepath, *self._pc.cache)
    def load(self, filepath):
        self.stop()
        data = self._load_enumeration_from_file(filepath)
        self._pc = PrimeCollection(data)
    @property
    def last_prime(self):
        return self._pc.last
    def is_continuing(self, *args):
        return not self._queuing_finished
    def _prime_finder(self):
        for prime_num in itertools.takewhile(self.is_continuing, self._pc):
            pass
    def _display_thread(self):
        while self.is_continuing():
            prw.print(self.last_prime, True)
            sleep(polling_time)
    def __len__(self):
        return len(self._pc.cache)
    def _save_enumeration_to_file(self, filepath, *output_enumeration):
        with open(filepath, mode='w') as file:
            for item in output_enumeration:
                file.write(f'{item}\n')
    def _load_enumeration_from_file(self, filepath):
        with open(filepath, mode='r') as file:
            stripped_lines = (line.strip() for line in file.readlines())
            return [int(line) for line in stripped_lines if line]
if __name__ == "__main__":
    print('Prime number finder:')
    prw.print('Loading...', True)
    prime_gui = PrimeGUI()
    try:
        prime_gui.load(OUTPUT_FILE)
    except IOError:
        print('No data found, starting from scratch.')
    print('Hit Enter to finish and save.')
    prime_gui.start()
    input()
    prime_gui.stop()
    print()
    print(f'{prime_gui.last_prime} highest prime')
    print(f'{len(prime_gui)} found')
    print(f'Attempting to save file to {OUTPUT_FILE!r}, this may take a while.')
    try:
        prime_gui.save(OUTPUT_FILE)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')