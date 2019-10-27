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
    def __init__(self, character = None, frequency = None):
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


def build_huffman_tree(char_count_dict):
    """
    The simplest construction algorithm uses a priority queue where the node with lowest probability is given highest priority:

    1. Create a leaf node for each symbol and add it to the priority queue.
    2. While there is more than one node in the queue:
        2.1. Remove the two nodes of highest priority (lowest probability) from the queue
        2.2. Create a new internal node with these two nodes as children and with probability equal to the sum of the two nodes' probabilities.
        2.3. Add the new node to the queue.
    3. The remaining node is the root node and the tree is complete.

    reference: https://en.wikipedia.org/wiki/Huffman_coding

    :param char_count_dict: dict
    :return: Node
    """
    queue = PriorityQueue()
    for char, count in char_count_dict.items():
        queue.put(Node(char, count))

    while queue.qsize() > 1:
        min1, min2 = (queue.get(), queue.get())
        new_node = Node(frequency=min1.frequency + min2.frequency)
        new_node.left = min1
        new_node.right = min2
        queue.put(new_node)

    return queue.get()


def __find_letter_codes(node, code_dict, code = ""):
    """
    Traverses the tree and builds the `code_dict` with letter codes
    Args:
        node(Node): Root node of huffman tree
        code_dict(dict): Dictionary containing letter codes
        code: code built till this moment/depth in a recursive order
    Returns:
        dict: A dictionary containing letter codes
    """
    if node is None:
        return

    if node.is_leaf_node():
        code_dict[node.character] = code

    __find_letter_codes(node.left, code_dict, code + "0")
    __find_letter_codes(node.right, code_dict, code + "1")


def find_letter_codes(node):
    """
    Traverses the tree and builds the `code_dict` with letter codes
    Args:
        node(Node): Root node of huffman tree
    Returns:
        dict: A dictionary containing letter codes
    """
    letter_codes_dict = {}
    if node is None:
        return letter_codes_dict

    __find_letter_codes(node, letter_codes_dict)
    return letter_codes_dict


def huffman_encoding(text):
    if text is None or len(text) == 0:
        return None, None

    char_count_dict = {}
    for char in text:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1

    tree = build_huffman_tree(char_count_dict)
    letter_codes_dict = find_letter_codes(tree)

    codes = [letter_codes_dict[c] for c in text]
    return tree, ''.join(codes)


def test():
    text = "The bird is the word"
    tree, code = huffman_encoding(text)
    print(code)

test()