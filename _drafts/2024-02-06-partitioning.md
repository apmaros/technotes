---
layout: post
title:  Partitioning
date:   2024-02-05 19:35:41 -0500
categories: partitioning
tags: consistency consensus
---

Partitioning is a technique used for scaling databases horizontally. 

It is typically used when using a single, or a node with replicas is not sufficient. When partitioning, each record belongs to a single partition.

A partition can be understood as a single database on its own. A database is split into multiple partitions eventually.  Each partition can be run on a different host, hence the load is distributed across different machines. Each machine can independently execute queries.
It is still important to consider replication as partitions are typically replicated to provide failure tolerance guarantees.

Operational data are always changing and this causes partitions might no longer be evenly distributed. This can happen for example on social media networks when some popular celebrity has millions of followers. In this case, when the partitions are off-balance, the process of rebalancing can correct this and restore even partition distribution.

The next section will describe how to decide to what partition a new record should be allocated as well as how can we rebalance partitions.

**The primary goal of partitioning is to spread the data and the query load eventually across nodes.** 

**skewed partitioning**
the situation when partitioning is unfair and some partitions have more data or load than the others.

**hot spot**
result of skewed partitioning, when a partition is under a higher load than the others.

**key-value** 
Let's have a record containing data with a key and be queriable by the key. In key-value partitioning, records are sorted and assigned to partitions based on the order of the key.

**key-range**
Assign a continuous range of keys to each partition. Each partition has a minimum and maximum key assigned. Based on this we know where to look for the record. The key range is particularly useful when range queries are required. It is important to note that ranges of keys do not need to be evenly spaced.
This is a popular partitioning strategy used in HBase, RethinkDB, and MongoDB.
The downside of this strategy is that certain access patterns can lead to hot spots. For example, if the key is a timestamp and we are writing time-sensitive sensor data, it would lead to all writes landing at the same partition. This can be mitigated by creating a compound key and for example, appending a sensor name to the timestamp.

**partitioning by a hash of key**
To prevent skews and hot spots, many distributed data stores rely on a hash function to determine the partition for a given key.

A good hash function takes skewed data and makes it uniformly distributed. An example of a popular hashing function is MD5 used in Cassandra and MongoDB. A hash function should be language-independent as different languages produce different values of their hash function.

Each partition then will be assigned a *range of hashes* instead of a range of keys and every key whose hash falls within a partition's range will be stored in that partition.

This however will make the search for a key range more difficult. Some databases solve this challenge by sending range queries to all nodes (MongoDB), others do not support it (Couchbase, Voldemort).
Cassandra has a creative approach with a concept of compound keys. The first key is hashed to decide the partition, however, the rest of the keys are used as a concatenated index for sorting the data.

Partitioning by Key Range

Partitioning by Hash Key

Skewed Workloads and Relieving Hot Spots

Secondary Indexes

- Secondary Indexes by Document
- Secondary Indexes by Term

Rebalancing Partitions

- Don't hash `mod N`
- Fixed number of partitions
- Dynamic partitioning
