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
    networks = [[boxe] for boxe in range(len(boxes_coords))]
    print("Initial networks:", networks)
    nb_of_connections_remaining = 1000
    while nb_of_connections_remaining > 0:
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
            nb_of_connections_remaining -= 1
        print("Current networks state:", networks)
        
    print("Final networks:", networks)
    number_in_networks = [len(network) for network in networks]
    print("Number in networks:", number_in_networks)
    print("3 largest networks:", sorted(number_in_networks, reverse=True)[:3])
                                    

    
                    
if __name__ == "__main__":
    main()