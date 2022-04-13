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

*TBD*

## Reference

- [1] Class ReentrantReadWriteLock; <https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/locks/ReentrantReadWriteLock.html>
- [2] Chapter 2 Multithreading <https://docs.oracle.com/cd/E19455-01/806-3461/6jck06gqe/index.html>
- [3] Process calculus <https://en.wikipedia.org/wiki/Process_calculus>
- [4] Processes, threads, green threads, protothreads, fibers, coroutines: what's the difference? <https://stackoverflow.com/questions/3324643/processes-threads-green-threads-protothreads-fibers-coroutines-whats-the>
