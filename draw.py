import sys
from PIL import Image, ImageDraw

def draw_highlight(image, x1, y1, x2, y2):
    draw = ImageDraw.Draw(image) # Prepare drawing context 
    yellow = (255, 255, 0) # Define yellow in RGB
    draw.rectangle([x1, y1, x2, y2], outline = yellow) # Draw rectangle 

