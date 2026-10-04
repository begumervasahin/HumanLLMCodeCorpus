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
    b8.debug('TREE: %s' % b9.b3)
    b9.b1 = class1(8)
    b8.debug('TREE.LEFT: %s' % b9.b1.b3)
    b9.b1.b1 = class1(1)
    b8.debug('TREE.LEFT.LEFT: %s' % b9.b1.b1.b3)
    b9.b1.b2 = class1(3)
    b8.debug('TREE.LEFT.RIGHT: %s' % b9.b1.b2.b3)
    b9.b2 = class1(9)
    b8.debug('TREE.RIGHT: %s' % b9.b2.b3)
    b9.b2.b1 = class1(4)
    b8.debug('TREE.RIGHT.LEFT: %s' % b9.b2.b1.b3)
    b9.b2.b2 = class1(5)
    b8.debug('TREE.RIGHT.RIGHT: %s' % b9.b2.b2.b3)
    return b9
def fonk4():
    b9 = class1(1)
    b8.debug('TREE: %s' % b9.b3)
    b9.b1 = class1(8)
    b8.debug('TREE.LEFT: %s' % b9.b1.b3)
    b9.b1.b2 = class1(3)
    b8.debug('TREE.LEFT.RIGHT: %s' % b9.b1.b2.b3)
    b9.b2 = class1(4)
    b8.debug('TREE.RIGHT: %s' % b9.b2.b3)
    b9.b2.b2 = class1(5)
    b8.debug('TREE.RIGHT.RIGHT: %s' % b9.b2.b2.b3)
    b9.b2.b2.b2 = class1(7)
    b8.debug('TREE.RIGHT.RIGHT.RIGHT: %s' % b9.b2.b2.b2.b3)
    return b9
def fonk5(b9):
    if b9 is None:
        return 0
    else:
        b10 = fonk5(b9.b1)
        b8.debug('get_depth - LEFT_DEPTH: %s' % b10)
        b11 = fonk5(b9.b2)
        b8.debug('get_depth - RIGHT_DEPTH: %s' % b11)
        b12 = max(b10, b11) + 1
        b8.debug('get_depth - DEPTH: %s' % b12)
        return b12
def fonk6(b9, b13 = 0, b15=[]):
    if b9 is None:
        return
    else:
        b8.debug("return_tuple_value_level b9.b3 = %s" % b9.b3)
        b8.debug("return_tuple_value_level b13 = %s" % b13)
        fonk6(b9.b1, b13 + 1, b15)
        fonk6(b9.b2, b13 + 1, b15)
        b15.append([b13, b9.b3])
        b8.debug("return_tuple_value_level append b14 = %s" % ([b13, b9.b3]))
        b8.debug("return_tuple_value_level b15 b14 = %s" % b15)
        return b15
def fonk7(b9):
    b15 = []
    b12 = fonk5(b9)
    b16 = fonk6(b9, b15=[])
    b8.debug("sort_by_level - Entering nested loops in sort_by_level function")
    for d in range(b12):
        for r in range(len(b16)):
            if b16[r][0] == d:
                b15.append(b16[r][1])
                b8.debug("sort_by_level - Append to sorted list b16[%d][1] b17 = %d" % (r, b16[r][1]))
    return b15
def fonk8():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        b8.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("Create b18")
    b18 = fonk3()
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("Creating b19")
    b19 = fonk4()
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("Max b12 of b20 is %d" % fonk5(b18))
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("Max b12 of b21 is %d <<<<<<" % fonk5(b19))
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("List of Tuple Value,Level for b20 = %s" % fonk6(b18, b15=[]))
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("List of Tuple Value,Level for b21 = %s" % fonk6(b19, b15=[]))
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("List with elements of b20 sorted by b13 = %s" % fonk7(b18))
    b8.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b8.info("List with elements of b21 sorted by b13 = %s" % fonk7(b19))
if b22 = = "__main__":
    try:
        fonk8()
    except Exception as e:
        b23 = '%s failed to finish executing successfully.' % __file__
        b8.exception(b23)
        sys.exit(1)