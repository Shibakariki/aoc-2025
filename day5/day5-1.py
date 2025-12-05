import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file_two_lists
import numpy as np

def main():
    # ranges, ids = open_file_two_lists('example-1.txt')
    ranges, ids = open_file_two_lists('code-1.txt')
    fresh_ids = 0
    for i in ids:
        for r in ranges:
            start, end = map(int, r.split('-'))
            id_num = int(i)
            print(f"Checking ID {id_num} against range {start}-{end}")
            if start <= id_num <= end:
                fresh_ids += 1
                print(f"ID {id_num} is in range {r}")
                break
    
    print(f"Total fresh IDs: {fresh_ids}")
    
if __name__ == "__main__":
    main()