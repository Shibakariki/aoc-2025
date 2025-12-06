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
        operations = list(line)
        
        if i == len(input_lines) - 1:
            all_operations = [operations] + all_operations
        else:
            all_operations.append(operations)
            
    signs = [op for op in all_operations[0] if op in ['+', '*']]
    new_operations = np.array(all_operations[1:]).T.tolist()
    all_numbers = []
    for operations in new_operations:
        number = ""
        for op in operations:
            # print(op)
            number += op
            
        all_numbers.append(number)
        # print(number)
        # print('---')
    # print(all_numbers)
    
    no_operations = 0
    operations = [0 if sign == '+' else 1 for sign in signs]
    for number in all_numbers:
        # print(number, no_operations)
        if not number.strip():
            no_operations += 1
            continue
        elif signs[no_operations] == '+':
            operations[no_operations] += int(number)
        elif signs[no_operations] == '*':
            operations[no_operations] *= int(number)

        print('Final operations:', operations)
    print('Sum of operations:', sum(operations))        
                       
if __name__ == "__main__":
    main()