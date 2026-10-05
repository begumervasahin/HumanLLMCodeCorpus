import modules.gio_logger as utils
import os
import sys
class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
def make_tree1 ():
    b4 = class1(2)
    b18.debug('TREE: %s' % b4.b3)
    b4.b1 = class1(8)
    b18.debug('TREE.LEFT: %s' % b4.b1.b3)
    b4.b1.b1 = class1(1)
    b18.debug('TREE.LEFT.LEFT: %s' % b4.b1.b1.b3)
    b4.b1.b2 = class1(3)
    b18.debug('TREE.LEFT.RIGHT: %s' % b4.b1.b2.b3)
    b4.b2 = class1(9)
    b18.debug('TREE.RIGHT: %s' %  b4.b2.b3)
    b4.b2.b1 = class1(4)
    b18.debug('TREE.RIGHT.LEFT: %s' % b4.b2.b1.b3)
    b4.b2.b2 = class1(5)
    b18.debug('TREE.RIGHT.LEFT: %s' % b4.b2.b2.b3)
    return b4
def make_tree2 ():
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
def get_depth (b4):
    if b4 is None:
        return 0;
    else:
        b5 = get_depth(b4.b1)
        b18.debug('get_depth - LEFT_DEPTH: %s' % b5)
        b6 = get_depth(b4.b2)
        b18.debug('get_depth - RIGHT_DEPTH: %s' % b6)
        if (b5 > b6):
            b18.debug('get_depth - DEPTH: %s' % (b5+1))
            return b5+1
        else:
            b18.debug('get_depth - DEPTH: %s' % (b6+1))
            return b6+1
def return_tuple_value_level (b4, b7 = 0, b9=[]):
    if b4 is None:
        return;
    else:
        b18.debug("return_tuple_value_level b4.b3 = %s" % b4.b3 )
        b18.debug("return_tuple_value_level b7 = %s" % b7)
        b5 = return_tuple_value_level(b4.b1,  b7+1, b9)
        b6 = return_tuple_value_level(b4.b2, b7+1, b9)
        b7-1
        b9.append([b7, b4.b3])
        b18.debug("return_tuple_value_level append b8 = %s" % ([b7, b4.b3]))
        b18.debug("return_tuple_value_level b9 b8 = %s" % b9)
        return b9
def fonk2(b4):
    b9 = []
    b10 = get_depth(b4)
    b11 = return_tuple_value_level(b4, b9=[])
    b18.debug("sort_by_level - Entering nested loops in sort_by_level function")
    for d in range(b10):
        for r in range(len(b11)):
            if b11[r][0] == d:
                b9.append(b11[r][1])
                b18.debug("sort_by_level - Append to sorted list b11[%d][1] b12 = %d" % (r,b11[r][1]))
    return b9
def main ():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        b18.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Create b13")
    b13 = make_tree1()
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Creating b14")
    b14 = make_tree2()
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Max b10 of b15 is %d" % get_depth(b13))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("Max b10 of b16 is %d <<<<<<" % get_depth(b14))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List of Tuple Value,Level for b15 = %s" % return_tuple_value_level(b13, b9=[]))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List of Tuple Value,Level for b16 = %s" % return_tuple_value_level(b13, b9=[]))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List with elements of b15 sorted by b7 = %s" % fonk2(b13))
    b18.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    b18.info("List with elements of b16 sorted by b7 = %s" % fonk2(b14))
if b17 = = "__main__":
    global b18
    b18 = utils.get_top_level_logger(name=__file__, log_target='terminal')
    try:
        main()
    except Exception as e:
        b19 = '%s failed to finish executing successfully.' % __file__
        b18.exception(b19)
        sys.exit(1)