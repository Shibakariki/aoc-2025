import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file_two_lists
import numpy as np

def main():
    # ranges, _ = open_file_two_lists('example-1.txt')
    ranges, _ = open_file_two_lists('code-1.txt')
    fresh_ids = 0
    
    # Parse and sort ranges
    intervals = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        intervals.append((start, end))
    intervals.sort()    
    
    # Merge ranges
    merged_ranges = []
    for start, end in intervals:
        if not merged_ranges or start > merged_ranges[-1][1]:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
    
    print(f"Merged Ranges: {merged_ranges}")
    
    # Get fresh IDs
    for r in merged_ranges:
        fresh_ids += r[1] - r[0] + 1
    
    print(f"Total fresh IDs: {fresh_ids}")
    
if __name__ == "__main__":
    main()