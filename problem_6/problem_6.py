"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next

        out_string += "None"
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        return [n for n in self]

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next


def union(llist_1, llist_2):
    if llist_1 is None and llist_2 is None:
        return LinkedList()
    elif llist_1 is None:
        return llist_2
    elif llist_2 is None:
        return llist_1

    # a common dictionary/hashtable to maintain elements encountered in both lists,
    # I am dict for fast insert/search operations to keep my overall time complexity minimum
    common_dict = {}

    # go through first list and mark items encountered
    for item in llist_1:
        common_dict[item] = True
    # go through second list and mark items encountered
    for item in llist_2:
        common_dict[item] = True

    # now add items encountered in either list to resultant list
    union_linked_list = LinkedList()
    for item, status in common_dict.items():
        union_linked_list.append(item)

    return union_linked_list


def intersection(llist_1, llist_2):
    if llist_1 is None:
        return LinkedList()
    elif llist_2 is None:
        return LinkedList()

    l1_set = set(llist_1)
    l2_set = set(llist_2)
    intersection_result = l1_set.intersection(l2_set)
    intersection_result_linked_list = LinkedList()
    for value in intersection_result:
        intersection_result_linked_list.append(value)

    return intersection_result_linked_list


def test_case(list1, list2, expected_union_sorted_output, expected_intersection_sorted_output):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in list1:
        linked_list_1.append(i)

    for i in list2:
        linked_list_2.append(i)

    union_output = union(linked_list_1, linked_list_2).to_list()
    # NOTE: I am sorting the output so that I can add asserts otherwise order will be not defined
    union_output.sort()
    print(union_output)
    assert (union_output == expected_union_sorted_output)

    intersection_output = intersection(linked_list_1, linked_list_2).to_list()
    # NOTE: I am sorting the output so that I can add asserts otherwise order will be not defined
    intersection_output.sort()
    print(intersection_output)
    assert (intersection_output == expected_intersection_sorted_output)


def test():
    # Test case 1
    print("--------> Test-1")
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    expected_union_output = [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]
    expected_intersection_output = [4, 6, 21]
    test_case(element_1, element_2, expected_union_output, expected_intersection_output)


    # Test case 2
    print("--------> Test-2")
    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    expected_union_output = [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]
    expected_intersection_output = []
    test_case(element_1, element_2, expected_union_output, expected_intersection_output)

    # Test case 3
    print("--------> Test-3")
    element_1 = [5, 6, 4, -1]
    element_2 = [1, 2, 3, -1]
    expected_union_output = [-1, 1, 2, 3, 4, 5, 6]
    expected_intersection_output = [-1]
    test_case(element_1, element_2, expected_union_output, expected_intersection_output)

    # Edge cases
    # Test case 4
    print("--------> Test-4")
    element_1 = []
    element_2 = []
    expected_union_output = []
    expected_intersection_output = []
    test_case(element_1, element_2, expected_union_output, expected_intersection_output)

    # Test case 4
    print("--------> Test-5")
    union_output = union(None, None).to_list()
    print(union_output)  # should print []
    assert(union_output == [])
    intersection_output = intersection(None, None).to_list()
    print(intersection_output)  # should print []


test()