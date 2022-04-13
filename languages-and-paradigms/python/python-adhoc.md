# Python Adhoc

## String to list of chars

```Python
s = "my-string"
s_chars = list(s)
```

## Sort

```Python
l = [6,4,3,5,6]
# returns sorted array
sorted(l)
#> [3, 4, 5, 6]

# mutates the array
l.sort() # outputs None
l
#> [3, 4, 5, 6]

# sort by key
intv = [[0,30],[15,20],[5,10]]
intv.sort(key = (lambda e: e[0]))
intv
#> [[0, 30], [5, 10], [15, 20]]
```

## Seqs

```python
l = [1,2,3]
another_l = [4,5,6]

# mutates, extends l with another_l
l.extend(another_l)
l
#> [1, 2, 3, 4, 5, 6]
# returns result without mutating lists
another_l + [7,8,9]
# mutate and add to another_l
#> [4, 5, 6, 7, 8, 9]
another_l += [7,8,9,10]
l
#> [4, 5, 6, 7, 8, 9]
```

## Iterate

```Python
for i, n in enumerate([0,1,2]):
    print(f'i={i},n={n}')
#> i=0,n=0
#> i=1,n=1
#> i=2,n=2
```

## Defaultdict

read more in [API Doc](https://docs.python.org/3/library/collections.html#collections.defaultdict)

```python
from collections import defaultdict

items_agg = defaultdict(list)
items = [(1, 'foo'), (2, 'bar'), (1, 'bum'), (2, 'been')]

for i, word in items:
    items_agg[i].append(word)

dict(items_agg)
#> {1: ['foo', 'bum'], 2: ['bar', 'been']}
```

## Bisect

It is a mode that provides support for maintaining a list in sorted order without having to sort the list after each insertion. [bisect — Array bisection algorithm](https://docs.python.org/3/library/bisect.html#bisect.bisect_left)

- `bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)`
  - Locate the insertion point for x in a to maintain sorted order.
  - The parameters lo and hi may be used to specify a subset of the list which should be considered, by default the entire list is used
  - If x is already present in a, the insertion point will be before (to the left of) any existing entries
  - The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.

- `bisect.insort(a, x, lo=0, hi=len(a), *, key=None)`
  - Insert x in a in sorted order
  - complexity - O(N) due to `insert` being O(N)

```Python
    l = [6, 10, 11]
    r = bisect.bisect_left(l, 7)
    l.insert(r, 7)
    l
    #> [6, 7, 10, 11]
```
