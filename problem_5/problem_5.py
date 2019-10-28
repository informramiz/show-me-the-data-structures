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

    def __init__(self, timestamp, data, previous_hash = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __repr__(self):
        return str(f"Block({self.data})")

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        time = datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S")
        block = Block(time, data)

        if self.tail is None:
            self.tail = block
        else:
            block.previous_hash = self.tail
            self.tail = block

        self.size += 1

    def __len__(self):
        return self.size

    def to_list(self):
        blocks = []
        block = self.tail
        while block:
            blocks.append(block)
            block = block.previous_hash

        return blocks

    def __iter__(self):
        block = self.tail
        while block:
            yield block
            block = block.previous_hash

    def __repr__(self):
        return str([b for b in self])


def test():
    block_chain = BlockChain()
    block_chain.append("data1")
    block_chain.append("data2")
    print(block_chain.to_list())
    print(len(block_chain))

test()
