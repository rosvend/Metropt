import numpy as np
from grid import Grid
from transit import weight_node, nearest_station
from stochastics import expected_population_field


def calculate_expected_cost(grid_instance, time, stations):
    # Algebraic collapse: sum_{O,D} pop_O*pop_D*(d(O,S_O)+d(D,S_D)) = 2 * total_pop * sum_O pop_O * d(O,S_O)
    size = grid_instance.size
    pop = expected_population_field(size, time)

    coords = np.arange(size)
    X, Y = np.meshgrid(coords, coords, indexing='xy')
    sx = np.fromiter((s[0] for s in stations), dtype=int, count=len(stations))
    sy = np.fromiter((s[1] for s in stations), dtype=int, count=len(stations))

    dist = np.abs(X[None] - sx[:, None, None]) + np.abs(Y[None] - sy[:, None, None])
    nearest = dist.min(axis=0)

    return 2.0 * pop.sum() * (pop * nearest).sum()


def calculate_expected_cost_reference(grid_instance, time, stations):
    total_expected_cost = 0
    nodes = list(grid_instance.graph.nodes())

    for origin in nodes:
        for destination in nodes:
            prob = weight_node(origin, destination, time)
            station_o = nearest_station(grid_instance, origin, stations)
            station_d = nearest_station(grid_instance, destination, stations)
            walk_1 = grid_instance.manhattan_distance(origin, station_o)
            walk_2 = grid_instance.manhattan_distance(station_d, destination)
            total_expected_cost += prob * (walk_1 + walk_2)

    return total_expected_cost
