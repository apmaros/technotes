# Heapsort
## Heap
A heap is a tree-based data structure in which a node is larger than all of its child elements. There are 2 types of heaps
- **max-heap** -  the largest element in a max-heap is stored at the root, and the subtree rooted at a node contains values no larger than that contained at the node itself. 
-  **min-heap** - The smallest element in a min-heap is at the root, and the subree rooted at a node contains values no smaller than that contained at the node itself

Heap can be implemented as an array object with the first element to be a root. Root is also to be the largest, or smallest element, based on the heap type. Heap does not maintain sorted array, but ensures that childrens of all nodes in binary tree are smaller, or larger than the node, based on the heap type.

The binary heap is a almost comlete binary tree. Binary tree data structure is mapped into array indices and can be expressed as:
- `parent(i) -> i / 2`
- `leftchild(i) -> 2 * i`
- `rightchild(i) -> 2 * i + 1`

Heap data structure is typically used for priority queues data structure

## Heapsort Properties
- time complexity O(n log n)
- in-place algorithm, does not need additional space during sort

## Algorithm Description
Heapsort algorithm has 2 main parts.

**build a max-heap**
```Python
for i in range(n, -1, -1):  
	max_heapify(items, n, i)  
```

**sort a the heapified array**
Because the array has already heap properties, the first element (`items[0]`) is the largest element.

We are sorting the array be stepping backwards from `n-1` ( `-1` is to prevent out-of-bounds error). On each step, the first element is replaced with the current index `i`. This is because we put the largest element at the curent index at the back of the array. This causes potential breach of heap properties, and therefore we heapify the array again.

```Python
for i in range(n-1, 0, -1):  
	items[i], items[0] = items[0], items[i]  # swap  
	 max_heapify(items, i, 0)  
```

Below diagram illusrates this 
![[Screen Shot 2019-01-03 at 07.36.14.png]]

## Implementation
```python
import typing as t  
  
  
def heapsort(items: t.List):  
    n = len(items)  
	
	# build a heap
    for i in range(n, -1, -1):  
        max_heapify(items, n, i)  

	# sort the heap
    for i in range(n-1, 0, -1):  
        items[i], items[0] = items[0], items[i]  # swap  
		 max_heapify(items, i, 0)  
  
  
def max_heapify(items, n, i):  
    largest = i  
  
    left = 2 * i  
    right = 2 * i + 1  
  
	# if left child is grater than root  
    # largest is the left child 
	if left < n and items[i] < items[left]:  
        largest = left  
  
    if right < n and items[largest] < items[right]:  
        largest = right  
  
    if largest != i:  
        items[i], items[largest] = items[largest], items[i]  
  
        max_heapify(items, n, largest)
```
