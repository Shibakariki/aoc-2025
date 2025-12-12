import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import math
import numpy as np

def main():
    # input_lines = open_file("example-1.txt")
    input_lines = open_file('code-1.txt')
    
    red_tiles_coords = []
    for line in input_lines:
        parts = line.strip().split(',')
        x, y = map(int, parts)
        red_tiles_coords.append((x, y))
        
    max_area = 0
    for coord in red_tiles_coords:
        for coord2 in red_tiles_coords:
            if coord != coord2:
                area = (abs(coord[0] - coord2[0]) + 1) * (abs(coord[1] - coord2[1]) + 1)
                if area > max_area:
                    max_area = area
                

    print("Max area between red tiles:", max_area)


if __name__ == "__main__":
    main()