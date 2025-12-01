import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    number_of_zeros = 0
    position = 50
    for line in input_lines:
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        # print("Position after", position)
        if position == 0:
            number_of_zeros += 1
    print("Number of times position is zero:", number_of_zeros)
if __name__ == "__main__":
    main()