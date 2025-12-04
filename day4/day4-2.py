import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import numpy as np

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    
    board = np.array([[char for char in line.strip()] for line in input_lines])
    nb_lines = len(board)
    nb_cols = len(board[0])
    print(f"Number of lines: {nb_lines}, Number of columns: {nb_cols}")
    print(board)
    
    new_board = board.copy()
    good_papers = 0
    relaunch = True
    while(relaunch):
        for l in range(nb_lines):
            for c in range(nb_cols):
                # print(f"Element at ({l}, {c}): {board[l][c]}")
                # get 8's neighbors
                if board[l][c] != '@':
                    continue
                neighbors = []
                for dl in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dl == 0 and dc == 0:
                            continue
                        nl, nc = l + dl, c + dc
                        if 0 <= nl < nb_lines and 0 <= nc < nb_cols:
                            neighbors.append(board[nl][nc])
                # print(f"Neighbors: {neighbors}")
                if neighbors.count('@') >= 4:
                    print(f"Element at ({l}, {c}) has {neighbors.count('@')} '@' neighbors.")
                else:
                    new_board[l][c] = 'x'
                    good_papers += 1
        print(new_board)
        print(f"Number of good papers: {good_papers}")
        if np.array_equal(board, new_board):
            relaunch = False
        board = new_board.copy()
    
if __name__ == "__main__":
    main()