# Consistency and Consensus

The best way of building fault-tolerant systems is to find some general-purpose abstractions with useful guarantess, implement. them once and then let applications rely on those guarantees.

Consensus implemented once can be used for multiple different purposes. E.g. leader election.

distributed consistency models vs the hierarchy of transaction isolation levels:
- **transaction isolation** is primarily about avoiding race condtions due to concurrently executing transactions
- **distributed conseistency** is mostly about coordinating the state of. replicas in the face of delays and faults

## Eventual Consistency

Typically, the weakest consistency guarantee that most databases provide is *eventual consistency*. 
It means that the application will at som point in time converge to a consistency state by itself. 
It is not defined how much time it takes to converge to a consistent state, only that it will happen once and it will be without action from the operator.

benefit
- good performance - low latency and high throughput as there is not need to wait for the consistent state. 
- fault tolerant - database can progress with nodes being temporarily unavailable

disadvantage:
- difficult to work with for developers, consistency must be implemented on application level.
- error prone - developing consistent system is difficult


## Linearizability
Simply put a linearizabile system looks as if it was operating on a single copy of data with all operations being atomic.

Linearizability is a **recency** guarantee. As soon as the client sucessfully completes write all clients reading from the database must be able to see the value that was just written. Once a value was written, can can never change back to the previous value.

### Linearizability vs Serializability
Serializability is a isolation property of transactions where every transaction may read and write multiple objects. If multiple transactions are executed at the same time, they behave as if they were executed in serial order.

Linearizability is a recency guarantee on rads and writes of a register. It does not group operations together and does not prevent problems such as write skew.

Strict serializibility - is when a database combines of a linearizability and serializability guarantees.

Snapshot isolation is not serializable by design. To avoid lock contention between readers and writers, it makes reads from a consistent snapshot. The point of the consistent snapshot is that it does not include writes that are more recent than the snapshot and thus reads from snapshot are not linearizable.

### Use of Linearizability
**Locking and leader election** - a system using single leader replication uses a locking to ensure that there is only one leader. Once leader was selected, it must never come to previous value without additional write. If that would happen and linearizable guarantee was violated, there could be 2 different leaders selected and database would be in stat of split braine.

Typically coordination services like Apache ZooKeeper and etcd uses a consensus algorithms to implement fault tolernat linearizable operations.

Linearizable locking is can also be used independently for example in context of locking pages in distributed file system.

### Implementation of a Linearizable System
- **single copy of data with one writer** - the simple solution, however the system is unable to tolerate failures and is at risk of data loss.
- **single-leader replication** - potentially linearizable - a single leader replicates data to followers and return success for write only if is replicated to all followers.
- consensus algorithm - multiple nodes must agree on the value
- multi-leader replication - **not** linearizable - writes are concurrently processed on multiple nodes and asynchronousely replicatied to the rest of the nodes.
- leaderless replication - probably not linearizable

### The Cost of Linearizability
Linearizable distributed system availability is fragile to network partition. Network interuption causes the application to become unavailable in datacentres that cannot contact the leader.

The response time of read and write requests is at least proportaional to the uncertainty of delays in the network. Linearizable writes and reads are inevitably going to have a high response time.

## Ordering and Causality
Ordering is a recuring requirement for many guarantees - e.g. writes must be processed in order in single leader replication, concurrent writes must look as if they were in serial order for serializability, and others.

The reason why ordering is so important is because it preserves causality. Causality imposes ordering on events. *Cause comes before effect:* A message is sent before that message is received.

### Causal order and total order
A total order allows any 2 elements to be comared. It is always possible to say which one is greater and which one is smaller, which one is ordered befor the other. 

**Linearizability** - total order of operations, every operation is atomic.

**Causality** - two opeartions are the concurrent if neither happened before the other.  Operations are incomparable if they are concurrent. Causality defines a partial order. Some opeartions are ordered with respect to each other but some are incomparable.

According to our definition, there are no concurrent writes in linearizable system. There is a single timeline on which are all operations ordered. 

Linearizability implies causality, but causality does not provide total order.

Casual consistency is the strongest possible consistency model that does not slow down ue to network delays and remain available in the face of network failures.

**Partial order** - concurrent operations might be processed in any order, but if one happened before the other, they must be processed in that order on every replica. If a node had already seen the value X, when it issued the write Y, then X and Y may be casually related.

Casual consistency must track causal dependencies across the entire database. 

#### Sequence number or timestamp
**Sequence number**, or **timestamp** can be appended to every event. Timestamp does not need to be only wallclock timestamp but also can be a logical clock. Logical clock can be defined by an algorithm generating a sequence of numbers to uniquelly identify operations. Typically, it is a counter incremented for every operation.

Sequence numbers provide a total order. Sequence of two events can be compared and determined which one is greater to the other.

Using sequence numbers, or timestamp (logical and walltime) are a good way of providing total order for a single leader database. In multileader database, approach of each leader defining the sequence is not consistent with causality because:
- each node processes different number of event in a minutes
- physical wallclock can be skewed

**Lamport timestamps**
Lamport timestamps provide total ordering using logical clocks in multi-leader system (not by using physical clock).

State:
- Each node has a unique identifier
- Each node keeps a counter of the number of operations it has processed
- Lamort timestamp is a pair - (counter, node ID)

Algorithm:
- Every node and every client keeps track of the maximum counter value it has seen so far and includes that maximum on every request
- When a node receives a request or response with a maximum counter value grater than its own counter value, it immediatelly increases its own counter to that maximum

