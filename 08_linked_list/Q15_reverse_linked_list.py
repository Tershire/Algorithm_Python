# Q15_reverse-linked-list.py
# LeetCode 206

# Tershire
# 2024 JUN 23


# KEY TAKEAWAY ****************************************************************
"""
compare recursive and iterative concepts and mechanisms. (next, node, prev)
- next: keep the next head-tail of the original linked list.
- node: copies next to be a temporary head-tail, and let next keep the next.
- prev: replace the tail of node by itself the keep the newly head-attache tail.
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


x = [1, 2, 3, 4, 5]
head = list_to_linked_list(x)


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# multi-assignment pattern.
# 14.7 [ms]
def f1(head: List_Node) -> List_Node:
    q = None
    while head:
        q, q.next, head = head, q, head.next

    return q


# -----------------------------------------------------------------------------
# recursive
# 20 [ms]
def f1B(head: List_Node) -> List_Node:
    def reverse(node: List_Node, prev: List_Node = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


# -----------------------------------------------------------------------------
# iterative
# 16.7 [ms]
def f2B(head: List_Node) -> List_Node:
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


# test ////////////////////////////////////////////////////////////////////////
def linked_list_to_list(q: List_Node) -> list:
    x = []
    node = q
    while node:
        x.append(node.val)
        node = node.next

    return x


x = [1, 2, 3, 4, 5]
head = list_to_linked_list(x)
print(linked_list_to_list(f1(head)))

x = [1, 2, 3, 4, 5]
head = list_to_linked_list(x)
print(linked_list_to_list(f1B(head)))

x = [1, 2, 3, 4, 5]
head = list_to_linked_list(x)
print(linked_list_to_list(f2B(head)))
