# Transasctions
Data systems can go wrong in many ways such as :
- software, or hardware can fail
- network partitioning can interrupt network
- several clients write at the same time
- client might read data without making sense when reading partially written data
- bugs caused by race conditions between clients

Transasction is aiming to provide an abstraction layer that addresses these issues so the application does not have to.

## ACID
**Atomic**
If a transaction was aborted, the application can be sure that it didn't change anything and it can be safely retried.

**Consistency**
Some invariants will always be true - e.g. column uniquness. This was added only for sake of having the acronym work.

**Isolation**
Concurently executed transactions are isolated from each other.

**Durability**
Any written successfully commited data will not be forgotten even when the software, or hardware fails.

## Weak Isolation Levels
Serializable isolation means that the database guarantees that transactions have the same effect as if they ran serially. It would prevent all concurency issues, but for significant performance cost.
That is why typicall databases implement weaker isolation levels

### Read Committed Isolation
Most basic level of transaction isolation. It makes 2 guarantees:
- *no dirty reads* - Reader only sees data that has been commited
- *no dirty writes* - Only data that have been commited can be overwriten by another transaction

It is a very popular isolation level default by PostgresSQL, SQL Server and MemSQL.

**Prevent Dirty Writes**
Most commonly dirty writes are prevented by using *row-level locks*. Transaction holds a lock for every updated row. It holds the lock until is commited. If another transaction wants to change this value, it must wait until lock hold by another writer is released.

**Prevent Dirty Reads**
Many transactions can read the same data in parallel. Hence, it is not necessary for a reader to block other readers. It is however necessary for readers to be blocking writers. Addind a lock that blocks writers but not readers would solve this problem, but it is not practical.
If reader would block writers, it would mean that any long running queries would block writers and cause poor performance.

Therefore the solution is in remembering both the old commited value and the new value that set by the transaction that currently hold the write lock.

While transaction is ongoing, nay other transaction that read the object is given old value.

Avoiding dirty reads and writes ensures that only commited values are visible to the reader or the writer. This seems sufficient, but also it allows for race conditions. Thay are following:

### Read Skew
Read skew, or non repeatable read happen when two elements are updated under a constrain e.g. Alice moves $50 From Account A to Account B. Once the transaction is commited, this change is applied. There is however no guarantee that the change was applied at the same time. For a period of time a reader might see missing $50. If reader would repeat the read it would most likely see bot Account A and Account B updated - hence, we call this race condition also a non repeatable read.

Very often read skew can be tolerated, but not in following cases:
- backups
- analytic reports

### Snapshot Isolation and MVCC

Snapshot Isolation is the most common solution to prevent read skew and ensure repeatable read.

Snapshot Isolation means that each transaction reads from consistent snapshot of the database - that is the transaction sees all the data that was commited in the database at the start of the transaction. 

**Implementation**
Like read committed isolation, snapshot isolation is using write locks to prevent dirty writes - transactions making write can block another transaction making write. Readers however do not need lock.

*Core principle of snapshot isolation is that readers never block writers and writers never block readers*

Database must keep several copies of a commited object because several in-progress transactions might need to see different state of the database at time. It is also called Multi Version Concurrency Control (MVCC) because database needs to keep track of multiple object versions at the same time.

## Race Conditions

### Lost Updates
Happens when we read a value apply from database modifies it and writes  the updated value back  - *read-modift-write* cycle.
If two writers do this concurently, update from one writer might be lost. 

**Atomic Write Operations**
Some databases support atomic write operations, which apply the value change without the need to read the actual value.

e.g.
`UPDATE counters SET value + 1 where key='my_key'`

Atomic operations are usually implemeneted by taking an exclusive lock on the object when it is read so that no other transaction can read it until the update has been applied.

**Explicit Locking**
Another option to prevent lst update is to explicitly lock by doing both write and read in transaction

**Compare-and-set**

In databases not providing transactions, we can see sometime a compare-and-set update. It means that only if the value has not changed, the object will be updated.

```
UPDATE pages SET content = 'new content'
  WHERE id = 1234 and content = 'old content'
```

This may not be safe! If database allows the `WHERE` statement to read from an old snapshot this may not prevent lost updates.

### Write Skew
Write Skew happens can be understanded as a generalization of a lost update problem. 
It happen when two transactions read the same objects and then update some of those objects.

Typically it can be resolved only by locking row of which read will be used for the update.

For example lets have a software on-call rota with at least 1 person on the rota. Let both Bob and Alice be on on-call rota.
At about the same time, they both decide to withdraw from the rota.

Because of MVCC they both read data in isolation. Bob and Alice see that there are 2 people on rota can reschedule. After they commit the change, no one is on-call and the constrain was violated.


## Serializability
Serializability guarantees that even though transactions may execute in parallel, the end result is the same as if they had executed at a time serially without concurrency.

In the past there were multiple different solution to this isolation guarantee. The most popular are:

**Actual Serial Execution**
Applying changes in serial order by a single thread executes one transaction at the time and provies a serializability. This is a simple idea but was adopted only since 2007. The main reasons for the shift are:
- cheap RAM
- OLTP transactions are usually short and inly make small number of reads and writes

Used in Redis, H-Store and Datomic.

**Two-Phase Locking (2PL)**
It was the only widely used algorithm for 30 years.

In 2PL several readers can read the object as long as no one is writing to it. As soon as anyone wants to write to an object, exclusive access is required:

- if A has a read and B wants to write to that object B must wait until A commits or abort before it can continue
- If A has written an object and B wants to read object B must wait until A commits or aborts before it can continue.

2PL breaks the mantra of isolation - readers dont block writers and writers dont block readers. This has an impact on database performance. It is also the key between a snapshot isolation and two-phase locking.

2PL provides serializability, it protects against all the race conditions we have discussed earlier. including lost updates and write skew.

## Serializable Snapshot Isolation (SSI)
