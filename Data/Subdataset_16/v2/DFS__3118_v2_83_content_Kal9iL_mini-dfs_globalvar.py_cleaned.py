from threading import Event
from globalconsts import NUM_OF_DATASERVERS
b1 = None
b2 = Event()
b3 = Event()
b4 = [Event() for _ in range(NUM_OF_DATASERVERS)]
b5 = [Event() for _ in range(NUM_OF_DATASERVERS)]
b6 = False
b7 = None
b8 = None
b9 = None
b10 = None
b11 = None
b12 = None
b13 = None
b14 = {}
b15 = {}
b16 = None
b17 = None
b18 = {}
b19 = {}
b20 = []
b21 = {}
b22 = {}
b23 = None
b24 = None
def fonk1():
    global b1, b6, b7, b8, b9
    global b10, b11, b12, b13
    global b14, b15, b16
    global b17, b18, b19
    global b20, b21, b22, b23
    global b24
    b1 = None
    b6 = False
    b7 = None
    b8 = None
    b9 = None
    b10 = None
    b11 = None
    b12 = None
    b13 = None
    b14 = {}
    b15 = {}
    b16 = None
    b17 = None
    b18 = {}
    b19 = {}
    b20 = []
    b21 = {}
    b22 = {}
    b23 = None
    b24 = None
def fonk2():
    print("Initializing global variables and events...")
    fonk1()
    print("Initialization complete.")
if b25 = = "__main__":
    fonk2()