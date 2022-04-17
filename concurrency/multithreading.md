# Multithreading

Multithreading is a model of a program execution, when multiple threads (units of execution) can be created and run independently on each other. Threads share the same resources.

Whether threads share a single resources and run concurrently, or run in parallel is defined by the multutihreding model.

## Multithreading Models

### Many-to-One Model (Green Threads, or Coroutines)

- the application can create any number of threads
- threads are executed concurrently
- threads are restricted to only the user space
- only one of these thread can access the kernel at the time and be scheduled
- provides a limited concurrency and does not exploit multiprocessors

![many-to-one-green-threads](../_assets/multithreading/multithreading-green-threads.png)

### One-to-One Model

- each user thread created by the application is known to the kernel and all threads can access the kernel at the same time
- the main problem with this model is that each thread creates more "weight" to the process. Hence many OS limit the number of threads supported on the system

### Many-to-Many Model (Java Native Threads)

- it leverages capabilities of the kernel while also enabling creation of thousands of user-level threads
- can take advantage of the multiprocessor environment

## Structured Concurrency

Structured concurrency is a property of concurrent programs, where the lifetimes of concurrent functions are cleanly nested. That is, if a function foo starts running a function bar in the background (bar runs concurrently to foo), then bar must finish before foo completes.

This is however not how a concurrent code is typically written. Whether it is thread, fibers or coroutines, they are spawend in the background without any supervision of or joining.[5]

Structured concurrency specifies that any threads started by a function must complete before the function existes. Also, in structured concurrency thread-related side effects are not permitted. [5]

A pure function can mute a local state but it is not permitted to mutate a global state.

## Reference

- [1] Class ReentrantReadWriteLock; <https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/locks/ReentrantReadWriteLock.html>
- [2] Chapter 2 Multithreading; <https://docs.oracle.com/cd/E19455-01/806-3461/6jck06gqe/index.html>
- [3] Process calculus; <https://en.wikipedia.org/wiki/Process_calculus>
- [4] Processes, threads, green threads, protothreads, fibers, coroutines: what's the difference?; <https://stackoverflow.com/questions/3324643/processes-threads-green-threads-protothreads-fibers-coroutines-whats-the>
- [5] Structured concurrency and pure functions; <https://blog.softwaremill.com/structured-concurrency-and-pure-functions-92dd8ed1a9f2>
