from math import ceil
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file_one_line

def main():
    # input_line = open_file_one_line('example-1.txt')
    input_line = open_file_one_line('code-1.txt')
    
    invalid_ids = 0
    for part in input_line.split(','):
        range_part = part.split('-')
        start = int(range_part[0])
        end = int(range_part[1])
        size_start = 1
        size_end = len(str(end))
        
        # print(f"{start} - {end}")
        for i in range(start, end + 1):
            for j in range(size_start, size_end + 1):
                str_i = str(i)
                part_size = j
                parts = [str_i[k*part_size:(k+1)*part_size] for k in range(ceil(len(str_i)/part_size))]
                if all(part == parts[0] for part in parts) and len(parts) > 1 :
                    invalid_ids += i
                    # print(f"  {parts} parts of size {part_size} in {str_i}")
                    # print("------")
                    break
                
    print(f"Sum Invalid IDs: {invalid_ids}")
        
    
if __name__ == "__main__":
    main()