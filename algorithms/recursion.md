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