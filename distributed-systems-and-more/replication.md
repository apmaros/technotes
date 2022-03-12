# Replication
Replication means keeping a copy of the same data on multiple machines that are connected via a network.
## Purposes
- high availability - the system can tolerate a failure of one or more nodes
- latency - geographical colocation reduces the client's read latency
- scalability - spreading reads and potentially writing to replicas allows a database to handle more volume
## Challenges
The concept of replication is simple, but the execution is complex and has many challenges. The difficulty in replication is in handling the change to a replicated dataset.

Some of the challenges we need to deal with are:
- unavailable nodes
- network interruptions
- data inconsistency between nodes
- replication lag

These challenges require careful design of replication strategy.

## Replication Approaches
Each node storing a copy of a database is called a *replica*. The challenge is to ensure that all data are stored on all replicas and that they are up to date. There are multiple approaches to solve this challenge. Based on the latency, scale, and availability requirements different solution is a better or worse suited solution.

For example, handling a replicated database with bank transactions pays high attention to data consistency, than a shopping cart in Amazon.

### Single Leader Replication
the replication algorithms work as follows:
1. One node is called a leader. Leader node accepts all writes from clients. When it stores the writes to its own database it also replicates writes to replicas. The data are sent to replicas by a replication log or a change stream.
2. All writes are consumed and stored by the replicas in the same order as they were processed by the leader.
3. Read clients can connect to both the leader and the replica.

The ability to read from the replica node increases significantly the reading scale of the database. The cost is higher latency as the leader can not confirm the write to a client until the write is replicated.

This approach is popular and used in many databases such as PostgreSQL, MySQL, but also distributed message brokers such as Kafka, and highly available queues such as RabbitMQ.

#### Synchronous versus Asynchronous Replication
Synchronously waiting for processing the write on all replicas can be impractical for both latency and availability of the system. Even one unavailable replica can cause that database is not able to progress and accept writes.

A better trade-off is to have a single replica be synchronous while others keep asynchronous. This approach allows a replica to fail and at the same time, the durability is maintained. In case the synchronous follower becomes unavailable, one of the asynchronous followers becomes synchronous.

#### Write-Ahead-Log Replication (WAL)
WAL is a replication technique used in PostgreSQL.

The log is an append-only sequence of bytes containing all writes to the database. We can use the exact same log to build a replica on another node.

The advantage of this replication is that it is simple as the leader and replicas can use WAL to build their internal data structure. This is also a disadvantage as it is a very low-level data structure manipulating bytes and having an intimate knowledge of the underlying memory. This makes migration to a new version of the DB engine more difficult as all nodes must run on the same version.

Other replication approaches are:
**statement based replication**
In the simplest replication case, when the leader logs every writes to a request it executes and sends the statement log to its followers. This approach breaks quickly because of nondeterministic writes - DB internal functions e.g. time now(), triggers, or autoincrement of the record.

A simple solution could be not allowing non-deterministic writes, or a leader can replace non-deterministic functions with the actual value.

**logical (row-based) replication**
A replication and storage format is different. This is called a logical log, which is different from the physical log representing the data in memory.

This is useful for consuming this log by other 3 party applications for building custom indexes and caches. This technique is called a *data capture*.


### Multi Leader Replication
Leader-based replication has a major downside - it has only one leader and all writers must go through it. A natural extension to this model is allowing multiple leaders to accept writes. Replication still happens in the same way when writes are forwarded from leader to followers. This replication model is called multi-leader replication.

A common use-case for multi-leader replication is when having multiple data centers in different geo locations, this can have a significant impact on both latency and availability.
With multileader configuration, there can be a single leader in both datacenters. Within each data center, regular leader-follower replication is used. Between datacenters, each datacenter leader replicates its writes to other datacenters.

![[static/IMG_8103.jpg]]

**Advantages**
- performance - every write can be processed in the local datacenter and is replicated asynchronously to the other datacenters, the inter-datacenter delay is hidden from the users
- tolerance of data center outages
- tolerance of network problems - writes within a datacenter can be processed even when the inter-data center connection is interrupted. Typically the connection between DCs is over the internet and less stable than the one within the DC

