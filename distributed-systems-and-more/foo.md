# Replication
Replication means keeping a copy of the same data on multiple machines that are connected via network.

## Purposes
- high availability - system can tolerate a failure of one or more nodes
- latency - geographical colocation reduces clients read latency
- scalability - spreading reads and potentailly writes to replicas allows database to handle more volume

## Challenges
The concept of replication is simple, but the execution is complex and has many challenges. The difficulty in replication is in handling the change to replicated dataset.

Some of the challenges we need to deal with are:
- unavailable nodes
- network interuptions
- data inconsistency between nodes
- replication lag

These challenges require carefull desing of replication strategy.

## Replication Approaches
Each node storing a copy of database is called a *replica*. The challenge is to ensure that all data are stored on all replicas and that they are up to date. There are multiple approaches to solve this challenge. Based on the latency, scale and avalability requirements different solution is better or worse suited solution.

For example, handling a replicated database with bank transaction pays high attention to data consistency, then a shoppping cart in Amazon.

### Single Leader Replication
the replication algorithms works as following:
1. One node is called a leader. Leader node accepts all writes from clients. When it stores the writes to its own database it also replicates writes to replicas. The data are send to replicas by a replicayion log, or a change stream.
2. All writes are consumed and stored by the replicas in the same order as they were processed by the leader.
3. Read clients can connect to both the leader or the replica.

Ability to read from the replica node increases significantly the read scale of the database. The cost is higher latency as the leader can not confirm the write to client until the write is replicated.

This approach is popular and used in many databases such as PostgreSQL, MySQL, but also a disctributed message broakers such as Kafka, and highly available queues sucha asRabbitMQ.

#### Synchronous versus Asynchronous Replication
Synchronously waiting for processing the write on all replicas can be impractical for both latency and availability of the system. Even one unavailable replica can cause that database is not able to progress and accept writes.

Better trade off is to have a single replica to be synchronous while other keep asynchronous. This approach allows a replica to fail and at the same time the durability is maintained. In case that the synchronous follower becomes unavailable, one of the asynchronous followers become synchronous.

#### Write-ahead log shipping (WAL)
WAL is a replication technique used in PostgreSQL.

The log is an append-only sequence of bytes containing all writes to the database. We can use the exact same log to build a replica on another node.

Advantage of this replication is that it is simple as the leader and replicas can use WAL to build their internal datastructure. This is also a disadvantage as it is a very low level datastructure manipulating bytes and having and intimate knowledge of the underlying memory. This makes migration to new version of db engine more difficult as all nodes must run on the same version.

Another replication approaches are:
**statement based replication**
The simplest replication case, when the leader logs every write request it executes and sends the statement log to its followers. This approach breaks quickly because of nondeterministic writes - db internal functions e.g. time now(), triggers, or autoincrement of the record.

Simple solution could be not allowing non deterministic writes, or leader can replace non deterministic functions with the actual value.

**logical (row-based) replication**
Replication and storage format is different. This is called a logical log, which is different from the physical log representing the data in memory.

This is useful for consuming this log by other 3 party applications for building a custom indexes and caches. This technique is called a *data capture*.


### Multi Leader Replication
Leader based replication has a major downside - it has only one leader and all writes must go trough it. Natural extention to this model is allowing multiple leaders to accept writes. Replication still happen in thesame way when writes are forwarded from leader to followers. This replication model is called multi-leader replication.

A common usecase for multi-leader replication is when having a multiple datacentres in different geo locations, this can have significant impact on both latency and availability.
With multi leader configuration, there can be a single leader in both datacenters. Within each datacenter, regular leader-follower replication is used. Between datacenters, each datacenter leader replicates its writes to other datacenters.

![[static/IMG_8103.jpg]]

**Advantages**
- performance - every write can be processed in the local datacenter and is replicated asynchronously to the other datacenters, the inter-datacenter delay is hidden from the users
- tolearance of datacenter outages
- tolerance of network problems - writes within datacenter can be processed even when the inter data center connection is interrupted. Typically the connection between DCs is over internet and less stable then the one within the DC

