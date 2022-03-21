# Python Adhoc
**String to list of chars:**
```Python
s = "my-string"
s_chars = list(s)
```

**Sort**
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

**Seqs**
```python
l = [1,2,3]
another_l = [4,5,6]

# mutates, extends l with another_l
l.extend(another_l)
l
#> [1, 2, 3, 4, 5, 6]
# returns result without mutating lists
another_l + [7,8,9]
#> [4, 5, 6, 7, 8, 9]
```

**Iterate**
```Python
for i, n in enumerate([0,1,2]):
    print(f'i={i},n={n}')
#> i=0,n=0
#> i=1,n=1
#> i=2,n=2
```