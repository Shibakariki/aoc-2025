import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    all_voltage = 0
    for line in input_lines:
        first_digit = 0
        second_digit = 0
        for i, digit in enumerate(line):
            digit = int(digit)
            if digit > first_digit and i != len(line) - 1:
                second_digit = first_digit
                first_digit = digit
                second_digit = 0
            elif digit > second_digit:
                second_digit = digit
        # print(first_digit, second_digit)
        all_voltage += int(first_digit)*10 + int(second_digit)
    print(f"All voltage: {all_voltage}")
    
if __name__ == "__main__":
    main()