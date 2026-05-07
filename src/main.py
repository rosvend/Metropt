import numpy as np
import matplotlib.pyplot as plt
from grid import Grid
from stochastics import expected_population
from optimizer import greedy_optimizer

GRID_SIZE = 20
TIME = 10
N_STATIONS = 5

grid = Grid(GRID_SIZE)

stations, cost = greedy_optimizer(grid, TIME, N_STATIONS)
print(f"Optimal stations (t={TIME}, N={N_STATIONS}):")
for s in stations:
    print(f"  {s}")
print(f"Expected cost: {cost:.4f}")

i, j = np.meshgrid(np.arange(GRID_SIZE), np.arange(GRID_SIZE))
expected = np.zeros((GRID_SIZE, GRID_SIZE))
for x, y in grid.graph.nodes():
    expected[y, x] = expected_population(x, y, TIME, grid_size=GRID_SIZE)

fig, ax = plt.subplots(figsize=(8, 7))
cf = ax.contourf(i, j, expected, 50, cmap="viridis")
fig.colorbar(cf, ax=ax, label=f"Expected population at t={TIME}")

xs = [s[0] for s in stations]
ys = [s[1] for s in stations]
ax.scatter(xs, ys, marker="*", s=400, c="yellow",
           edgecolors="black", linewidths=1.5, zorder=5,
           label="Optimal stations")

ax.set_title(f"Greedy STRO: {N_STATIONS} stations, cost={cost:.2f}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc="upper right")
ax.set_aspect("equal")
plt.tight_layout()
plt.show()
