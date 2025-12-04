import os
import sys

from numpy import argmax, argmin
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file

def main():
    input_lines = open_file('example-1.txt')
    # input_lines = open_file('code-1.txt')
    
    all_voltage = 0
    for line in input_lines:
        min3digits = [-1,-1,-1]
        min3digitsposition = [-1,-1,-1]
        remaining_digits = 0
        # Check the best digit by window of 4 digits
        for i,(d1, d2, d3, d4) in enumerate(zip(line, line[1:], line[2:], line[3:])):
            d1 = int(d1)
            d2 = int(d2)
            d3 = int(d3)
            d4 = int(d4)
            max_idx = argmax([d1, d2, d3, d4])
            # print(f"Window {d1}{d2}{d3}{d4} -> maxIdx {max_idx}")
            if max_idx == 1:
                if i in min3digitsposition:
                    continue
                if remaining_digits == 0:
                    min3digits[0] = d1
                    min3digitsposition[0] = i
                elif remaining_digits == 1:
                    min3digits[1] = d1
                    min3digitsposition[1] = i
                elif remaining_digits == 2:
                    min3digits[2] = d1
                    min3digitsposition[2] = i
                remaining_digits += 1
            elif max_idx == 2:
                if i in min3digitsposition or i+1 in min3digitsposition:
                    continue
                if remaining_digits == 0:
                    min3digits[0] = d1
                    min3digits[1] = d2
                    min3digitsposition[0] = i
                    min3digitsposition[1] = i+1
                elif remaining_digits == 1:
                    min3digits[1] = d1
                    min3digits[2] = d2
                    min3digitsposition[1] = i
                    min3digitsposition[2] = i+1
                elif remaining_digits == 2:
                    min3digits[2] = d1
                    min3digitsposition[2] = i
                remaining_digits += 2
            elif max_idx == 3:     
                if i in min3digitsposition or i+1 in min3digitsposition or i+2 in min3digitsposition:
                    continue
                if remaining_digits == 0:
                    min3digits[0] = d1
                    min3digits[1] = d2
                    min3digits[2] = d3
                    min3digitsposition[0] = i
                    min3digitsposition[1] = i+1
                    min3digitsposition[2] = i+2
                elif remaining_digits == 1:
                    max_d = argmax([d1,d2,d3])
                    min3digits[1] = d1 if max_d != 0 else d2
                    min3digits[2] = d2 if max_d != 0 and max_d != 1 else d3
                    min3digitsposition[1] = i if max_d != 0 else i+1
                    min3digitsposition[2] = i+1 if max_d != 0 and max_d != 1 else i+2
                elif remaining_digits == 2:
                    list_d = [d1, d2, d3]
                    min_d = argmin(list_d)
                    min3digits[2] = list_d[min_d]
                    min3digitsposition[2] = i + min_d
                remaining_digits += 3
            else:
                if i == 11:
                    if remaining_digits == 0:
                        min3digits[0] = d2
                        min3digits[1] = d3
                        min3digits[2] = d4
                        min3digitsposition[0] = i+1
                        min3digitsposition[1] = i+2
                        min3digitsposition[2] = i+3
                    elif remaining_digits == 1:      
                        min3digits[1] = d3
                        min3digits[2] = d4
                        min3digitsposition[1] = i+2
                        min3digitsposition[2] = i+3
                    elif remaining_digits == 2:
                        min3digits[2] = d4
                        min3digitsposition[2] = i+3
                else:
                    continue
            # print(min3digits,"[", min3digitsposition, "]", remaining_digits)
            # get all digits without the min3digits by ising their positions
        voltage = line[:min3digitsposition[0]] + line[min3digitsposition[0]+1:min3digitsposition[1]] + line[min3digitsposition[1]+1:min3digitsposition[2]] + line[min3digitsposition[2]+1:]
        print(f"  Voltage without min3digits: {voltage}")
        all_voltage += int(voltage)
    print(f"All voltage: {all_voltage}")
    
if __name__ == "__main__":
    main()