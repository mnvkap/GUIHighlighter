import sys
import xml.etree.ElementTree as ET 

def find_leaf_nodes(node):
    if len(node) == 0: # Check if node is a leaf node 
        return [node]  # If so return 
    
    leaf_nodes = []
    for child in node:
        leaf_nodes.extend(find_leaf_nodes(child))

    return leaf_nodes

