# Python builtin - Popular Functions Built in Python

## Builtin methods on sequences

### All, Any

- `all(iterable)` - True if *all* elements in iterable returns True
- `any(iterable)` - True if *any* element in iterable returns True

```Python
all([True, True, False])
#> False

any([True, True, False ])
#> True 
```

## Min and Max

```Python
min([100, 1, 15, 20])
#> 1
min(1, -4)
#> -4

min([100, 1, 15, 20])
#> 100
min(1, -4)
#> 1
```

### Sum

```Python
sum([0, 2, 5])
#> 7
```

### Zip

`zip(*iterables, strict=False)`

Iterate over several iterables in parallel, producing tuples with an item from each one

```Python
list(zip(items, ids))
#> [('sugar', 123), ('flower', 456), ('eggs', 789)]
```


## Sorted

Return a new sorted list from the items in iterable.

- `sorted(iterable, /, *, key=None, reverse=False)`
  - **key** specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, `key=lambda e: e[0]`)
  - **reverse** is a boolean value. If set to `True`, then the list elements are sorted as if each comparison were reversed.

### Enumerate

```Python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

list(enumerate(seasons, start=1))
```

## Higher Level Functions

### Filter

Filter is equivalent to `(item for item in iterable if function(item))`

```Python
list(filter(lambda e: len(e) > 1, [[1,2], [], [2]])
#> [[1, 2]]
```

### Map

```Python
list(map(lambda e: e.upper(), ['a', 'b', 'c']))
#> ['A', 'B', 'C']
```

### Reduce

```Python
import functools
print(functools.reduce(lambda acc, e,: e + acc, [1,2,3,4,5]))
```

### Reverse

Return a reverse iterator.

```Python
list(reversed([1,2,3,4,5,6]))
#> [6, 5, 4, 3, 2, 1]
```

## Char - To and From Unicode Point

`ord(c)` - Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
`chr(i)` - Returns the string representing a character whose Unicode code point is the integer i.

```Python
ord(a)
#> 97

chr(97)
#> 'a'
```

### Delete item

```Python
d = {1: 'a', 2: 'b'}
del d[1]
#> {2: 'b'}
```

## Round

Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

```Python
round(2.3)
#> 2

round(2.3333, 2)
#> 2.33
```
