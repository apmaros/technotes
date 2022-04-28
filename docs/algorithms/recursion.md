# Recursion

A recursive function is calling itself in order to calculate the result. Each time the funcion is called, it reduces the problem by calling itself with a smaller problem.

**base case** - a terminating condition that stops the recursion and returns the result

## Recursion with Accumulator

```python
def reverse_string(s: str) -> str:
    return _reverse_string(list(s), [])

def _reverse_string(s, acc) -> str:
    if s:
        acc.append(s.pop())
        _reverse_string(s, acc)

    return ''.join(acc)
```

## Recursion bottom up

### Reverse List

![recursion-bottom-up](../_assets/algos/recursion.png)

```Python
def reverse(head: ListNode, debug_on=False, i=0):
  # base case
    if head is None or head.next is None:
        return head

    if debug_on: print(f"current-head={head.val}, i={i}")
  # `head.next` - progress to next element
    rest = reverse(head.next, debug_on, i+1)

    if debug_on: print(f"swapping head={head.val} with next-head={head.next.val}, i={i}")
    # when we have reached the end recursion,
    # the operations will be applied first 
    # to the last elements wrapping back to
    # the first element
    head.next.next = head
    head.next = None

    return rest
```

### Swap Pairs

```Python
def swap_pairs(head: LLNode):
    if head is None or head.next is None:
        return head

    print(f"before val={head.val}")
    print(f"before val next={head.next.val}")

    first_node = head
    second_node = head.next

    first_node.next = swap_pairs(second_node.next)
    first_node.next = first_node

    print(f"after val={head.val}")
    print(f"after val next={head.next.val}")

    return second_node


if __name__ == '__main__':
    print(''.join(reverse_string(list('john doe'))))
    # l = LLNode(1, LLNode(2, LLNode(3, LLNode(4, LLNode(5, LLNode(6))))))
```

## Linked List

```Python
class ListNode:
    def __init__(self, value, node=None):
        self.next: ListNode = node
        self.val: int = value

    def append(self, val):
        curr = self
        while curr.next:
            curr = curr.next

        curr.next = ListNode(val)

        return self

    def append_i(self, val):
        if self.next is None:
            return ListNode(val, self)

        self.append(self.next)

    def prepend(self, val):
        return ListNode(val, self)

    def __repr__(self):
        acc = []
        curr = self
        while curr:
            acc.append(str(curr.val))
            curr = curr.next

        return '->'.join(acc)
```

## BST - Binary Search Tree

```Python
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def add(self, val):
        if val < self.val:
            if self.left is not None:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right is not None:
                self.right.add(val)
            else:
                self.right = Node(val)

        return self
```

### Merge Linked Lists

```Python
    from typing import Optional

    def mergeTwoLists(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

### Mirror Tree

Determine, whether one node is a mirror image of another node.

```Python
def is_mirror(head: Node, another_head: Node, ) -> bool:
    """
    we will traverse the tree until we find difference
    or the whole tree was traversed

    @return True if head is identical to another_head
    and false if they are different


               20
              /  \
            10    40
           / \    / \
          4  14  21  45
    """

    if head is None and another_head is None:
        return True

    if head is None or another_head is None:
        return False

    print(f'comparing {head.val} with {another_head.val}')
    if head.val != another_head.val:
        return False

    return is_mirror(head.left, another_head.left) and is_mirror(head.right, another_head.right)
```

#### Test

```Python
if __name__ == '__main__':
    n = Node(20).add(10).add(40).add(4).add(14).add(21).add(45)
    longer_n = Node(20).add(10).add(40).add(4).add(14).add(21).add(45).add(2)
    an = Node(20).add(10).add(40).add(5).add(14).add(21).add(45)

    assert is_mirror(n, n)
    assert not is_mirror(n, longer_n)
    assert not is_mirror(n, an)
```
