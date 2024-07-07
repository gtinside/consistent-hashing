import sys
import hashlib
import logging

class ConsistentHashingImpl:
    def __init__(self, max_hash:int=2**10) -> None:
        self.max = max_hash
        self.node_hash_map = dict()
    
    def hash(self, key:str):
        """ Function to generate an md5 hash and modulo it with 2^10, the max hash on the ring
        
        Parameters:
        key (str): Key that needs to be hashed

        Returns:
        str: Hex digest
        
        """
        print("Generating hash for key: %s" % key)
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), base=16) % self.max
    
    def addNode(self, node_id:str):
        """ Function to add a node to the ring
        
        Parameters:
        node_id (str): Either node name or ip

        Returns:
        None
        
        """
        if node_id not in self.node_hash_map:
            self.node_hash_map[self.hash(node_id)] = node_id
        else:
            raise ValueError("Node: %s is already present in the ring" % node_id)
        


print(ConsistentHashingImpl().hash("gaurav"))

