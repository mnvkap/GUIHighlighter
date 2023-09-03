import sys
import xml.etree.ElementTree as ET 

def find_leaf_nodes(node):
    if len(node) == 0: # Check if node is a leaf node 
        return [node]  # If so return 
    
    leaf_nodes = []
    for child in node:
        leaf_nodes.extend(find_leaf_nodes(child))

    return leaf_nodes

def main(): 
    tree = ET.parse(sys.argv[1]) # Create ET object 
    root = tree.getroot() # Store root of tree
    leaf_nodes = find_leaf_nodes(root) # Find all leaf nodes 
    
    print(leaf_nodes)

if __name__ == "__main__":
    main()
