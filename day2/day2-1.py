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
        size_start = len(str(start))
        size_end = len(str(end))
        
        # print(f"{start} - {end}")
        for i in range(start, end + 1):
            if (str(i)[:size_start//2] == str(i)[size_start//2:]):
                invalid_ids += i
                # print(f"  {str(i)[:size_start//2]}")
                # print(f"  {str(i)[size_start//2:]}")
                # print("------")
            elif (size_start != size_end) and (str(i)[:size_end//2] == str(i)[size_end//2:]):
                invalid_ids += i
                # print(f"  {str(i)[:size_end//2]}")
                # print(f"  {str(i)[size_end//2:]}")
                # print("======")
                
    print(f"Sum Invalid IDs: {invalid_ids}")
        
    
if __name__ == "__main__":
    main()