import numpy as np
from haversine import haversine

def create_distance_matrix(points):
    n = len(points)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = haversine(points[i][1], points[i][2], 
                                       points[j][1], points[j][2])
    return matrix