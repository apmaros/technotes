# Sequences

Object is a sequence if it implements [collections.abc.MutableSequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence) abstract class.

Ojbect can be tested whether it is given seq with `issubclass(D, Sequence)`

```Python
class D:                                 # No inheritance
    def __init__(self): ...              # Extra method not required by the ABC
    def __getitem__(self, index):  ...   # Abstract method
    def __len__(self):  ...              # Abstract method
    def count(self, value): ...          # Mixin method
    def index(self, value): ...          # Mixin method

Sequence.register(D)                     # Register instead of inherit

```

## Sequence Operations

| Operation | Result |
| --------- | ------ |
| `x in s`| True if an item of s is equal to x, else False |
| `x not in s`| False if an item of s is equal to x, else True |
| `s + t`| the concatenation of s and t |
| `s * n or n * s` | equivalent to adding s to itself n times |
| `s[i]`| ith item of s, origin 0 |
| `s[i:j]` | slice of s from i to j |
| `s[i:j:k]` | slice of s from i to j with step k |
| `len(s)` | length of s |
| `min(s)` | smallest item of s |
| `max(s)` | largest item of s |
| `s.index(x[, i[, j]])` |  index of the first occurrence of x in s (at or after index i and before index j) |
| `s.count(x)` | total number of occurrences of x in s |

## Range

Immutable sequence type, typically used for looping a specific number of times in for loops.

- `range(start, stop[, step])`
  - start: **inclusive** start index
  - end: **exclusive** end index
  - step:
    - positive: the contents of a range r are determined by the formula `r[i] = start + step*i` where `i >= 0 and r[i] < stop`.
    - negative: the contents of the range are still determined by the formula `r[i] = start + step*i`, but the constraints are `i >= 0 and r[i] > stop`

```Python
list(range(10))
#> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 10))
#> [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 10, 2))
#> [1, 3, 5, 7, 9]
list(range(10, 0, -1))
#> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
