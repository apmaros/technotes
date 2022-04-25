# Back of Envelope Calculations

## Data Size Conversions

- 1000 bytes                   (1 thousand)     1 kilobyte
- 1000 000 bytes           (1 million)          1 megabyte
- 1000 000 000 bytes   (1 billion)           1 gigabyte
- 1000 000 000 000      (1 trillion)          1 terabyte

## Common Data Types

- Char (UTF-8) - 4bytes
- integer - 4bytes
- big integer - 8bytes

## Availability Levels

| Level    | per day      | per month    | per year     |
|----------|--------------|--------------|--------------|
| 99%      | 14.4 minutes | 7.2 hours    | 3.65 days    |
| 99.9%    | 1.44 minutes | 43.2 minutes | 8.76 hours   |
| 99.99%   | 8.64 seconds | 4.32 minutes | 4.32 minutes |

## Latency Comparison Numbers (~2012)

- L1 cache reference 0.5 ns
- Main memory reference 100 ns 20x L2 cache, 200x L1 cache
- Compress 1K bytes with Zippy 3,000 ns 3 us
- Send 1K bytes over 1 Gbps network 10,000 ns 10 us
- **Read 4K randomly from SSD 150,000 ns 150 us ~1GB/sec SSD**
- Read 1 MB sequentially from memory 250,000 ns 250 us
- **Round trip within same datacenter 500,000 ns 500 us**
- Read 1 MB sequentially from SSD* 1,000,000 ns 1,000 us 1 ms ~1GB/sec SSD, 4X memory
- Disk seek 10,000,000 ns 10,000 us 10 ms 20x datacenter roundtrip
- Read 1 MB sequentially from disk 20,000,000 ns 20,000 us 20 ms 80x memory, 20X SSD
- **Send packet CA->Netherlands->CA 150,000,000 ns 150,000 us 150 ms**

### Notes

- 1 ns = 10^-9 seconds
- 1 us = 10^-6 seconds = 1,000 ns
- 1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

## References

- 1.  <https://gist.github.com/jboner/2841832>
- 2. <https://sre.google/sre-book/availability-table>
- 3. <https://colin-scott.github.io/personal_website/research/interactive_latency.html>
- 4. <https://itsallbinary.com/system-design-back-of-envelop-calculations-for-storage-size-bandwidth-traffic-etc-estimates>
