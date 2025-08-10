---
layout: post
title:  AsyncIO
date:   2025-08-09
categories: asyncio
tags: concurrency coroutines asyncio
---

It is convenient to process I/O intensitve operation concurrently. If a method spends time waiting for response from I/O, we can safely assume that it is not doing anything useful and it can yield execution. In asynchronous programming, the event loop suspends the waiting task and registers interest in its I/O operation with the operating system. 

When the OS signals that the I/O is ready, the event loop resumes the task. In Python `asyncio` the execution of task execution is handled by a single main thread concurrently, not in parallel. For I/O-bound workloads this simplifies the execution and often can perform better than in parallel as it does not need to coordinate thread execution.


## Simple example

```python
import asyncio
import time
from dataclasses import dataclass


async def hello():
    print("Hello")
    await asyncio.sleep(5)
    print("World")


async def main():
    await asyncio.gather(hello(), hello(), hello())


if __name__ == '__main__':
    start = time.perf_counter()

    asyncio.run(main())

    print(f"{__file__} executed in {(time.perf_counter() - start):0.2f} seconds.")
```

## Chaining

```Python
@dataclass
class User:
    user_id: int
    user_name: str


@dataclass
class UserWithOrders:
    user: User
    orders: list


async def fetch_orders(user_id: int) -> list:
    orders = {
        1: [1, 3, 10, 11],
        2: [23, 34],
        3: [],
    }
    return orders.get(user_id, [])


async def fetch_user(user_id: int) -> dict:
    return User(user_id=user_id, user_name=f"user-{user_id}")


async def get_user_with_orders(user_id: int) -> UserWithOrders:
    user, orders = await asyncio.gather(fetch_user(user_id), fetch_orders(user_id))

    return UserWithOrders(user=user, orders=orders)


if __name__ == '__main__':
    user_w_orders = asyncio.run(get_user_with_orders(1))
    assert user_w_orders == UserWithOrders(User(1, "user-1"), [1, 3, 10, 11])
```