import logging
import os
import sys
class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
def fonk2(name, b7):
    b4 = logging.getLogger(name)
    b5 = logging.StreamHandler()
    b6 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    b5.setFormatter(b6)
    b4.addHandler(b5)
    b4.setLevel(b7)
    return b4
b7 = os.environ.get('GIO_LOG_LEVEL', 'INFO').upper()
b8 = fonk2(__file__, b7)
def fonk3():
    b9 = class1(2)
    b8.debug(f'Creating root: {b9.b3}')
    b9.b1 = class1(8)
    b8.debug(f'Creating b1 child of root: {b9.b1.b3}')
    b9.b1.b1 = class1(1)
    b8.debug(f'Creating b1 child of b1 child: {b9.b1.b1.b3}')
    b9.b1.b2 = class1(3)
    b8.debug(f'Creating b2 child of b1 child: {b9.b1.b2.b3}')
    b9.b2 = class1(9)
    b8.debug(f'Creating b2 child of root: {b9.b2.b3}')
    b9.b2.b1 = class1(4)
    b8.debug(f'Creating b1 child of b2 child: {b9.b2.b1.b3}')
    b9.b2.b2 = class1(5)
    b8.debug(f'Creating b2 child of b2 child: {b9.b2.b2.b3}')
    return b9
def fonk4():
    b9 = class1(1)
    b8.debug(f'Creating root: {b9.b3}')
    b9.b1 = class1(8)
    b8.debug(f'Creating b1 child of root: {b9.b1.b3}')
    b9.b1.b2 = class1(3)
    b8.debug(f'Creating b2 child of b1 child: {b9.b1.b2.b3}')
    b9.b2 = class1(4)
    b8.debug(f'Creating b2 child of root: {b9.b2.b3}')
    b9.b2.b2 = class1(5)
    b8.debug(f'Creating b2 child of b2 child: {b9.b2.b2.b3}')
    b9.b2.b2.b2 = class1(7)
    b8.debug(f'Creating b2 child of b2 child of b2 child: {b9.b2.b2.b2.b3}')
    return b9
def fonk5(b9):
    if b9 is None:
        return 0
    b10 = fonk5(b9.b1)
    b8.debug(f'get_depth - b1 b12: {b10}')
    b11 = fonk5(b9.b2)
    b8.debug(f'get_depth - b2 b12: {b11}')
    b12 = max(b10, b11) + 1
    b8.debug(f'get_depth - current b12: {b12}')
    return b12
def fonk6(b9, b13 = 0, b14=None):
    if b14 is None:
        b14 = []
    if b9 is None:
        return b14
    b8.debug(f"return_tuple_value_level - b9.b3: {b9.b3}, b13: {b13}")
    b14.append((b13, b9.b3))
    fonk6(b9.b1, b13 + 1, b14)
    fonk6(b9.b2, b13 + 1, b14)
    b8.debug(f"return_tuple_value_level - b14: {b14}")
    return b14
def fonk7(b9):
    b14 = []
    b12 = fonk5(b9)
    b15 = fonk6(b9)
    b8.debug("sort_by_level - entering nested loops")
    for d in range(b12):
        for b13, value in b15:
            if b13 = = d:
                b14.append(value)
                b8.debug(f"sort_by_level - append value: {value}")
    return b14
def fonk8():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        b8.warning("Set OS Variable GIO_LOG_LEVEL to 'DEBUG' for more information.")
    b8.debug("Creating class1 1")
    b16 = fonk3()
    b8.debug("Creating class1 2")
    b17 = fonk4()
    b8.info(f"Max b12 of class1 1: {fonk5(b16)}")
    b8.info(f"Max b12 of class1 2: {fonk5(b17)}")
    b8.info(f"List of b15 (value, b13) for class1 1: {fonk6(b16)}")
    b8.info(f"List of b15 (value, b13) for class1 2: {fonk6(b17)}")
    b8.info(f"List of class1 1 elements sorted by b13: {fonk7(b16)}")
    b8.info(f"List of class1 2 elements sorted by b13: {fonk7(b17)}")
if b18 = = "__main__":
    try:
        fonk8()
    except Exception as e:
        b8.exception(f"{__file__} failed to finish executing successfully.")
        sys.exit(1)