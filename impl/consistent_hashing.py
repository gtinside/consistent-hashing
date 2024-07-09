import sys
import hashlib
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')


class ConsistentHashingImpl:
    def __init__(self, max_hash:int=2**10) -> None:
        self.max = max_hash
        self.node_hash_map = dict()
        self.key_node_map = dict()

    
    def hash(self, key:str):
        """ Function to generate an md5 hash and modulo it with 2^10, the max hash on the ring
        
        Parameters:
        key (str): Key that needs to be hashed

        Returns:
        str: Hex digest
        
        """
        logger.info("Generating hash for key: %s" % key)
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), base=16) % self.max
    
    def add_node(self, node_id:str):
        """ Function to add a node to the ring
        
        Parameters:
        node_id (str): Either node name or ip

        Returns:
        None
        
        """
        if node_id not in self.node_hash_map:
            self.node_hash_map[self.hash(node_id)] = node_id
            self.node_hash_map = dict(sorted(self.node_hash_map.items()))
        else:
            raise ValueError("Node: %s is already present in the ring" % node_id)
    
    def get_node_for_data(self, key:str):
        """ Function to look in the ring and find the node that will
        store the key
        
        Parameters:
        key (str): The key that needs to be stored

        Returns:
        str: The name of the node
        
        """
        left_hash = 0
        key_hash = self.hash(key)
        for right_hash, node in self.node_hash_map.items():
            if key_hash > left_hash and key_hash < right_hash:
                self.key_node_map[key] = node
                return self.key_node_map[key]
            left_hash = right_hash
        self.key_node_map[key] = self.node_hash_map[list(self.node_hash_map.keys())[-1]]
        return self.key_node_map[key]
    
    def get_key_node_map(self):
        """
        Function to return the map of which node holds what key

        Parameters:
        None

        Returns:
        dict: The key node map
        """
        return self.key_node_map
