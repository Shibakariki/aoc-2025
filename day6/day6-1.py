import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import numpy as np

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    all_operations = []
    for i, line in enumerate(input_lines):
        operations = line.strip().split(' ')
        operations = [op for op in operations if op]
        if i == len(input_lines) - 1:
            all_operations = [operations] + all_operations
        else:
            all_operations.append(operations)
            
    signs = all_operations[0]
    operations = [0 if sign == '+' else 1 for sign in signs]
    for op in all_operations[1:]:
        for i, sign in enumerate(signs):
            if sign == '+':
                operations[i] += int(op[i])
            elif sign == '*':
                operations[i] *= int(op[i])
        
                
    print('Final operations:', operations)
    print('Sum of operations:', sum(operations))
                    
if __name__ == "__main__":
    main()