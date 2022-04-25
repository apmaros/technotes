# Java Multithreading

<!-- 
    - runable and how to run a thread
    - thread pool and scheduled thread pool
    - runnable
    - locks
    - volatile
 -->

## Synchronised and Happened-Before Relationship

```Java
ExecutorService executor = Executors.newFixedThreadPool(2);

IntStream.range(0, 10000)
    .forEach(i -> executor.submit(this::incrementSync));

stop(executor);

System.out.println(count);
```

Synchronised is also available in a block statement

```Java
void incrementSync() {
    synchronized (this) {
        count = count + 1;
    }
}
```

Synchronisation is built around an internal entity known as the **intrinsic lock**, or **lock monitor**. Every object has an intrinsic lock associated with it. If a thread needs an exclusive access to the object, it has to acquire its intrinsic lock before accessing them and release it when it is done. [1]

A thread owns the intrinsic lock after it has acquired it and before it has released the lock. When other thread tries to acquire the lock, or access the object it will be blocked until the lock is released. When a thread invokes a synchronized method, it automatically acquires the intrinsic lock for that method's object and releases it when the method returns. The lock release occurs even if the return was caused by an uncaught exception. [2]

Intrinsic lock has a reentrant characteristics. It means that a thread owning a lock can safely re-acquire it multiple times without the risk of running into the deadlock. [1]

### Happens Before Relationship

Multi-core processors are able to run multiple threads per core. Each core has number of levels of its own local cache. When a process operates on a shared variables, there can be delay between modifying the variable and when the variable is written to main memory accessible by all threads. This can cause that another thread could access stale value.

This can be observed by following example:

```Java
public class StopThread {
        private static boolean stopRequested;
        public static void main(String[] args)
                throws InterruptedException {
            Thread backgroundThread = new Thread(new Runnable() {
                public void run() {
                    int i = 0;
                    while (!stopRequested)
                        i++;
                }
            });
            backgroundThread.start();
            TimeUnit.SECONDS.sleep(1);
            stopRequested = true;
        }
    }
```

There is no guarantee that the change of the value in “stopRequested” variable (from the main thread) becoming visible to the “backgroundThread” that we created. As the write operation to the “stopRequested” variable to true from the main method is invisible to the “backgroundThread”, it will go into an infinite loop.[3]

The reason can be explain as following:

- The main thread and our “backgroundThread” is running on two different cores inside the processor.
- The “stopRequested” will be loaded into the cache of the core that executes the “backgroundThread”.
- The main thread will keep the updated value of the “stopRequested” value in a cache of a different core. Since now the “stopRequested” value resides in two different caches, the updated value may not be visible to the “backgroundThread”.

To avoid this problem, java has introduced happens-before relationship defined as:

- Two actions can be ordered by a happens-before relationship.
- If one action happens-before another, then the first is visible to and ordered before the second.

According to this, if there is a happens-before relationship between a write and read operation, the results of a write by one thread are guaranteed to be visible to a read by another thread. Therefore, we will be able to maintain the memory consistency if we are able to have the happens-before relationship between our actions.

```Java
public class StopThread {
        private static boolean stopRequested;
        private static synchronized void requestStop() {
            stopRequested = true;
        }
        private static synchronized boolean stopRequested() {
            return stopRequested;
        }
        public static void main(String[] args)
                throws InterruptedException {
            Thread backgroundThread = new Thread(new Runnable() {
                public void run() {
                    int i = 0;
                    while (!stopRequested())
                        i++;
                }
            });
            backgroundThread.start();
            TimeUnit.SECONDS.sleep(1);
            requestStop();
        }
    }
```

Synchronised can be used achieved to happens-before relationship. When a thread releases an intrinsic lock, a happens-before relationship is established between that action and any subsequent acquisition of the same lock.[2]

Using synchronization has an impact on the performance as threads are blocked while acquiring the lock. That is why it should be used mainly for a exclusive access of threads to a shared state.

```Java
public class StopThread {
        private static boolean stopRequested;
        private static synchronized void requestStop() {
            stopRequested = true;
        }
        private static synchronized boolean stopRequested() {
            return stopRequested;
        }
        public static void main(String[] args)
                throws InterruptedException {
            Thread backgroundThread = new Thread(new Runnable() {
                public void run() {
                    int i = 0;
                    while (!stopRequested())
                        i++;
                }
            });
            backgroundThread.start();
            TimeUnit.SECONDS.sleep(1);
            requestStop();
        }
    }
```

If exclusiveness is not required, happens-before realationship can also be establisted by using a `volatile` field modifier.

Changes to a volatile variable are always visible to other threads. What's more, it also means that when a thread reads a volatile variable, it sees not just the latest change to the volatile, but also the side effects of the code that led up the change. [4]

### Java Lock

Lock objects work very much like the implicit locks used by synchronized code.

The biggest advantage of Lock objects over implicit locks is their ability to back out of an attempt to acquire a lock. The `tryLock` method backs out if the lock is not available immediately or before a timeout expires (if specified). The lockInterruptibly method backs out if another thread sends an interrupt before the lock is acquired.

Lock implementations implement a Lock interface. With increased flexibility comes also increased responsibility to release the lock not required when using a `synchronized` methods, or blocks. Typically a following idiom should be followed:

```Java
 Lock l = ...;
 l.lock();
 try {
   // access the resource protected by this lock
 } finally {
   l.unlock();
 }
```

Some of the lock implementations are:

- ReentrantLock - a mutual exclusion Lock with the same basic behavior and semantics as `synchronized` with extended capabilities
- ReadWriteLock The ReadWriteLock interface similarly defines locks that may be shared among readers but are exclusive to writers

### Concurrent Collections

- **BlockingQueue** - defines a first-in-first-out data structure that blocks or times out when you attempt to add to a full queue, or retrieve from an empty queue.
- **BlockingQueue** - defines a first-in-first-out data structure that blocks or times out when you attempt to add to a full queue, or retrieve from an empty queue.
- **ConcurrentNavigableMap** is a subinterface of ConcurrentMap that supports approximate matches. The standard general-purpose implementation of ConcurrentNavigableMap is ConcurrentSkipListMap, which is a concurrent analog of TreeMap.[4]

## Reference

- [1] Java 8 Concurrency Tutorial: Synchronization and Locks; <https://winterbe.com/posts/2015/04/30/java8-concurrency-tutorial-synchronized-locks-examples/>
- [2] Intrinsic Locks and Synchronization' <https://docs.oracle.com/javase/tutorial/essential/concurrency/locksync.html>
- [3] Handling Java Memory Consistency with happens-before relationship; <https://medium.com/@kasunpdh/handling-java-memory-consistency-with-happens-before-relationship-95ddc837ab13#:~:text=Java%20defines%20a%20happens%2Dbefore,and%20ordered%20before%20the%20second.>
- [4] Atomic Access; <https://docs.oracle.com/javase/tutorial/essential/concurrency/atomic.html>
