---
layout: post
title:  "Linked List"
date:   2024-03-11
categories: algo
tags: node linked list
---

{% highlight python %}
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def _get_sum(node: Node) -> int:
    result = 0
    curr = node

    while curr:
        result += curr.val
        curr = curr.next

    return result


def get_sum_rec(node: Node) -> int:
    if not node:
        return 0

    return node.val + get_sum_rec(node.next)


class NumberLinkedList:
    head: Node = None

    def get_sum(self):
        return _get_sum(self.head)

    def add(self, num: int):
        if not self.head:
            self.head = Node(num)

            return self

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(num)

        return self

    def delete(self, num: int):
        if not self.head:
            raise ValueError(f"Number {num} not in the list")

        curr = self.head
        prev = None

        while curr:
            if curr.val == num:
                # first node
                if not prev:
                    self.head = curr.next
                    return self

                prev.next = curr.next

                return self

            prev = curr
            curr = curr.next

        raise ValueError(f"Number {num} not in the list")

    def to_arr(self):
        if not self.head:
            return []

        curr = self.head

        items = []

        while curr:
            items.append(curr.val)
            curr = curr.next

        return items

    def __str__(self):
        if not self.head:
            return ""

        curr = self.head
        s = f"{curr.val}"
        curr = curr.next

        while curr:
            s += f"-> {curr.val}"
            curr = curr.next

if __name__ == '__main__':
    l = NumberLinkedList()
    l.add(10).add(4).add(13).add(1)

    assert 28 == l.get_sum()
    assert 28 == get_sum_rec(l.head)

    assert l.to_arr() == [10, 4, 13, 1]
    assert l.delete(4).to_arr() == [10, 13, 1]

{% endhighlight %}

## Linked list with sentinel nodes
It is a linked list with maintaining nodes at the head and tail of the linked list. Sentinel nodes are also present in empty linked list. They are however not part of the list

For this purpose we will use a DoublyNodes containing pointers to next and previous node as well

{% highlight python %}

class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class SentinelLinkedList:
    def __init__(self):
        self.head = DoublyNode(None)
        self.tail = DoublyNode(None)

        self.head.next = self.tail
        self.tail.next = self.head

    def remove_left(self):
        if self.head == self.tail:
            return

        to_remove = self.head.next
        self.head.next = to_remove.next
        to_remove.next.prev = self.head

    def remove_right(self):
        if self.head == self.tail:
            return

        to_remove = self.tail.prev
        self.tail.prev = to_remove.prev
        to_remove.prev.next = self.tail

    def peek_left(self):
        return self.head.val

    def peek_right(self):
        return self .tail.val
{% endhighlight %}

## Example Problems

{% highlight python %}

def find_middle(head: Node):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


def has_cycle(head: Node):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def has_cycle_hash(head: Node):
    seen = set()

    current = head
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next

    return False


def get_node(head: Node, k: int) -> int:
    slow = fast = head
    counter = 0

    while fast.next and counter < k:
        fast = fast.next
        counter += 1

    if counter != k:
        raise ValueError(f'Out of bounds, found {counter} elements')

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.val


def deduplicate(head: Node) -> Node:
    if not head:
        return head

    prev = head
    curr = head.next

    while curr:
        if prev.val == curr.val:
            prev.next = curr.next
            curr = curr.next
        else:
            curr = curr.next
            prev = prev.next

    return head
{% endhighlight %}
