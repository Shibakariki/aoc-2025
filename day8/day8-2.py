import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import math
import numpy as np

def main():
    # input_lines = open_file("example-1.txt")
    input_lines = open_file('code-1.txt')
    
    boxes_coords = []
    for line in input_lines:
        parts = line.strip().split(',')
        x, y, z = map(int, parts)
        boxes_coords.append((x, y, z))
        
    # print("Boxes coordinates:", boxes_coords)
    
    # Create distance matrix
    distance_matrix = []
    for i, coord in enumerate(boxes_coords):
        row = []
        for j, other_coord in enumerate(boxes_coords):
            if i == j:
                row.append(0)
            else:
                row.append(math.dist(coord, other_coord))
        distance_matrix.append(row)
    
    # print(np.array(distance_matrix).round(0))
    
    # Find the minimum distance in the distance matrix excluding zeros
    networks = [[box] for box in range(len(boxes_coords))]
    print("Initial networks:", networks)
    while len(networks) > 2:
        min_distance = float('inf')
        min_duo = []
        for i in range(len(distance_matrix)):
            for j in range(len(distance_matrix)):
                if i != j and distance_matrix[i][j] < min_distance:
                    min_distance = distance_matrix[i][j]
                    min_duo = [i,j]
        print("New min duo found:", min_duo, "with distance", min_distance)
        min_duo_0_network = None
        min_duo_1_network = None
        for network in networks:
            if type(network) == list:
                if min_duo[0] in network:
                    min_duo_0_network = network
                if min_duo[1] in network:
                    min_duo_1_network = network
        print("Duo networks found:", min_duo_0_network, min_duo_1_network)
        if min_duo_0_network is not None and min_duo_1_network is not None:
            # Merge networks
            if min_duo_0_network != min_duo_1_network:
                new_network = set(min_duo_0_network + min_duo_1_network)
                networks.remove(min_duo_0_network)
                networks.remove(min_duo_1_network)
                networks.append(list(new_network))
                print(f"Merging networks {min_duo_0_network} and {min_duo_1_network} into {new_network}")

                    
            distance_matrix[min_duo[0]][min_duo[1]] = float('inf')
            distance_matrix[min_duo[1]][min_duo[0]] = float('inf')
            # nb_of_connections_remaining -= 1
        print("Current networks state:", networks)
        
    print("Final networks:", networks)
    last_box = [network for network in networks if len(network) == 1][0][0]
    print("Isolated box:", last_box)
    nearest_box_dist = float('inf')
    nearest_box_index = -1
    for dist in distance_matrix[last_box]:
        if dist < nearest_box_dist and dist != 0:
            nearest_box_dist = dist
            nearest_box_index = distance_matrix[last_box].index(dist)
    print("Nearest box to isolated box:", nearest_box_index, "with distance", nearest_box_dist)
    print("last_box:", last_box, "nearest_box_index:", nearest_box_index, "=>", boxes_coords[last_box], boxes_coords[nearest_box_index])
    print("Result:", boxes_coords[last_box][0] * boxes_coords[nearest_box_index][0])
    
    
                    
if __name__ == "__main__":
    main()