**Disadvantages**
- conflicts caused by concurrent updates
- multileader configuration is commonly retrofitted to databases without being a first-class citizen. It can have many pitfalls:
	- autoincrement keys
	- triggers
	- integrity contains

Multi leader replication is considered dangerous and should be avoided.

### Conflict Resolution Strategies:
**1. Each Write has a unique ID**
The writer with the highest ID is the winner and other writers will be ignored. Timestamp can also be used as an ID, in this case, the strategy is called Last Write Wins (LWW). *This strategy will lead to data loss*.

**2. Each Replica has a unique ID**
Write from a replica with the highest ID wins and other writes will be ignored. *This strategy also implies data loss*.

**3. Values are merged together**
Written values are merged together by e.g. concatenation e.g. "B/C"

**4. Conflict managed by data structure**
Conflict is recorded by a data structure and describes the conflict. This data structure can either just capture the conflict or merge it to a result based on predefined rules.

**5. Custom logic**
A custom logic can be used to resolve a conflict resolved by an application code. This could happen on:
- write - conflict is reported on write. This might not be possible with async replication.
- read - all versions of the write are returned to the application. The application can handle the conflict

## Leaderless Replication
***Leaderless replication became popular after Amazon used it for Dynamo DB. Cassandra, Voldemort, and Riak followed the example.***

Some databases dodged the leader-follower model altogether and they directly write the data to all clients.
When a node is offline and misses a write (fails to accept the write), the write is stored in other nodes if some nodes (e.g. 2 out of 3) are available and the database continues to progress. When the offline node recovers and starts accepting reads, it can have lag and might be providing stale data. To prevent serving stale results, the client does not request data from a single, but from multiple nodes in parallel.

If we know that every successful writer is guaranteed to be present on at least 2 out of 3 replicas, that means that at most one replica can be stale.

**Consistency Quorum**
More generally, if there are n replicas, every write must be confirmed by w nodes to be successful, and we must read at least r nodes for each read. As long as a `w + r > n` - Reads and writes that obey these *r* and *w* values are called *quorum reads and writes*.

**Limits to Consistency Quorum**
Quorums are not necessarily a majority. it only means that a set of nodes for writing and reading are overlapping in at least one node. There are the following edge cases:
- If a sloppy quorum is used
- 2 writes happen concurrently
- write happens concurrently with the read
- write succeeded on some but failed on other replicas
- others

Typically, database leaderless replication are more tolerant towards eventual consistency. In this case, it is important to practically define what eventual consistency means and closely follow the nodes' lag.

**Read Repair**
When a client reads a value from multiple replicas, it can detect that some nodes had stale, or missing values. If that happens, a client can replace the stale value with the latest one.

**Any-Entropy process**
A background process that constantly looks for differences in the data between replicas and copies any missing data.

**Sloppy Quorum**
It is common to make trade-offs between availability and consistency depending on the requirement. We ask a question: 
Is it better to return errors to all requests for which we cannot reach a quorum of w or r nodes?
In a *Sloppy Quorum* system accepts writes anyway and writes them to some nodes that are reachable but are not a month the *n* nodes on which the value is usually present?

Once the network interruption is fixed and writes that one node temporarily accepted on behalf of the other node is sent to the appropriate *home node*. - This strategy is called *Hinted Handoff*

## Replication Lag Consistency Models

### Read after Write Consistency
Guarantees that if the user reloads the page, they will always see updates they submitted themselves. It makes no guarantees about other users.

In case the client writes to a leader and reads from an async replica, it can happen that the writer has not yet been replicated. This leads to an unhappy user. There are a few solutions to address this:

- read user modified data from the leader - impractical if a majority of data is produced by the user
- track the time of the last user update and do all reads from the leader for a given user for 1 minute after write
- client remembers the last write timestamp and makes sure that the given replica is up to date with that timestamp

### Monotonic Reads
When a client reads a single value from the database, the monotonic read guarantees that every successive read operation will return the same or more recent value.

### Consistent Prefix Reads
Guarantee that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

This guarantee can be in danger in a case when different database partitions operate independently so there is no global ordering of writes.

One solution can be that casually dependent writes are always written to the same partition.
