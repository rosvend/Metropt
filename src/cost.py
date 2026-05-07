import numpy as np
from grid import Grid
from transit import prob_node, nearest_station

def calculate_expected_cost(grid_instance, time, stations):
    total_expected_cost = 0
    nodes = list(grid_instance.graph.nodes())
    
    # Loop over every possible Origin (O) and Destination (D) pair
    for origin in nodes:
        for destination in nodes:
            #trip probability
            prob = prob_node(origin, destination, time)
            
            # find nearest stations for O and D
            station_o = nearest_station(grid_instance, origin, stations)
            station_d = nearest_station(grid_instance, destination, stations)
            
            # find the walking distance
            walk_1 = grid_instance.manhattan_distance(origin, station_o)
            walk_2 = grid_instance.manhattan_distance(station_d, destination)
            
            # Add to total expected cost
            total_expected_cost += prob * (walk_1 + walk_2)
            
    return total_expected_cost
