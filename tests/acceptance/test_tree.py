from pytries import Tree

class TestTree(object):
    NODES = 10
    EDGES = 2

    def pytest_funcarg__tree(self, request):
        t = Tree(nodes=self.NODES, edges=self.EDGES)
        t.expand_tree()
        return t

    def test_nodes_at_level(self, tree):
        assert len(tree.nodes_at_level(0)) == 1
        assert len(tree.nodes_at_level(1)) == 2
        assert len(tree.nodes_at_level(2)) == 4
        assert len(tree.nodes_at_level(3)) == 4
        assert len(tree.nodes_at_level(4)) == 0
