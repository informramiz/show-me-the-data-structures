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
import sys


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
    elif node.is_leaf_node():  # handle single node use case
        letter_codes_dict[node.character] = "0"
        return letter_codes_dict

    __find_letter_codes(node, letter_codes_dict)
    return letter_codes_dict


def huffman_encoding(text):
    if not isinstance(text, str):
        print("Invalid Data!")
        return None, None
    elif text is None or len(text) == 0:
        print("Empty Data!")
        return None, None

    char_count_dict = {}
    for char in text:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1

    tree = build_huffman_tree(char_count_dict)
    letter_codes_dict = find_letter_codes(tree)

    codes = [letter_codes_dict[c] for c in text]
    return tree, ''.join(codes)


def huffman_decoding(tree, coded_data):
    """
        Traverses the tree and decodes coded_data back to proper text
        Args:
            tree(Node): Root node of huffman tree
            coded_data(str): A string representing data in coded form
        Returns:
            str: A dictionary containing letter codes
    """
    if not isinstance(tree, Node) or not isinstance(coded_data, str):
        print("Invalid Data!")
        return None
    elif tree is None or coded_data is None or len(coded_data) == 0:
        print("Empty tree or coded data!")
        return None

    letters = []
    node = tree
    # for each bit in coded_data, traverse the tree to find the letter at leaf node, then restart
    if node.is_leaf_node():  # single node tree, special case
        for _ in coded_data:
            letters.append(node.character)
    else:
        for c in coded_data:
            if c == '0':
                node = node.left
            else:
                node = node.right

            if node.is_leaf_node():
                # reached leaf node, only leaf nodes contain characters
                letters.append(node.character)
                # search for this code is complete, restart the search for next bits
                node = tree

    return ''.join(letters)


def test_case(a_great_sentence):
    print("\n-------Test-----------")
    tree, encoded_data = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(tree, encoded_data)

    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))
    assert(a_great_sentence == decoded_data)


def run_test_cases():
    test_case("The bird is the word")
    test_case("My name is Ramiz")
    test_case("a + b = c + d")

    # repetitive alphabet
    test_case("aaaaa")
    test_case("bbbbbbbb")
    test_case("aaaaabbbbccccc")

    # empty input
    print("----Edge input related cases----")
    huffman_encoding(None)  # should print "Invalid Data!"
    huffman_encoding("")  # should print "empty data"
    huffman_decoding(None, None)  # should print "Invalid Data!"
    huffman_decoding(Node(), "")  # should print "Empty tree or coded data!"

    # invalid input
    huffman_encoding(123) # should print "invalid data"
    huffman_decoding(Node(), 123) # should print "invalid data"


run_test_cases()