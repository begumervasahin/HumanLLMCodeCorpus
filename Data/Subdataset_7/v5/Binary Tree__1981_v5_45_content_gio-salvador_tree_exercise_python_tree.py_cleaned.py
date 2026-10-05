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
    b17.debug('TREE: %s' % b4.b3)
    b4.b1 = class1(8)
    b17.debug('TREE.LEFT: %s' % b4.b1.b3)
    b4.b1.b1 = class1(1)
    b17.debug('TREE.LEFT.LEFT: %s' % b4.b1.b1.b3)
    b4.b1.b2 = class1(3)
    b17.debug('TREE.LEFT.RIGHT: %s' % b4.b1.b2.b3)
    b4.b2 = class1(9)
    b17.debug('TREE.RIGHT: %s' %  b4.b2.b3)
    b4.b2.b1 = class1(4)
    b17.debug('TREE.RIGHT.LEFT: %s' % b4.b2.b1.b3)
    b4.b2.b2 = class1(5)
    b17.debug('TREE.RIGHT.RIGHT: %s' % b4.b2.b2.b3)
    return b4
def fonk3():
    b4 = class1(1)
    b17.debug('TREE: %s' % b4.b3)
    b4.b1 = class1(8)
    b17.debug('TREE.LEFT: %s' % b4.b1.b3)
    b4.b1.b2 = class1(3)
    b17.debug('TREE.LEFT.RIGHT: %s' % b4.b1.b2.b3)
    b4.b2 = class1(4)
    b17.debug('TREE.RIGHT: %s' % b4.b2.b3)
    b4.b2.b2 = class1(5)
    b17.debug('TREE.RIGHT.RIGHT: %s' % b4.b2.b2.b3)
    b4.b2.b2.b2 = class1(7)
    b17.debug('TREE.RIGHT.RIGHT.RIGHT: %s' % b4.b2.b2.b2.b3)
    return b4
def fonk4(node):
    if node is None:
        return 0
    else:
        b5 = fonk4(node.b1)
        b6 = fonk4(node.b2)
        return max(b5, b6) + 1
def fonk5(node, b7 = 0, b8=[]):
    if node is None:
        return
    else:
        fonk5(node.b1, b7 + 1, b8)
        fonk5(node.b2, b7 + 1, b8)
        b8.append([b7, node.b3])
        return b8
def fonk6(node):
    b8 = []
    b9 = fonk4(node)
    b10 = fonk5(node, b8=[])
    for d in range(b9):
        for r in range(len(b10)):
            if b10[r][0] == d:
                b8.append(b10[r][1])
    return b8
def fonk7():
    b11 = os.environ.get('GIO_LOG_LEVEL', 'warning')
    if b11 = = 'debug':
        b17.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("Creating b12")
    b12 = fonk2()
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("Creating b13")
    b13 = fonk3()
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("Max b9 of b14 is %d" % fonk4(b12))
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("Max b9 of b15 is %d" % fonk4(b13))
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("List of Tuple Value,Level for b14 = %s" % fonk5(b12, b8=[]))
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("List of Tuple Value,Level for b15 = %s" % fonk5(b12, b8=[]))
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("List with elements of b14 sorted by b7 = %s" % fonk6(b12))
    b17.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b17.info("List with elements of b15 sorted by b7 = %s" % fonk6(b13))
if b16 = = "__main__":
    b17 = utils.get_top_level_logger(name=__file__, log_target='terminal')
    try:
        fonk7()
    except Exception as e:
        b18 = '%s failed to finish executing successfully.' % __file__
        b17.exception(b18)
        sys.exit(1)