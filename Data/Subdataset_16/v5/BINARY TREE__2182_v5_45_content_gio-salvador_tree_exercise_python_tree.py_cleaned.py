import os
import sys
import modules.gio_logger as utils
class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
def fonk2():
    b4 = class1(2)
    b18.debug(f'TREE: {b4.b3}')
    b4.b1 = class1(8)
    b18.debug(f'TREE.LEFT: {b4.b1.b3}')
    b4.b1.b1 = class1(1)
    b18.debug(f'TREE.LEFT.LEFT: {b4.b1.b1.b3}')
    b4.b1.b2 = class1(3)
    b18.debug(f'TREE.LEFT.RIGHT: {b4.b1.b2.b3}')
    b4.b2 = class1(9)
    b18.debug(f'TREE.RIGHT: {b4.b2.b3}')
    b4.b2.b1 = class1(4)
    b18.debug(f'TREE.RIGHT.LEFT: {b4.b2.b1.b3}')
    b4.b2.b2 = class1(5)
    b18.debug(f'TREE.RIGHT.RIGHT: {b4.b2.b2.b3}')
    return b4
def fonk3():
    b4 = class1(1)
    b18.debug(f'TREE: {b4.b3}')
    b4.b1 = class1(8)
    b18.debug(f'TREE.LEFT: {b4.b1.b3}')
    b4.b1.b2 = class1(3)
    b18.debug(f'TREE.LEFT.RIGHT: {b4.b1.b2.b3}')
    b4.b2 = class1(4)
    b18.debug(f'TREE.RIGHT: {b4.b2.b3}')
    b4.b2.b2 = class1(5)
    b18.debug(f'TREE.RIGHT.RIGHT: {b4.b2.b2.b3}')
    b4.b2.b2.b2 = class1(7)
    b18.debug(f'TREE.RIGHT.RIGHT.RIGHT: {b4.b2.b2.b2.b3}')
    return b4
def fonk4(b4):
    if b4 is None:
        return 0
    b5 = fonk4(b4.b1)
    b18.debug(f'get_depth - LEFT_DEPTH: {b5}')
    b6 = fonk4(b4.b2)
    b18.debug(f'get_depth - RIGHT_DEPTH: {b6}')
    b7 = max(b5, b6) + 1
    b18.debug(f'get_depth - DEPTH: {b7}')
    return b7
def fonk5(b4, b8 = 0, b9=None):
    if b9 is None:
        b9 = []
    if b4 is None:
        return b9
    b18.debug(f'return_tuple_value_level b4.b3 = {b4.b3}')
    b18.debug(f'return_tuple_value_level b8 = {b8}')
    fonk5(b4.b1, b8 + 1, b9)
    fonk5(b4.b2, b8 + 1, b9)
    b9.append([b8, b4.b3])
    b18.debug(f'return_tuple_value_level append b10 = {[b8, b4.b3]}')
    b18.debug(f'return_tuple_value_level b9 b10 = {b9}')
    return b9
def fonk6(b4):
    b9 = []
    b7 = fonk4(b4)
    b11 = fonk5(b4)
    b18.debug("sort_by_level - Entering nested loops in sort_by_level function")
    for d in range(b7):
        for b8, b12 in b11:
            if b8 = = d:
                b9.append(b12)
                b18.debug(f'sort_by_level - Append to sorted list b12 = {b12}')
    return b9
def fonk7():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        b18.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Create b13")
    b13 = fonk2()
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Creating b14")
    b14 = fonk3()
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info(f"Max b7 of b15 is {fonk4(b13)}")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info(f"Max b7 of b16 is {fonk4(b14)} <<<<<<<")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info(f"List of Tuple Value, Level for b15 = {fonk5(b13)}")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info(f"List of Tuple Value, Level for b16 = {fonk5(b14)}")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info(f"List with elements of b15 sorted by b8 = {fonk6(b13)}")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info(f"List with elements of b16 sorted by b8 = {fonk6(b14)}")
if b17 = = "__main__":
    global b18
    b18 = utils.get_top_level_logger(name=__file__, log_target='terminal')
    try:
        fonk7()
    except Exception as e:
        b18.exception(f'{__file__} failed to finish executing successfully.')
        sys.exit(1)