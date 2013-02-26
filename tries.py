from Queue import Queue
from collections import defaultdict
from random import choice
from lib import name_factory


class Node(object):
    def __init__(self, name='', edges=2, variable=False):
        self.children = []
        self.data = None
        self._depth = 0
        self.name = name
        self.variable = variable
        self.edges = edges if not self.variable else choice(xrange(2, edges+1))

    def add_node(self, node):
        self.children.append(node)

    def __repr__(self):
        return "Node: %s" % self.name

    def printer(self):
        if 'root' == self.name:
            print self.name
        else:
            print '   ' * self._depth, self.name
        for child in self.children:

            child.printer()


## TODO: - return a list of nodes at a given depth
class Tree(Node):
    def __init__(self, node_count=2, *args, **kwargs):
        super(Tree, self).__init__(*args, **kwargs)
        self.node_count = node_count
        self.levels = 0
        self.expand_queue = Queue()
        self._level_nodes = defaultdict(list)

        self.expand_queue.put(self)

        # create a naming function
        self._namer = name_factory(self.node_count)

    def nodes_at_level(self, level):
        try:
            return self._level_nodes[level]
        except Exception:
            print "level %s not found" % level
            raise

    def set_node_at_level(self, level, node):
        self._level_nodes[level].append(node)

    def expand_tree(self):
        tree = self.expand_queue.get()

        self.levels += 1
        for i in xrange(tree.edges):

            if self.node_count == 0:
                return

            n = Node(self.edges, self.variable, name=self._namer.next())
            self.node_count -= 1
            n._depth = tree._depth + 1
            tree.add_node(n)
            self.expand_queue.put(n)



        return self.expand_tree()


class WeightedNode(Node):
    def __init__(self, *args, **kwargs):
        cost = kwargs.pop('cost', 1)
        super(WeightedNode, self).__init__(*args, **kwargs)
        # The cost of the edge between the parent node
        self.cost = cost

    def printer(self):
        if 'root' == self.name:
            print self.name, self.cost
        else:
            print '   ' * self._depth, self.name, self.cost
        for child in self.children:
            child.printer()


class WeightedGraph(Tree, WeightedNode):
    """
    Creates a weighted graph. Good for demonstrating Uniform Cost Search.
    """
    def __init__(self, *args, **kwargs):
        weight_range = kwargs.pop('weight_range', [])
        super(WeightedGraph, self).__init__(*args, **kwargs)
        self.weight_range = weight_range
        self.name = 'root'
        self.weight = 1  # default
        self.expand_tree()

    def weighter(self, weight=0):
        """
        Used to generate an edges weight.
        """
        if self.weight_range:
            return choice(range(*self.weight_range))
        elif weight:
            return weight
        else:
            print self.weight_range, 'print self.weight_range'
            return self.weight

    def expand_tree(self):
        tree = self.expand_queue.get()

        self.levels += 1
        for i in xrange(tree.edges):
            if self.node_count == 0:
                return
            cost = self.weighter()

            n = WeightedNode(variable=self.variable, edges=self.edges, cost=cost, name=self._namer.next())

            self.node_count -= 1
            self.weight += 1
            n._depth = tree._depth + 1

            tree.add_node(n)
            self.expand_queue.put(n)
            self.set_node_at_level(self.levels, n)

        return self.expand_tree()


class Trie(Tree):
    """

    """
    pass
