import sys
from queue import Queue
from queue import LifoQueue


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    @classmethod
    def create_node(cls, value, left=None, right=None):
        new_node = cls()
        new_node.value = value
        new_node.left = left
        new_node.right = right
        return new_node

    def add_child(self, val):
        new_node = Node.create_node(val)
        if not self.left:
            self._add_child_left(new_node)
        else:
            self._add_child_right(new_node)

    def _add_child_left(self, new_node):
        self.left = new_node

    def _add_child_right(self, new_node):
        self.right = new_node


    @staticmethod
    def height(_node):
        if not _node:
            return 0
        return 1 + max(Node.height(_node.left), Node.height(_node.right))

    def __repr__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None

    @classmethod
    def create_tree(cls, key):
        new_tree = cls()
        new_tree.root = Node.create_node(key)
        return new_tree

    def insert(self, value):
        q_nodes = Queue()
        q_nodes.put(self.root)
        first_hole = None
        while not q_nodes.empty():
            this_node = q_nodes.get()
            if this_node.left:
                q_nodes.put(this_node.left)
            elif not first_hole:
                first_hole = this_node
            if this_node.right:
                q_nodes.put(this_node.right)
            elif not first_hole:
                first_hole = this_node

        #print("The last value I found was ", this_node.value)
        #print("First hole was found at ", first_hole)
        first_hole.add_child(value)

    def __repr__(self):
        q_nodes = Queue()
        q_nodes.put(self.root)
        s = "["
        next_square = 1
        n_popped = 0
        while not q_nodes.empty():
            #s += '**QSIZE ==  '+str(q_nodes.qsize()) + '**',
            #s += '*qs == ' + str(q_nodes.qsize()) + '*'
            if n_popped == next_square:
                s += '\n'
                n_popped = 0
                next_square *= 2
            this_node = q_nodes.get()
            n_popped += 1
            s += " <" + str(this_node.value) + "> "
            if this_node.left:
                q_nodes.put(this_node.left)
            if this_node.right:
                q_nodes.put(this_node.right)
        s += "]"
        return s

        #print("The last value I found was ", this_node.value)
        #print("First hole was found at ", first_hole)

    def get_height(self):
        return Node.height(self.root)

    @staticmethod
    def dfs_pre_order(node):
        print(node.value)
        if node.left:
            tree.dfs_pre_order(node.left)
        if node.right:
            tree.dfs_pre_order(node.right)

    @staticmethod
    def dfs_in_order(node):
        if node.left:
            tree.dfs_in_order(node.left)
        print(node.value)
        if node.right:
            tree.dfs_in_order(node.right)

    @staticmethod
    def dfs_post_order(node):
        if node.left:
            tree.dfs_post_order(node.left)
        if node.right:
            tree.dfs_post_order(node.right)
        print(node.value)


if __name__ == '__main__':
    print("Begin main")
    node = Node.create_node(1)
    tree = Tree.create_tree(node)
    #print(node)
    #print(tree.get_height())

    for i in range(2, 16):
        tree.insert(i)
    print(tree)

    tree.dfs_in_order(tree.root)
    print("Post-order")
    tree.dfs_post_order(tree.root)
    print("Pre-order")
    tree.dfs_pre_order(tree.root)
