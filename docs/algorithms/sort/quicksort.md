# Quicksort

- time complexity - `O(n * log(n))`
- divide and conquer algorithm

Quicksort algorithm has 2 key parts:
- **pivot**: arbitrarily chosen element around which other elements will be partitioned
- **partitioning**: process placing all elements *smaller* than the pivot in the array to the left and larger to the right

Ideally the partition would be the median of the array. However, most textbooks selects first or last element of the array as the pivot. More about the runtime and pivot selection is in the Runtime Discussion section.

## Partitioning
Partitioning is based on two indexes `i` and `j`. Index `i` is the the index of element smaller, or equal than the pivot value. In our case, the pivot is at the last index processed by partition method - `pivot = items[high]`. 

Partitioning makes a single pass trough the array, not including the end index `for j in range(low, high)`. Each iteration increases the `j` index. On each iteration the `i` index is only increased if the value at `j` index is smaller, or equal to the pivot. If the value at the `j` index is smaller than the pivot, it also swaps the value of the smaller than the pivot `j` with `i`. Note that the increment of the `i` happens before the swap.

```Python
for j in range(low, high):  
    if items[j] <= pivot:  
        i += 1  
 items[i], items[j] = items[j], items[i]
```

Final step of the partitioning is to move the pivot value into the right place on the list. It should be after the last smallest element in the array. Index of this element will be also returned from the method.

```Python
items[i+1], items[high] = items[high], items[i+1]
```

## Runtime Discussion
Quicksort on average runs 2-3 times faster than *merge_sort*. If the data is mostly pre-sorted, then the runtime performance will be worse than expected, and will approach `O(n^2)`.

Ironically, the pre-sorted data takes longer to sort than the “random” data. The reason is because the pivot point will always be picked sub-optimally, with a “lopsided” partitioning of the data. When we pick this "lopsided" pivot, we are only reducing the problem size by one element. 
If the pivot were ideal, we would be reducing the problem size by half, since roughly half of the elements would be to the left of the pivot and the other half to the right.


```Python
import typing as t  
  
  
def quicksort(items: t.List):  
    _quicksort(items, 0, len(items)-1)  
  
  
def _quicksort(items: t.List, low: int, high: int):  
    if len(items) == 1:  
        return items  
    if low >= high:  
        return  
  
 pi = partition(items, low, high)  
  
    _quicksort(items, low, pi-1)  
    _quicksort(items, pi+1, high)  
  
  
def partition(items: t.List, low: int, high: int):  
    i = low - 1  
 pivot = items[high]  
  
    for j in range(low, high):  
        if items[j] <= pivot:  
            i += 1  
 items[i], items[j] = items[j], items[i]  
  
    items[i+1], items[high] = items[high], items[i+1]  
    return i + 1
```