Lamport timestamps are able to provide total order that is causaul. It is possible to order all events with each other. This however does not help with many problems in distributed systems.
This is because it is not possible to tell whether two evetnts are concurrent, or causaly dependent. This causes that lamport timestamps are not sufficient to solve some problems in distributed systems. E.g. checking a uniqueness constrain.

### Total Order Broadcast
A [broadcast](https://en.wikipedia.org/wiki/Broadcasting_(networking) "Broadcasting (networking)") where all correct processes in a system of multiple processes receive the same set of messages in the same order. It can be used for example in failover algorithm to select a new leader.

It requires 2 safety properties to be satisfied:
- reliavle delivery
- totally ordereded delivery- messages delivered to every node in the sam order

Total order (also atomic broadcast) is what is required for a database replication. It is also useful for implementing a fencing tokens used for a lock.

Total order has different guarantees from linearizability. Total broadcas is asynchronousm there is no guarantee about when a message will be delivered.
Linearizable storage can be built on top of the total broadcat

## 2PC - Two phase commit
It is an algorithm for achieving atomic transaction commit across multiple nodes. It ensures that either all nodes coomit or all nodes abort.

**Algorithm**
transaction begins with the application reading and writing data on multi-ple nodes as normal.

Nodes are calle participants.

When transaction is readay to commit, the coordinator begins phase 1.

In phase 1 - the coordinator sends a *prepare* request to each of the nodes, asking them whether they are able to commit. Coordinator tracks reposnses.
 - If all participants reply *yes* indicating they are ready to commit, then the coordinator sends out a commit request in phase 2.
 - If any of the participants replies *no* the coordinator an sends abort request to all nodes in phase 2

After a node replied yes to coordinator and signalled that is ready to commit, there is no way of return. A node can not abort the commit and has to commit the transaction if it will receives commit command from cooridnator in phase 2.

It does not matter whether the node fails or not. If it failed it will have to process the commit after it wakes up.

## Fault-Tolerant Consensus
In false tolerant consensus, one or more nodes can propose a value and the consensus algorithm decides on one of those values.

It must satisfy following properties:
- **uniform agreement** - no two noodes decide differently
- **integrity** - no node decides twice
- **validity** - if a node decides value v then v was proposed by soomoe node
- **termination** - every node that does not crash eventually decides some value

The uniform agreement and the integrity define the core idea of consensus:
*If everyone decides on the same outhcome and once you have decided, you cannoon change your mind*

The algorithm assumes that if a node crashes it will be gone forever and will never come back. 2PC does not satisgy termination property because it expects to wait for the failed node to come back.

The best known algorithms are Viewstamped Replication
- VSR
- Paxos
- Raft
- Zab

These algorithms have many similarities. They decide a sequence of values which makes them a total order broadcast algorithm.
Total broadcast requires messages to be delivered exactly once in the same order to all nodes. Total broadcast can be understood as repeated rounds of consensus. It is because of its properties:
- agreement - all nodes decide to deliver the same message in the same oreder
- integrity - messages are not dupplicated
- validity - messages are not corrupted or fabricated from the thin air
- termination - messages are not lost

### Epoch Numbers and quorums
Typically, protocols use internally a leader, but they dont guarantee the leader to be unique. They guarantee that the leader is unique per each epoch defined by an epoch number.

Every time the current leader is thought to be dead, a vote is started among the nodes to elect a new leader.

Election is given an incremented epoch number - thus epoch numbers are totally ordered and monotonically increasing.

If there is a conflict of two leaders, the leader with a higher epoch number wins.

Before a leader can decide on anything, it must first verify that there is not othere leader with a higher epoch number.

Every decision that a leader want to make, it must send the proposed value to the other nodes and wait for a quorum of nodes to respond in fabour of the proposal.

A node votes in favor of a proposal only if it is not aware of any other leader with a higher epoch.

Thus there are two rounds to:
1. choose a leader
2. vote on leaders proposal

The insight is that the quorum in the 2 votes must overlap.

The main difference to 2PC is that in consensus the leader is elected and in 2PC it is not.

The main benefits of the consensus are:
- they bring concrete safety properties
- they remain fault tolerant
- they provide total order
	- thus can also implement linearizable atomic operations

Limitations:
- they require strict majority to operate
- relying on timeouts can falsely cause that a healthy node is mark as unhealthy due to network delay or partitioning - a system can spend more time electing a leader than useful work

## Membership and Coordination Service
Zookeeper is a popular database providing a API that allows to write and read a key. It is used as part of other systems and is not meant as general use database.

Following systems are using a Zookeeper:
- HBase
- Hadoop YARN
- OpenStack Nova
- Kafka in the past - now it is using a kafka for this purpose

Zookeeper and etcd are used to hold a small amounts of data that can fit entirely in memory. Zookeeper is modeled after Google's Chubby lock service and is extended to fit following usecases:
- linearizable atomic operations:
	- e.g. lock with lease with an expiration date
- total ordering operations:
	- a fencing token, some number that is monotonically increasing each time when lock is aquired
- failure detection
	- clients maintain a long-lived session on ZooKeeper servers, and the client  and server periodically exchange heartbeats to check whether the other node is still alive.
- change notifications

Zookeeper is not intended for a runtime application storage, however it is very useful for number of tasks that require fault tolerant node synchronization.
