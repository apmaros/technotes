# Mergesort

Mergesort is a divide and conquer algorithm hence sorts the array in steps:
1. splits the array into 2 parts
2. sorts each part recursivelly
3. combines results of each recursive call

Mergesort keeps dividing an array of items into halfs until there are only 2 items in the array. Following condition is the recursion base case. When the size of the array is reduced to 2 items we stop recursion and simply compare the these items.
```Python
if len(items) < 2:  
        return items  
```
The next step after recursion reached its bottom is merging the partial results back. It is important to note, that the partial results are already sorted. Starting with 2 items at the bottom of the recursion, continuing level up. 
```Python
import typing as t  
  
  
def merge_sort(items: t.List):  
    if len(items) < 2:  
        return items  
  
 # `x // y` - floor div  
 middle = len(items) // 2  
  
 return _merge(  
        left=merge_sort(items[:middle]),  
 right=merge_sort(items[middle:])  
    )  
  
  
def _merge(left: t.List, right: t.List) -> t.List:  
    """  
 Receives two different sorted arrays and merges them. :returns a single sorted array """  
 if not left:  
        return right  
  
    if not right:  
        return left  
  
    left_index = right_index = 0  
  
 result = []  
  
    while len(result) < len(left) + len(right):  
        if left[left_index] < right[right_index]:  
            result.append(left[left_index])  
            left_index += 1  
 else:  
            result.append(right[right_index])  
            right_index += 1  
  
 if len(left) == left_index:  
            result += right[right_index:]  
            break  
  
 if len(right) == right_index:  
            result += left[left_index:]  
            break  
  
 return result
```


```Python
from src.algorithms.sort.merge_sort import merge_sort  
  
  
def test_merge_sort_sorts_array():  
    items = [0, 3, 1, 9, 2, 6, 3]  
    assert merge_sort(items) == [0, 1, 2, 3, 3, 6, 9]
```