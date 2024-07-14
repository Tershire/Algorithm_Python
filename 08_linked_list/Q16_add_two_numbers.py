# Q16_add_two_numbers.py
# LeetCode 2

# Tershire
# 2024 JUN 25


# KEY TAKEAWAY ****************************************************************
"""

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


x = [2, 4, 3]
y = [5, 6, 4]
x = [2, 4, 9]
y = [5, 6, 4, 9]
l1 = list_to_linked_list(x)
l2 = list_to_linked_list(y)


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# define custom linked list class. reverse explicitly.
# 49 [ms]
def f1(l1, l2):
    n1, n2 = "", ""
    node1, node2 = l1, l2
    while node1 is not None:
        n1 += str(node1.val)
        node1 = node1.next
    while node2 is not None:
        n2 += str(node2.val)
        node2 = node2.next

    n1, n2 = n1[::-1], n2[::-1]

    v = None
    if n1 and n2:
        v = str(int(n1) + int(n2))

    print(n1, n2)
    # print(v)

    class List_Node(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def string_to_linked_list(x: str):
        def create_node(x, i):
            if i == len(x):
                return None
            else:
                return List_Node(x[i], create_node(x, i + 1))

        linked_list = create_node(x, 0)
        return linked_list

    return string_to_linked_list(v[::-1])


# -----------------------------------------------------------------------------
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# define custom methods. reverse explicitly.
# 51 [ms]
def f1B(l1, l2):
    def reverse_linked_list(q: ListNode) -> ListNode:
        node, prev = q, None
        while node:
            next, node.next = node.next, prev
            node, prev = next, node

        return prev

    def linked_list_to_list(q: ListNode) -> list:
        x = []
        while q:
            x.append(q.val)
            q = q.next

        return x

    def list_to_reversed_linked_list(x: list) -> ListNode:
        prev = None
        for v in x:
            node, node.next = ListNode(v), prev
            prev = node

        return node

    a = linked_list_to_list(reverse_linked_list(l1))
    b = linked_list_to_list(reverse_linked_list(l2))
    v = int(''.join(str(c) for c in a)) + int(''.join(str(c) for c in b))

    return list_to_reversed_linked_list(str(v))


# test ////////////////////////////////////////////////////////////////////////
def linked_list_to_list(q: List_Node) -> list:
    x = []
    node = q
    while node:
        x.append(node.val)
        node = node.next

    return x

c = f1(l1, l2)
print(linked_list_to_list(c))

c = f1B(l1, l2)
print(linked_list_to_list(c))
