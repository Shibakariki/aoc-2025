import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file

from math import floor

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    number_of_zeros = 0
    init_position = 50
    for line in input_lines:
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (init_position - distance) % 100
            turns = ((position - init_position) + distance) / 100
            if init_position == 0:
                turns -= 1
        elif direction == 'R':
            position = (init_position + distance) % 100
            turns = (init_position + distance) / 100
            if position == 0:
                turns -= 1
        
        # print("pos", init_position, "->", position, "over", "+" if direction == 'R' else "-", distance, "turns:", turns)
               
        if position == 0:
            number_of_zeros += 1
        if turns > 0:
            number_of_zeros += floor(turns)
        init_position = position
    print("Number of times position is zero:", number_of_zeros)
    
if __name__ == "__main__":
    main()