**Disadvantages**
- conflicts caused by concurrent updates
- multi leader configuration is commonly retrofitted to databases without being a first class citizen. It can have many pitfalls:
	- autoincrement keys
	- triggers
	- integrity constains

Multi leader replication is considerered dangerous and should be avoided.

### Conflict Resolution Stategies:
**Each Write has unique ID**
The write with the highest ID is the winner and other writes will be ignored. Timestamp can also be used as and ID, in this case the stategy is called Last Write Wins (LWW). *This stategy will lead to data loss*.

**Each Replica has unique ID**
Write from a replica with the highest ID wins and other writes will be ignored. *This stategy also implies data loss*.

**Values are merged together**
Written values are merged together by e.g. concatenation e.g. "B/C"

**Conflict managed by data structure**
Conflict is recorded by a data structure and describing the conflict. This data structure can either just capture the conflict or merge it to a result based on predefined rules.

**Custom logic**
Also a custom logic can be used to resolve a conflict resolved by an application code. This could happen on:
- write - conflict is reported on write. This might not be possible with async replication.
- read - all versions of the write are returned to application. Application can handle the conflict

## Leaderless Replication
Leaderless replication became popular after Amazon used it for Dynamo DB. Cassandra, Voldemort and Riak followed the example.

Some databases diged the leader follower model alltogether and they directly write the data to all clients.
When a node is offline and misses a write (fails to accept the write), the write is stored in other nodes if e.g. 2 out of 3 nodes are available and the database continous to progress. When the offline node recovers and start accepting reads, it can have lag and might be providing a stale data. To prevent serving a stale results, client does not request dat from a single, but from multiple nodes in parallel.

If we know that every succesfull write is guaranteed to be present on at least 2 out of 3 replicas, that means that at most one replica can be stale.

**Consistency Quorum**
More generally, if there are n replicas, every write must be confirmed by w nodes to be successful and we must read at least r nodes for each read. As long as a `w + r > n` - Reads and writes that obey these *r* and *w* values are called *quorum reads and writes*.

**Limits to Consistency Quorum**
Quorums are not necessarily majority. it only means that a set of nodes for write and read are overlapping in at least one node. There are following edge cases:
- If sloppy quorum is used
- 2 writes happen concurrently
- write happens concurrently with the read
- write succeeded on some but failed on other replicas
- others

Typically databases leaderless replication are more tolerant towards eventual consistency. In this case it is important to practicly define what eventual consistency means and closely follow the nodes lag.

**Read Repair**
When client reads a value from multiple replicas, it can detect that some node had stale, or missing value. If that happens a client can replace stale value with the latest one.

**Any-Entryopy process**
Background process that constantly looks for differences in the dat abetween replicas and copie any missing data.

**Sloppy Quorum**
It is common to make trade-offs between availability and consistency depending on the requirement. We ask a question: 
Is it better to return errors to all requests for which we cannot reach a quorng of w or r nodes?
In a *Slopy Quorum* system accepts writes anyway and write them to some nodes that are reachable but are not amonth the *n* nodes on which the value is usually present?

Once the network interruption is fixed, any writes that one node temporarily accepted on behalf of the other node are sent to the appropriate *home node*. - This strategy is called *Hinted Handoff*

## Replication Lag Consistency Models

### Read after Write Consistency
Guarantees that if the user reloads the page, they will always see updates they submitted themeselves. It makes no guarantees about other users.

In case that client writes to leader and reads from async replica, it can happen that the write has not yet been replicated. This leads to unhappy user. There are few solutions to address this:

- read user modified data from the leader - impractical if majority of data is produced by the user
- track the time of the last user update and do all reads from the leader for given user for 1 minute after write
- client remembers the last write timestamp and makes sure that given replica is up to date with that timestamp

### Monotonic Reads
When a client reads a single value from database, the monotonic read guarantees that every successive read operation will return the same or more recent value.

### Consisten Prefix Reads
Guarantee that if a sequence of writes happens in a certain order, then anyone rading those writes will see them appear in the same order.

This guarantee can be in danger in case when a different database partitions operate independently so there is no global ordering of writes.

One solution can be that casually dependent writes are always written to the same partition.
