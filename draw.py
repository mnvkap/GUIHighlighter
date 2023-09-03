import sys
from PIL import Image, ImageDraw

image = Image.open(sys.argv[1]) # Load our image
draw = ImageDraw.Draw(image) # Prepare drawing context 
yellow = (255, 255, 0) # Define yellow in RGB

x1, y1 = 100, 100 # Top left corner coordinates
x2, y2 = 200, 200 # Bottom right corner coordinates

draw.rectangle([x1, y1, x2, y2], outline = yellow) # Draw rectangle 
image.save("output_image.png") 
