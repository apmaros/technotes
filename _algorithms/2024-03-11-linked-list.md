---
layout: post
title:  "Linked List"
date:   2024-03-11
categories: list
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
        # List is already empty
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
{% endhighlight %}
  
