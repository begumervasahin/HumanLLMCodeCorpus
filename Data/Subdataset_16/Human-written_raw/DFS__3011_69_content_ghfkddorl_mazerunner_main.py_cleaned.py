import os
import sys
b1 = os.path.abspath(__file__)
b2 = os.path.dirname(b1)
sys.path.append(b2)
print("[ START PROGRAM ]")
print("start main file : "+b1)
print("sys append path : "+b2)
from gui.b3 import *
b3 = Application(b2)
b3.mainloop()