```python
class MinHeap:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.heap = [0] * (self.size + 1)

    def add(self, num):
        if self.count > self.size + 1:
            raise IndexError("Heap out of bounds")

        self.count += 1

        i = self.count

        self.heap[i] = num

        parent = i // 2

        while self.heap[i] < self.heap[parent] and i > 1:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            i = parent
            parent = i // 2

    def peek(self):
        return self.heap[1]
```
