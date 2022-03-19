# Binary Search
```python
import typing as t  
  
  
def binary_search(items: t.List[int], target: int) -> bool:  
    low = 0  
 high = len(items) - 1  
  
 while low <= high:  
        mid = (high + low) // 2  
  
 if target == items[mid]:  
            return mid  
  
        if target < items[mid]:  
            high = mid - 1  
 else:  
            low = mid + 1  
  
 return None
```