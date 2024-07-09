### Consistent Hashing

Consistent hashing is used in distributed systems to efficiently distribute data among multiple nodes while minimizing reorganization when nodes are added or removed.It maps both data and nodes onto a common hash space (typically a circle), where each node is responsible for the data that falls within its range on the circle.

#### Features
1. This library use md5 from hashlib. Get the string value (hex digest) and convert it into a string
2. Two maps are maintained by this library
    a. Map to identify the hash of nodes adding to the ring
    b. Map to identify which keys are part of what nodes

#### Usage
```
consistent_hashing_impl = ConsistentHashingImpl()
consistent_hashing_impl.add_node("node1")
consistent_hashing_impl.add_node("node2")
consistent_hashing_impl.add_node("node3")

print("Key will be stored in node :%s" % consistent_hashing_impl.get_node_for_data("python"))
print("Key will be stored in node :%s" % consistent_hashing_impl.get_node_for_data("Java"))
```
The above code will generate the following output
```
2024-07-09 00:01:34,035: Generating hash for key: node1
2024-07-09 00:01:34,035: Generating hash for key: node2
2024-07-09 00:01:34,035: Generating hash for key: node3
2024-07-09 00:01:34,035: Generating hash for key: python
Key will be stored in node :node2
2024-07-09 00:01:34,035: Generating hash for key: Java
Key will be stored in node :node1
```

#### Installation 
```pip install py-consistent-hash==1.0.0```