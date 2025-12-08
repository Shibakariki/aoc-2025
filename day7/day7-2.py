import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import networkx as nx

def main():
    # input_lines = open_file('example-1.txt')
    input_lines = open_file('code-1.txt')
    
    # Create matrix representation
    matrix = [list(line.strip()) for line in input_lines]

    nodes = []
    last_line = ["." for _ in range(len(matrix[0]))]
    for i, line in enumerate(matrix):
        diagram = line
        for j, char in enumerate(diagram):
            if i == len(matrix) - 1 and char == "|":
                last_line[j] = "^"
                nodes.append((i, j))
            if char == "S":
                matrix[i + 1][j] = "|"
                # nodes.append((i + 1, j))
            if char == "^":
                nodes.append((i, j))
                matrix[i][j-1] = "|"
                if i < len(matrix) - 1 and matrix[i + 1][j] == ".":
                    matrix[i+1][j-1] = "|"
                matrix[i][j+1] = "|"
                if i < len(matrix) - 1 and matrix[i + 1][j] == ".":
                    matrix[i+1][j+1] = "|"
            if char == "|" and i < len(matrix) - 1 and matrix[i + 1][j] == ".":
                matrix[i + 1][j] = "|"
    matrix.append(last_line)
    # print(np.array(matrix))
    
    # Add directive edges 2 between nodes based on only x coordinates
    edges = []
    for node in nodes:
        i, j = node
        right_node_remaining = True
        left_node_remaining = True
        for target in nodes:
            ti, tj = target
            if tj == j + 1 and ti >= i + 1 and right_node_remaining:
                edges.append((node, target))
                right_node_remaining = False
            elif tj == j - 1 and ti >= i + 1 and left_node_remaining:
                edges.append((node, target))
                left_node_remaining = False
                # print("Node:", node)
                # print(f"Adding edge between {node} and {target}")
    
    G = nx.DiGraph()
    for idx, (i, j) in enumerate(nodes):
        G.add_node(idx, pos=(j, -i))  # Note: Invert i for correct y-axis orientation            

        # Create edges in the graph Directed
    for edge in edges:
        src = nodes.index(edge[0])
        dst = nodes.index(edge[1])
        G.add_edge(src, dst)        
        
    print("Number of nodes:", G.number_of_nodes())
    pos = nx.get_node_attributes(G, 'pos')
    # nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, edge_color="gray")
    # Get number of unique paths
    start_nodes = [idx for idx, (i, _) in enumerate(nodes) if i == 2]
    end_nodes = [idx for idx, (i, _) in enumerate(nodes) if i == len(matrix) - 2]
    total_paths = 0
    
    # ------------------------------------------------------
    
    print("Start count")

    # Precompute topological order (DiGraph must be acyclic — if not, we detect it)
    topo = list(nx.topological_sort(G))

    # Prepare DP array
    path_count = {n: 0 for n in G.nodes()}

    total_paths = 0

    for start in start_nodes:
        # Reset counts for each start
        for n in path_count:
            path_count[n] = 0
        path_count[start] = 1

        for node in topo:
            for succ in G.successors(node):
                path_count[succ] += path_count[node]

        # Add paths leading to all end nodes
        total_paths += sum(path_count[end] for end in end_nodes)
        print(total_paths)

    print("Total unique paths:", total_paths)
           
if __name__ == "__main__":
    main()