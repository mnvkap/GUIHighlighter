import sys
import re
from PIL import Image
import xml.etree.ElementTree as ET 
from find_leafs import find_leaf_nodes
from draw import draw_highlight

def main(): 
    image = Image.open(sys.argv[2]) # Load our image 
    tree = ET.parse(sys.argv[1]) # Create ET object 
    root = tree.getroot() # Store root of tree
    leaf_nodes = find_leaf_nodes(root) # Find all leaf nodes 

    for node in leaf_nodes:
        bounds = node.get("bounds") # Get the value from the attribute bounds
        coordinates = re.findall("\d+", bounds) # Utilize regex to make a list of the coordinates
        
        # Set coordinates using bounds
        x1, y1 = int( coordinates[0] ), int( coordinates[1] ) 
        x2, y2 = int( coordinates[2] ), int( coordinates[3] ) 

        # Draw on image
        draw_highlight(image, x1, y1, x2, y2)

    image.save("output_image.png") 
    image.show() 

if __name__ == "__main__":
    main()
