# Python Data Structures
This page describes basic Python's native data structures such as arrays, lists, dictionaries and others. Most of the text are notes taken from [Common Python Data Structures](https://realpython.com/python-data-structures/)
## Array - `array.array`
It is a contigous data structure as a data is stored in adjoining block of memory. 
Main benefit is fast O(1) lookup
```python
from array import array

# array(<type code>)
arr = array('i') # signed char type code
arr.append(1)
```

docs: [docs.python.org - array](https://docs.python.org/3/library/array.html)

## List
List is a mutable dynamic array, able to hold arbitrary objects (everything in Python is an object). Objects in array can be mixed.

docs:  [Data Structures- 5.1. More on List](https://docs.python.org/3/tutorial/datastructures.html)

```python
list = ['one', 'two']
```

## Tuples
Tuples are immutable sequences (unlike mutable Lists)

```python
arr = ("one", "two", "three")
```

## Bytes
Bytes objects are immutable sequences of single bytes, or integers in the range 0 ≤ _x_ ≤ 255. They are sumilar to `str` and can also be though of as _immutable_ arrays of bytes.

```python
arr = bytes((0, 1, 2, 3))
```

## Bytearray
A mutable arrays of single bytes. Same as `bytes` but mutable

```python
arr = bytearray((0, 1, 2, 3))
```

## Dict
```python
person = {
	"name": "Art Vandelay",
	"age": 33
}
```

## Namedtuple
Convenient data objects allowing to define reusable blueprints for the records that ensure the correct field names.

```python
from collections import namedtuple

point = namedtuple("Point", "x y z")(1, 2, 3)

Car = namedtuple("Car" , "color mileage automatic")
red_car = Car("red", 3812.4, True)
```

## Imporved NamedTuple -`typing.NamedTuple`
Improved `NamedTuples` including (since `Python 3.6`) with updated syntax for defining new record types and added support for type hints.

```python
from typing import NamedTuple
class Person(NamedTuple):
	name: str
	age: int
```


## Struct - `struct.Struct`
The `struct.Struct` class converts between Python values and C structs serialized into Python bytes objects.

```python
from struct import Struct
MyStruct = Struct("i?f")
data = MyStruct.pack(23, False, 42.0)

# data
# > b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'

# Data blobs can be unpacked again:
MyStruct.unpack(data)
(23, False, 42.0)
```


## Set
Set is mutable and backed by the dictionary. Any hashable object can be stored in a set
```
vowels = {"a", "e", "i", "o", "u"}
s = set()
s.add(1)
"e" in vowels
# > True
```

[Built-in Types - Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

## frozenset
Immutable version of the set

```python
vowels = frozenset({"a", "e", "i", "o", "u"})
```

[Built-in Types _class_ `frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset)

## Multisets - `collections.Counter`
Multiset, alowing to keep track of elements occurance.

```python
from collections import Counter

inventory = Counter()
inventory.update({"sword": 1, "bread": 3})
```

## Dequeue - `collections.deque`
The [dequeue](https://docs.python.org/3/library/collections.html#collections.deque) implements a double-ended queue with `append` and `pop` having O(1) time (non-amortized). Because of its non-amortize `append` and `pop` performance, it is preffered for stack implementation in compare to list (array).

It is implemented as [doubly-linked list](https://github.com/python/cpython/blob/6e8128f02e1d36e38e5866f9dc36e051caa47bc9/Modules/_collectionsmodule.c#L33-L35)

**FIFO Queue**: Ideal datastructure for implementing a fifo queue due its fast O(1) insert and delete at the beginning and end of the queue.

- [collections.dequeue](https://realpython.com/linked-lists-python/#introducing-collectionsdeque)

```python
from collections import deque

q = deque()
q.append("first")
q.append("second")
q.popleft()
#> "first"
```

## Lifo Queue - `queue.LifoQueue`
[LifoQueue](https://docs.python.org/3/library/queue.html#queue.LifoQueue) is a synchronized, threadsafe stack implementation. It is a blocking on `get` method, or non-blocking on `get_nowait` method.

```python
from queue import LifoQueue

q = LifoQueue()
q.put("myItem")
```

## Queue - `queue.Queue`
The Queue is a synchronized datastructure (threadsafe) and provides locking semantics to support multiple concurrent producers nad consumers.

```python
from queue import Queue

q = Queue()
q.put("first")
q.put("second")

q.get()
#> "first"
q.get()
#> "second"

q.get_nowait()
#> queue.Empty

q.get() # blocks until receives new item, forever in this case
```

## Shared Job Queues `multiprocessing.Queue`
It is a shared job queue implementation that allows queued items to be processed in parallel by multiple workers. Process-based paralellization is possible in CPython because a global interpretter lock (GIL). GIL prevents some forms of parallel execustions on a single interpreter process. (_It is however likely to be changed due to latest [proposal](https://mail.python.org/archives/list/python-dev@python.org/thread/ABR2L6BENNA6UPSPKV474HCS4LWT26GY/) to remove GIL_).

Multiprocessing queue is a specialized queue implementation meant for sharing data between processis. It makes it easy to distribute work across multiple processes and avoid GIL limitations.

It can store and transfer any [pickeable](https://realpython.com/python-pickle-module/) object across process boundaries

## Heap queue algorithm `heapqueue`
The [heapq](https://docs.python.org/3/library/heapq.html#module-heapq) algorithm is also known as the priority queue algorithm.

> Heaps are binary trees for which every parent node has a value less than or equal to any of its children.

It supports insertion and exctraction of the smallert element in O(log n) time. It provides only min-heap implementation, hence additional implementation is required for priority queue feature parity.

```python
import heapq
q = []
heapq.heappush(q, (2, "first"))
heapq.heappush(q, (1, "second"))
heapq.heappush(q, (3, "third"))

while q:
     next_item = heapq.heappop(q)
     print(next_item)

#> (1, 'first')
#> (2, 'second')
#> (3, 'third')
```
## Priority Queue - `queue.PriorityQueue`

Priority queue is internally built on the `heapq` and is synchronised.

```python
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, "second"))
q.put((1, "first"))
q.put((3, "third"))

while not q.empty():
    next_item = q.get()
    print(next_item)
```



# TODO
- [ ] Think about API for each major data structure
- [ ] How does these Python data structures map to basic DS data structures?