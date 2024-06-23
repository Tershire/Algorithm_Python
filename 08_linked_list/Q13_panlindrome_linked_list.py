# Q13_panlindrome_linked_list.py
# LeetCode 234

# Tershire
# 2024 JUN 14


import collections


# KEY TAKEAWAY ****************************************************************
"""
runner.
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


x = [1, 2, 2, 1]
# x = [1, 2]
x = [1, 2, 3, 4]
head = list_to_linked_list(x)
print(head)
print(head.val, head.next)
print(head.next.val, head.next.next)


# algo ////////////////////////////////////////////////////////////////////////
# -----------------------------------------------------------------------------
# convert to list then check
# 777 [ms]
def f1(head: List_Node) -> bool:
    x = []
    node = head
    while node is not None:
        x.append(node.val)
        node = node.next

    print(x)
    return x == x[::-1]


# -----------------------------------------------------------------------------
# convert to list then check: pop()
# 1228 [ms]
def f1B(head: List_Node) -> bool:
    x = []
    node = head
    while node is not None:
        x.append(node.val)
        node = node.next

    while len(x) > 1:
        if x.pop(0) != x.pop():
            return False

    return True


# -----------------------------------------------------------------------------
# convert to deque then check
# 786 [ms]
def f2B(head: List_Node) -> bool:
    x = collections.deque()
    node = head
    while node is not None:
        x.append(node.val)
        node = node.next

    while len(x) > 1:
        if x.popleft() != x.pop():
            return False

    return True


# -----------------------------------------------------------------------------
# runner
# 520 [ms]
def f2B(head: List_Node) -> bool:
    q = None
    fast = slow = head

    # create half-reverse-ordered linked list: q
    while fast and fast.next:
        fast = fast.next.next
        q, q.next, slow = slow, q, slow.next

    # processing for case: odd-length linked list
    if fast:
        slow = slow.next

    # check symmetry
    while q and q.val == slow.val:
        slow, q = slow.next, q.next

    return not q


# test ////////////////////////////////////////////////////////////////////////
print(f1(head))
print(f1B(head))
print(f2B(head))
