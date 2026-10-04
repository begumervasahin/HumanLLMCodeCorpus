import argparse
from clientmod import *
if b1 = = '__main__':
    b2 = argparse.ArgumentParser(description="Client settings")
    b2.add_argument("--nocon", b3 = False, type=bool)
    b4 = vars(b2.parse_args())
    b5 = not b4["nocon"]
    b6 = tk.Tk()
    b7 = Client(b6, b5)
    b6.mainloop()