import numpy as np
from cost import calculate_expected_cost


def random_search(grid_instance, time, N, iterations=100):
    nodes = list(grid_instance.graph.nodes())
    rng = np.random.default_rng()

    best_stations = None
    best_cost = float("inf")

    for _ in range(iterations):
        idx = rng.choice(len(nodes), size=N, replace=False)
        stations = [nodes[i] for i in idx]
        cost = calculate_expected_cost(grid_instance, time, stations)
        if cost < best_cost:
            best_cost = cost
            best_stations = stations

    return best_stations, best_cost


def greedy_optimizer(grid_instance, time, N):
    all_nodes = list(grid_instance.graph.nodes())
    chosen = []
    chosen_set = set()

    for _ in range(N):
        best_candidate = None
        best_cost = float("inf")
        for candidate in all_nodes:
            if candidate in chosen_set:
                continue
            trial = chosen + [candidate]
            cost = calculate_expected_cost(grid_instance, time, trial)
            if cost < best_cost:
                best_cost = cost
                best_candidate = candidate
        chosen.append(best_candidate)
        chosen_set.add(best_candidate)

    final_cost = calculate_expected_cost(grid_instance, time, chosen)
    return chosen, final_cost
