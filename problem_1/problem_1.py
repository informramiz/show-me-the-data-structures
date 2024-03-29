"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry
is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add
a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put()
operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU
cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.
For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full,
you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.
"""

from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self._capacity = capacity
        # pop, delete and append operations of OrderedDict are O(1) as it is a high performance Python container
        # inside it, it uses native Python Dictionary, HashMap and DoublyLinkedList
        # reference: https://docs.python.org/2/library/collections.html
        self._items = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self._capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return -1

        # edge case
        if key is None:
            return -1

        # can search for
        item = self._items.get(key, -1)

        if item == -1:
            return item

        # now that item has been accessed we need to update its order so that it is considered as the most
        # recently used item. For that we will delete it first and then add it back again
        del self._items[key]
        self.set(key, item)

        return item

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self._capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        # edge case
        if key is None:
            # key can't be None
            return

        # check for capacity full
        if len(self._items) == self._capacity:
            # remove the least recently used item
            self._items.popitem(False)

        self._items[key] = value

    def __repr__(self):
        return str(self._items)


def assert_(expected, actual):
    print(actual)
    assert expected == actual, f"expected={expected}, actual={actual}"


def test_cases():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    output = our_cache.get(1)  # returns 1
    assert_(1, output)

    output = our_cache.get(2)  # returns 2
    assert_(2, output)

    output = our_cache.get(9)  # returns -1 because 9 is not present in the cache
    assert_(-1, output)

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    output = our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    assert_(-1, output)

    # edge cases
    our_cache.set(None, None)
    output = our_cache.get(None) # should return -1
    assert_(-1, output)

    # check for different type keys like for example: string keys
    our_cache.set("hello", -8)
    output = our_cache.get("hello") # should return -8
    assert_(-8, output)

    # update the value of an existing key
    our_cache.set(1, 10)
    our_cache.set(2, 11)
    print(our_cache.get(1))  # should print 10
    assert(our_cache.get(1) == 10)

    print(our_cache.get(2))  # should print 11
    assert(our_cache.get(2) == 11)

    # 0 capacity cache
    zero_capacity_cache = LRU_Cache(0)
    zero_capacity_cache.set(1, 10) # should print warning message
    output = zero_capacity_cache.get(1)  # should print warning message and return -1
    print(output)
    assert (output is -1)


test_cases()



