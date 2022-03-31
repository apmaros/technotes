
# Cassandra
<!-- give 1 sentence overview -->
Apache Cassandra is an open source', distributed, NoSQL database. It presents a partitioned wide column storage model with eventually consistent semantics.

<!-- More detail -->
Systems like Cassandra are designed for these challenges and seek the following design objectives:

- Full multi-master database replication
- Global availability at low latency
- Scaling out on commodity hardware
- Linear throughput increase with each additional processor
- Online load balancing and cluster growth
- Partitioned key-oriented queries
- Flexible schema

Cassandra explicitly chooses not to implement operations that require cross partition coordination. The main reasons for the limitation are:
- low latency requirement - cross partition coordination is slow
- hard to provide highly available global semantics


## Key Features and Concepts
- **Keyspace** - Defines how a dataset is replicated, per datacenter
- **Table** - Defines the typed schema for a collection of partitions. Tables contain partitions that contain rows.
- **Partition** - partition is a node where table rows are stored. Partition is selected based on the part of the primary key. The partition part of the key is mandatory for each record and each *performant* query.
- **Row** - A collection of columns uniquely identified by partition key and optionally additional cluster keys.
- **Column** - A single datum with a type that belongs to a row.

### CQL
Cassandra Query Language [CQL](https://github.com/apache/cassandra/blob/cassandra-4.0.3/doc/modules/cassandra/pages/architecture/cql/ddl.adoc) is an SQL-like language used to create and update database schema and access data

#### Features
- Single partition lightweight transactions with atomic compare and set semantics.
- User-defined types, functions, and aggregates.
- Collection types include sets, maps, and lists.
- Local secondary indices


## Performance
<!-- How many RPS are supported -->

## Guarantees

Different consistency levels can be set for both reads and writes. Each query can set a different consistency level.

- **High availability** - provided by a failure tolerant storage. Failure detection is implemented by a gossip protocol.
- **Durability** - guaranteed by replicas.
- **Eventual Consistency** - all updates will reach all replicas eventually. Divergent data versions might occasionally happen, but are temporary and eventually will converge to a consistent state.
- **Lightweight transactions with linearizable consistency** - the Paxos consensus protocol is used to implement lightweight transactions that can handle concurrent operations. This type of transaction is called CAS (Compare and Set). Replica data is compared, and any data found to be out of date is set to the most consistent value.



## Architecture
<!-- What components it consists of -->

# References
- https://github.com/apache/cassandra/blob/cassandra-4.0.3/doc/modules/cassandra/pages/architecture/overview.adoc