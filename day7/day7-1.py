import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import numpy as np

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    beams = []
    nb_splits = 0
    for i, line in enumerate(input_lines):
        diagram = line.strip()
        for j, char in enumerate(diagram):
            if char == 'S':
                beams.append(j)
            if char == "^" and j in beams:
                beams.remove(j)
                if j-1 not in beams:
                    beams.append(j - 1)
                if j+1 not in beams:
                    beams.append(j + 1)
                nb_splits += 1
    print(f"Number of splits: {nb_splits}")
        
    
                    
if __name__ == "__main__":
    main()