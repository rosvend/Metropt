import numpy as np 
from stochastics import expected_population

def prob_node(origin, destination,time):
    mass_o = expected_population(origin[0],origin[1],time)
    mass_d = expected_population(destination[0],destination[1],time)
    return mass_o * mass_d

def nearest_station(grid_instance,node,stations):
    return min(stations, key=lambda station: grid_instance.manhattan_distance(node, station))