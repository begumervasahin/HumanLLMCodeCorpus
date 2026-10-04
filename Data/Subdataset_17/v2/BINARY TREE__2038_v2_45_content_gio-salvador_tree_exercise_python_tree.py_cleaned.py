import logging
import os
import sys
class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def setup_logger(name, log_level):
    logger = logging.getLogger(name)
    log_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.setLevel(log_level)
    return logger
log_level = os.environ.get('GIO_LOG_LEVEL', 'INFO').upper()
log = setup_logger(__file__, log_level)
def make_tree1():
    tree = Tree(2)
    log.debug(f'TREE: {tree.data}')
    tree.left = Tree(8)
    log.debug(f'TREE.LEFT: {tree.left.data}')
    tree.left.left = Tree(1)
    log.debug(f'TREE.LEFT.LEFT: {tree.left.left.data}')
    tree.left.right = Tree(3)
    log.debug(f'TREE.LEFT.RIGHT: {tree.left.right.data}')
    tree.right = Tree(9)
    log.debug(f'TREE.RIGHT: {tree.right.data}')
    tree.right.left = Tree(4)
    log.debug(f'TREE.RIGHT.LEFT: {tree.right.left.data}')
    tree.right.right = Tree(5)
    log.debug(f'TREE.RIGHT.RIGHT: {tree.right.right.data}')
    return tree
def make_tree2():
    tree = Tree(1)
    log.debug(f'TREE: {tree.data}')
    tree.left = Tree(8)
    log.debug(f'TREE.LEFT: {tree.left.data}')
    tree.left.right = Tree(3)
    log.debug(f'TREE.LEFT.RIGHT: {tree.left.right.data}')
    tree.right = Tree(4)
    log.debug(f'TREE.RIGHT: {tree.right.data}')
    tree.right.right = Tree(5)
    log.debug(f'TREE.RIGHT.RIGHT: {tree.right.right.data}')
    tree.right.right.right = Tree(7)
    log.debug(f'TREE.RIGHT.RIGHT.RIGHT: {tree.right.right.right.data}')
    return tree
def get_depth(tree):
    if tree is None:
        return 0
    left_depth = get_depth(tree.left)
    log.debug(f'get_depth - LEFT_DEPTH: {left_depth}')
    right_depth = get_depth(tree.right)
    log.debug(f'get_depth - RIGHT_DEPTH: {right_depth}')
    depth = max(left_depth, right_depth) + 1
    log.debug(f'get_depth - DEPTH: {depth}')
    return depth
def return_tuple_value_level(tree, level=0, result=None):
    if result is None:
        result = []
    if tree is None:
        return
    log.debug(f"return_tuple_value_level tree.data = {tree.data}")
    log.debug(f"return_tuple_value_level level = {level}")
    return_tuple_value_level(tree.left, level + 1, result)
    return_tuple_value_level(tree.right, level + 1, result)
    result.append((level, tree.data))
    log.debug(f"return_tuple_value_level append tuple = {(level, tree.data)}")
    log.debug(f"return_tuple_value_level result tuple = {result}")
    return result
def sort_by_level(tree):
    result = []
    depth = get_depth(tree)
    tuples = return_tuple_value_level(tree)
    log.debug("sort_by_level - Entering nested loops in sort_by_level function")
    for d in range(depth):
        for level, value in tuples:
            if level == d:
                result.append(value)
                log.debug(f"sort_by_level - Append to sorted list value = {value}")
    return result
def main():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        log.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("Create tree1")
    tree1 = make_tree1()
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info("Creating tree2")
    tree2 = make_tree2()
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(f"Max depth of Tree1 is {get_depth(tree1)}")
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(f"Max depth of Tree2 is {get_depth(tree2)}")
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(f"List of Tuple Value, Level for Tree1 = {return_tuple_value_level(tree1)}")
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(f"List of Tuple Value, Level for Tree2 = {return_tuple_value_level(tree2)}")
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(f"List with elements of Tree1 sorted by level = {sort_by_level(tree1)}")
    log.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    log.info(f"List with elements of Tree2 sorted by level = {sort_by_level(tree2)}")
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        msg = f'{__file__} failed to finish executing successfully.'
        log.exception(msg)
        sys.exit(1)