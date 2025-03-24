import csv
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from deap import base, creator, tools, algorithms
from plot_on_sphere import plot_route_on_sphere
from plot_route import plot_route
from print_route_details import print_route_details
from haversine import haversine
from settings import MAX_TIME, SPEED, POPULATION_SIZE, GENERATIONS, CXPB, MUTPB
from setup import setup
from create_distance_matrix import create_distance_matrix
from genetic_algorithm_tsp import genetic_algorithm_tsp
from calculate_total_time import calculate_total_time

def main(csv_file, office_lat, office_lon, garage_lat, garage_lon):
    points = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                try:
                    num, lat, lon = row
                    points.append((f"Colab {num.strip()}", float(lat), float(lon)))
                except ValueError:
                    continue
    
    points.append(("Garagem", garage_lat, garage_lon))
    points.append(("Escritório", office_lat, office_lon))
    garage_idx = len(points) - 2
    office_idx = len(points) - 1
    toolbox = setup(len(points) - 2)
    best_route = genetic_algorithm_tsp(points, garage_idx, office_idx, toolbox)
    
    distance_matrix = create_distance_matrix(points)
    total_time = calculate_total_time(best_route, distance_matrix, garage_idx,office_idx)
    print_route_details(points, best_route, distance_matrix, garage_idx, office_idx, total_time)
    plot_route(points, best_route, (garage_lat, garage_lon), (office_lat, office_lon), total_time)
    plot_route_on_sphere(points, best_route, (garage_lat, garage_lon), (office_lat, office_lon), total_time)

if __name__ == "__main__":
    csv_file = "coordinates.csv"
    office_coords = (-23.556466554081997, -46.66260117644396)
    garage_coords = (-23.609414526900654, -46.64490736778047)
    
    main(csv_file, *office_coords, *garage_coords)