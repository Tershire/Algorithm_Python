# Q14_merge-two-sorted-lists.py
# LeetCode 21

# Tershire
# 2024 JUN 15


# KEY TAKEAWAY ****************************************************************
"""
multiple assignment pattern for linked list.
recursion termination condition using if, return, and backtracking.
"""


# case ////////////////////////////////////////////////////////////////////////
class List_Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(x: list):
    def create_node(x, i):
        if i == len(x):
            return None
        else:
            return List_Node(x[i], create_node(x, i + 1))

    linked_list = create_node(x, 0)
    return linked_list


x1, x2 = [1, 2, 4], [1, 3, 4]
list1, list2 = map(list_to_linked_list, [x1, x2])


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# collect vals in a list then convert to linked list
# timeout [ms]
def f1(list1: List_Node, list2: List_Node) -> List_Node:
    node1, node2 = list1, list2
    x = []
    while node1 or node2:
        if node1 and node2:
            if node1.val < node2.val:
                x.append(node1.val)
                node1 = node1.next
            else:
                x.append(node2.val)
                node2 = node2.next
        elif node1:
            while node1:
                x.append(node1.val)
                node1 = node1.next
        elif node2:
            while node1:
                x.append(node2.val)
                node2 = node2.next

    return list_to_linked_list(x)


# -----------------------------------------------------------------------------
# to descending linked list then reverse
# timeout [ms]
def f2(list1: List_Node, list2: List_Node) -> List_Node:
    a = None
    while list1 or list2:
        if list1 and list2:
            if list1.val < list2.val:
                a, a.next, list1 = list1, a, list1.next
            else:
                a, a.next, list2 = list2, a, list2.next
        elif list1:
            while list1:
                a, a.next, list1 = list1, a, list1.next
        elif list2:
            while list1:
                a, a.next, list2 = list2, a, list2.next

    # reverse
    q = None
    while a:
        q, q.next, a = a, q, a.next

    return q


# -----------------------------------------------------------------------------
# recursive: try
# incomplete [ms]
def f3(list1: List_Node, list2: List_Node) -> List_Node:
    # def collect(list1, list2):
    #     print(linked_list_to_list(list1))
    #     if not list1 and not list2:
    #         return list1
    #
    #     if list1 and list2:
    #         if list1.val < list2.val:
    #             a.next = collect(list1.next, list2)
    #         else:
    #             a.next = collect(list1, list2.next)
    #     elif list1:
    #         while list1:
    #             a.next = collect(list1.next, list2)
    #     elif list2:
    #         while list1:
    #             a.next = collect(list1, list2.next)
    #
    # return collect(list1, list2)
    pass


# -----------------------------------------------------------------------------
# recursive
# 16 [ms]
def f1B(list1: List_Node, list2: List_Node) -> List_Node:
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1

    if list1:
        list1.next = f1B(list1.next, list2)

    return list1


# test ////////////////////////////////////////////////////////////////////////
def linked_list_to_list(q: List_Node) -> list:
    x = []
    node = q
    while node:
        x.append(node.val)
        node = node.next

    return x


print(linked_list_to_list(f1(list1, list2)))

x1, x2 = [1, 2, 4], [1, 3, 4]
list1, list2 = map(list_to_linked_list, [x1, x2])
print(linked_list_to_list(f2(list1, list2)))

x1, x2 = [1, 2, 4], [1, 3, 4]
list1, list2 = map(list_to_linked_list, [x1, x2])
print(linked_list_to_list(f1B(list1, list2)))
