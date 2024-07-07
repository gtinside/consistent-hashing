### Consistent Hashing

Consistent hashing is used in distributed systems to efficiently distribute data among multiple nodes while minimizing reorganization when nodes are added or removed.It maps both data and nodes onto a common hash space (typically a circle), where each node is responsible for the data that falls within its range on the circle.

#### Step-by-Step Implementation
1. Create a Hash function: This library use md5 from hashlib. Get the string value (hex digest) and convert it into a string
2. Node representation 
3. Virtual Nodes (Coming soon!!)
4. Hash Ring construction
5. Mapping data to nodes
