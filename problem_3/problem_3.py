"""
The technique works by creating a binary tree of nodes. These can be stored in a regular array, the size of which
depends on the number of symbols, {\displaystyle n}n. A node can be either a leaf node or an internal node. Initially,
all nodes are leaf nodes, which contain the symbol itself, the weight (frequency of appearance) of the symbol and
optionally, a link to a parent node which makes it easy to read the code (in reverse) starting from a leaf node.
Internal nodes contain a weight, links to two child nodes and an optional link to a parent node.

Note:
As a common convention, bit '0' represents following the left child and bit '1' represents following the right child.
"""

from queue import PriorityQueue


class Node(object):
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def is_leaf_node(self):
        return self.left is None and self.right is None

    # overriding < operator method to use this node in priority queue
    def __lt__(self, other):
        return self.frequency < other.frequency

    # for easy debugging
    def __repr__(self):
        return str(f"Node({self.character, self.frequency})")


def test():
    q = PriorityQueue()
    q.put(Node('c', 1))
    q.put(Node('c', 2))
    print(q.get())
    print(q.get())

test()