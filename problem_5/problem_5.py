"""
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and
how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous
block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time
when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.
"""

import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash = 0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __repr__(self):
        return str(f"Block({self.data, self.timestamp, self.hash}, prev_hash={self.previous_hash})")

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        time = datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S")
        block = Block(time, data)

        if self.head is None:
            self.head = Node(block)
            self.size += 1
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        block.previous_hash = tail.value.hash
        tail.next = Node(block)
        self.size += 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def search(self, data):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node:
            if node.value.data == data:
                return node
            node = node.next
        return None

    def delete(self, data):
        """ Remove first occurrence of value. """
        if self.is_empty():
            return False

        if self.head.value.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        node = self.head
        while node.next and node.next.value != data:
            node = node.next

        if node.next:
            node.next = node.next.next
            self.size -= 1
            return True

        # Node not found
        return False

    def to_list(self):
        return [b for b in self]

    def __iter__(self):
        block = self.head
        while block:
            yield block.value
            block = block.next

    def __repr__(self):
        return str([b for b in self])


def test_hash_equality(output):
    # check if next block's previous_hash is same as first block's hash
    prev_hash = None
    for b in output:
        if prev_hash is None:
            prev_hash = b.hash
        else:
            assert (b.previous_hash == prev_hash)
            prev_hash = b.hash


def test():
    block_chain = BlockChain()
    block_chain.append("data1")
    block_chain.append("data2")
    block_chain.append("data3")

    # Test Append
    output = block_chain.to_list()
    print(output) # should print Block(data1, time, hash, prev_hash=0), (data2, time, hash, prev_hash=hash of prev bloc), (data3, ...)
    test_hash_equality(output)
    output = [b.data for b in output] # simplifying output for assert
    assert (output == ["data1", "data2", "data3"])

    # Test-1 Search
    search_result = block_chain.search("data1")
    print(search_result.value) # should print (data1, time, hash, prev_has)
    assert(search_result.value.data == 'data1')

    # # Test-2 Search
    search_result = block_chain.search("data5")
    print(search_result)  # should print None
    assert (search_result is None)

    # Test-1 Delete
    block_chain.delete("data1")
    print(len(block_chain))  # should print 1
    assert(len(block_chain) == 2)
    # Test-2 Delete
    block_chain.delete("data2")
    print(len(block_chain))  # should print 0
    assert(len(block_chain) == 1)


test()
