import modules.gio_logger as utils
import os
import sys
class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
def fonk2():
    b4 = class1(2)
    b18.debug('TREE: %s' % b4.b3)
    b4.b1 = class1(8)
    b18.debug('TREE.LEFT: %s' % b4.b1.b3)
    b4.b1.b1 = class1(1)
    b18.debug('TREE.LEFT.LEFT: %s' % b4.b1.b1.b3)
    b4.b1.b2 = class1(3)
    b18.debug('TREE.LEFT.RIGHT: %s' % b4.b1.b2.b3)
    b4.b2 = class1(9)
    b18.debug('TREE.RIGHT: %s' % b4.b2.b3)
    b4.b2.b1 = class1(4)
    b18.debug('TREE.RIGHT.LEFT: %s' % b4.b2.b1.b3)
    b4.b2.b2 = class1(5)
    b18.debug('TREE.RIGHT.RIGHT: %s' % b4.b2.b2.b3)
    return b4
def fonk3():
    b4 = class1(1)
    b18.debug('TREE: %s' % b4.b3)
    b4.b1 = class1(8)
    b18.debug('TREE.LEFT: %s' % b4.b1.b3)
    b4.b1.b2 = class1(3)
    b18.debug('TREE.LEFT.RIGHT: %s' % b4.b1.b2.b3)
    b4.b2 = class1(4)
    b18.debug('TREE.RIGHT: %s' % b4.b2.b3)
    b4.b2.b2 = class1(5)
    b18.debug('TREE.RIGHT.RIGHT: %s' % b4.b2.b2.b3)
    b4.b2.b2.b2 = class1(7)
    b18.debug('TREE.RIGHT.RIGHT.RIGHT: %s' % b4.b2.b2.b2.b3)
    return b4
def fonk4(b4):
    if b4 is None:
        return 0
    else:
        b5 = fonk4(b4.b1)
        b18.debug('get_depth - LEFT_DEPTH: %s' % b5)
        b6 = fonk4(b4.b2)
        b18.debug('get_depth - RIGHT_DEPTH: %s' % b6)
        b7 = max(b5, b6) + 1
        b18.debug('get_depth - DEPTH: %s' % b7)
        return b7
def fonk5(b4, b8 = 0, b9=None):
    if b9 is None:
        b9 = []
    if b4 is None:
        return b9
    else:
        b18.debug("return_tuple_value_level b4.b3 = %s" % b4.b3)
        b18.debug("return_tuple_value_level b8 = %s" % b8)
        fonk5(b4.b1, b8 + 1, b9)
        fonk5(b4.b2, b8 + 1, b9)
        b9.append([b8, b4.b3])
        b18.debug("return_tuple_value_level append b10 = %s" % ([b8, b4.b3]))
        b18.debug("return_tuple_value_level b9 b10 = %s" % b9)
        return b9
def fonk6(b4):
    b9 = []
    b7 = fonk4(b4)
    b11 = fonk5(b4)
    b18.debug("sort_by_level - Entering nested loops in sort_by_level function")
    for d in range(b7):
        for r in range(len(b11)):
            if b11[r][0] == d:
                b9.append(b11[r][1])
                b18.debug("sort_by_level - Append to sorted list b11[%d][1] b12 = %d" % (r, b11[r][1]))
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
    b18.info("Max b7 of b15 is %d" % fonk4(b13))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Max b7 of b16 is %d <<<<<<" % fonk4(b14))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List of Tuple Value, Level for b15 = %s" % fonk5(b13))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List of Tuple Value, Level for b16 = %s" % fonk5(b14))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List with elements of b15 sorted by b8 = %s" % fonk6(b13))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List with elements of b16 sorted by b8 = %s" % fonk6(b14))
if b17 = = "__main__":
    global b18
    b18 = utils.get_top_level_logger(name=__file__, log_target='terminal')
    try:
        fonk7()
    except Exception as e:
        b19 = '%s failed to finish executing successfully.' % __file__
        b18.exception(b19)
        sys.exit(1)