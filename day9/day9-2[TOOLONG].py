import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import open_file
import math
import numpy as np
import math

def order_polygon_points(points):
    """
    Trie les points du périmètre dans l'ordre trigonométrique
    en utilisant le centroïde comme référence.
    """
    # Calculer le centroïde
    n = len(points)
    cx = sum(p[0] for p in points) / n
    cy = sum(p[1] for p in points) / n
    
    # Trier par angle par rapport au centroïde
    def angle_from_centroid(point):
        return math.atan2(point[1] - cy, point[0] - cx)
    
    return sorted(points, key=angle_from_centroid)

def point_in_polygon(x, y, polygon):
    """
    Teste si un point (x, y) est à l'intérieur du polygone.
    Utilise l'algorithme du ray-casting.
    """
    n = len(polygon)
    inside = False
    
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside


from shapely.geometry import Polygon, Point
from shapely.prepared import prep
import math

def get_integer_points_in_polygon(ordered_polygon):
    """
    Retourne tous les points à coordonnées entières dans le polygone.
    
    Args:
        ordered_polygon: liste de tuples [(x1, y1), (x2, y2), ...] déjà ordonnés
    
    Returns:
        liste de tuples (x, y) des points entiers à l'intérieur
    """
    # 1. Créer le polygone et le préparer (80x plus rapide)
    polygon = Polygon(ordered_polygon)
    prepared_polygon = prep(polygon)
    
    # 2. Déterminer la bounding box
    bounds = polygon.bounds  # (minx, miny, maxx, maxy)
    min_x = int(math.floor(bounds[0]))
    max_x = int(math.ceil(bounds[2]))
    min_y = int(math.floor(bounds[1]))
    max_y = int(math.ceil(bounds[3]))
    
    # 3. Tester tous les points entiers
    points_inside = []
    for x in range(min_x, max_x + 1):
        print(len(points_inside), x , "/", max_x ,"(", max_y - min_y, ")")
        for y in range(min_y, max_y + 1):
            if prepared_polygon.contains(Point(x, y)):
                points_inside.append((x, y))
    
    return points_inside

def main():
    # input_lines = open_file("example-1.txt")
    input_lines = open_file('code-1.txt')
    
    # Get red tiles coordinates and board size
    red_tiles_coords = []
    board_max_x, board_max_y = 0, 0
    for line in input_lines:
        parts = line.strip().split(',')
        x, y = map(int, parts)
        if x > board_max_x:
            board_max_x = x
        if y > board_max_y:
            board_max_y = y
        red_tiles_coords.append((x, y))
    print("Board size:", board_max_x, board_max_y)
        
    # Get green tiles coordinates (perimeter between red tiles)
    green_tiles_coords = []
    for coord in red_tiles_coords:
        for coord2 in red_tiles_coords:
            same_x = coord[0] == coord2[0]
            same_y = coord[1] == coord2[1]
            if coord != coord2 and (same_x or same_y):
                if same_x:
                     min_y = min(coord[1], coord2[1])
                     max_y = max(coord[1], coord2[1])
                     for y in range(min_y + 1, max_y):
                          green_tiles_coords.append((coord[0], y))
                if same_y:
                     min_x = min(coord[0], coord2[0])
                     max_x = max(coord[0], coord2[0])
                     for x in range(min_x + 1, max_x):
                          green_tiles_coords.append((x, coord[1]))
    print("Number of green tiles (perimeter):", len(green_tiles_coords))
    
    points = red_tiles_coords.copy()
    points.extend(green_tiles_coords)
    
    polygon = order_polygon_points(points)
    
    print("Polygon ordered")
    
    # filled_green_tiles = []
    # for x in range(board_max_x + 1):
    #     for y in range(board_max_y + 1):
    #         if point_in_polygon(x, y, polygon):
    #             filled_green_tiles.append((x, y))
                
    filled_green_tiles = get_integer_points_in_polygon(polygon)
                
    print("Number of filled green tiles (inside polygon):", len(filled_green_tiles))
        
    # board = [['.' for _ in range(board_max_x + 1)] for _ in range(board_max_y + 1)]
    # for (x, y) in red_tiles_coords:
    #     board[y][x] = '#'
    # for (x, y) in green_tiles_coords:
    #     if board[y][x] == '.':
    #         board[y][x] = 'X'
    # for (x, y) in filled_green_tiles:
    #     if board[y][x] == '.':
    #         board[y][x] = 'o'
            
    # print(np.array(board))
    
    all_points = set(red_tiles_coords + green_tiles_coords + filled_green_tiles)
    print("Total points inside polygon:", len(all_points))
    max_area = 0
    max_coords = (0, 0)
    for coord in red_tiles_coords:
        for coord2 in red_tiles_coords:
            if coord != coord2:
                invalid = False
                area = 0
                # Get all coords of rectangle
                c = []
                for x in range(min(coord[0], coord2[0]), max(coord[0], coord2[0]) + 1):
                    c.append((x, min(coord[1], coord2[1])))
                    c.append((x, max(coord[1], coord2[1])))
                for y in range(min(coord[1], coord2[1]), max(coord[1], coord2[1]) + 1):
                    c.append((min(coord[0], coord2[0]), y))
                    c.append((max(coord[0], coord2[0]), y))
                # Check if rectangle is fully inside polygon
                for rect_coords in c:
                    if rect_coords not in all_points:
                        invalid = True
                        break
                if invalid:
                    continue
                
                # Get number of points inside polygon
                for all_coord in all_points:
                    if all_coord[0] >= min(coord[0], coord2[0]) and all_coord[0] <= max(coord[0], coord2[0]) and all_coord[1] >= min(coord[1], coord2[1]) and all_coord[1] <= max(coord[1], coord2[1]):
                        area += 1
                if area > max_area:
                    max_area = area
                    max_coords = (coord, coord2)
                    
    # board = [['.' for _ in range(board_max_x + 1)] for _ in range(board_max_y + 1)]
    # for (x, y) in red_tiles_coords:
    #     board[y][x] = '#'
    # for (x, y) in green_tiles_coords:
    #     if board[y][x] == '.':
    #         board[y][x] = 'X'
    # for (x, y) in filled_green_tiles:
    #     if board[y][x] == '.':
    #         board[y][x] = 'o'
    # for x in range(min(max_coords[0][0], max_coords[1][0]), max(max_coords[0][0], max_coords[1][0]) + 1):
    #     for y in range(min(max_coords[0][1], max_coords[1][1]), max(max_coords[0][1], max_coords[1][1]) + 1):
    #         if board[y][x] == '.' or board[y][x] == 'o' or board[y][x] == 'X':
    #             board[y][x] = '*'
            
    # print(np.array(board))
                    
    print("Max area between red tiles inside polygon:", max_area)

if __name__ == "__main__":
    main()