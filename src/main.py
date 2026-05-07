import numpy as np
import matplotlib.pyplot as plt
from grid import Grid
from stochastics import gen

grid = Grid(20)
i, j = np.meshgrid(np.arange(20), np.arange(20))
num = np.zeros((20,20))

for x, y in grid.graph.nodes():
    num[y, x] = gen(x, y, 10)

# plot
plt.contourf(i, j, num, 50)
plt.colorbar()
plt.scatter(i, j, marker='.', color='r', s=8)
plt.show()