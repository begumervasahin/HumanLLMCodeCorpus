import sys
import os
import logging
from collections import deque
class CustomLogger:
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self._configure_handler(log_level)
    def _configure_handler(self, log_level):
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
    def debug(self, message):
        self.logger.debug(message)
    def info(self, message):
        self.logger.info(message)
    def warning(self, message):
        self.logger.warning(message)
    def error(self, message):
        self.logger.error(message)
    def exception(self, message):
        self.logger.exception(message)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def create_node(data):
    return TreeNode(data)
def make_tree1():
    tree = create_node(2)
    _log_node_creation(tree, "Tree1")
    tree.left = create_node(8)
    tree.left.left = create_node(1)
    tree.left.right = create_node(3)
    tree.right = create_node(9)
    tree.right.left = create_node(4)
    tree.right.right = create_node(5)
    return tree
def make_tree2():
    tree = create_node(1)
    _log_node_creation(tree, "Tree2")
    tree.left = create_node(8)
    tree.left.right = create_node(3)
    tree.right = create_node(4)
    tree.right.right = create_node(5)
    tree.right.right.right = create_node(7)
    return tree
def _log_node_creation(node, tree_name):
    log.debug(f"Created {tree_name} with root data: {node.data}")
    if node.left:
        log.debug(f"Added left child to {tree_name}: {node.left.data}")
    if node.right:
        log.debug(f"Added right child to {tree_name}: {node.right.data}")
def get_depth(tree):
    if tree is None:
        return 0
    else:
        left_depth = get_depth(tree.left)
        right_depth = get_depth(tree.right)
        return max(left_depth, right_depth) + 1
def return_tuple_value_level(tree):
    if tree is None:
        return []
    result = []
    queue = deque([(tree, 0)])
    while queue:
        node, level = queue.popleft()
        result.append((node.data, level))
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return result
def sort_by_level(tree):
    tuples = return_tuple_value_level(tree)
    tuples.sort(key=lambda x: x[1])
    return [value for value, _ in tuples]
def main():
    if os.environ.get('GIO_LOG_LEVEL') is None:
        log.warning("Set OS Variable GIO_LOG_LEVEL to 'debug' for more information.")
    log.debug("Starting program execution...")
    log.info("Creating and analyzing Tree1...")
    tree1 = make_tree1()
    log.info("Creating and analyzing Tree2...")
    tree2 = make_tree2()
    log.info(f"Max depth of Tree1 is {get_depth(tree1)}")
    log.info(f"Max depth of Tree2 is {get_depth(tree2)}")
    log.info("Generating list of Tuple Value,Level for Tree1...")
    log.info(f"List of Tuple Value,Level for Tree1: {return_tuple_value_level(tree1)}")
    log.info("Generating list of Tuple Value,Level for Tree2...")
    log.info(f"List of Tuple Value,Level for Tree2: {return_tuple_value_level(tree2)}")
    log.info("Sorting elements of Tree1 by level...")
    log.info(f"List with elements of Tree1 sorted by level: {sort_by_level(tree1)}")
    log.info("Sorting elements of Tree2 by level...")
    log.info(f"List with elements of Tree2 sorted by level: {sort_by_level(tree2)}")
    log.debug("Program execution completed.")
if __name__ == "__main__":
    log = CustomLogger(log_level=logging.DEBUG)
    try:
        main()
    except Exception as e:
        msg = 'Program failed to finish executing successfully.'
        log.exception(msg)
        sys.exit(1)