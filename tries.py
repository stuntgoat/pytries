from Queue import Queue
from random import choice
from time import sleep

from lib import name_factory


class Node(object):
    def __init__(self, name, edges=2, variable=False):
        self.children = []
        self._depth = 0
        self.name = name
        self.variable = variable
        self.edges = edges if not self.variable else choice(xrange(2, edges+1))

    def add_node(self, node):
        self.children.append(node)

    def __repr__(self):
        return self.name

    def printer(self):
        if 'root' == self.name:
            print self.name
        else:
            print '   ' * self._depth, self.name
        for child in self.children:

            child.printer()

class Tree(Node):
    def __init__(self, node_count, *args, **kwargs):
        super(Tree, self).__init__('root', *args, **kwargs)
        self.node_count = node_count
        self.levels = 0
        self.name = 'root'
        self.expand_queue = Queue()

        # put the root node on the trie
        self.expand_queue.put(self)

        # create a naming function
        self._namer = name_factory(self.node_count)

        # create the trie
        self.expand_tree()

    def expand_tree(self):

        tree = self.expand_queue.get()

        self.levels += 1
        for i in xrange(tree.edges):
            if self.node_count == 0:
                return

            n = Node(self._namer.next(), self.edges, self.variable)
            self.node_count -= 1
            n._depth = tree._depth + 1
            tree.add_node(n)
            self.expand_queue.put(n)

        return self.expand_tree()
