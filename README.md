pytries
=======

Work in progress. This does not make an actual Trie yet.

Currently only makes a tree object that has `num_nodes` number of nodes and maximum `max_edges` number of edges connected to each node.

Usage: `Tree(edges=<num>, nodes=<num>)`

       t = Tree(nodes=10, edges=3)
       t.printer()

output:

    root
        a
           d
           e
           f
        b
           g
           h
           i
        c
           j

Pass `variable=True` to Tree and it will randomly create different numbers of edges between each node and it's children (between 2 and the number that was passed as the edges quantity).
