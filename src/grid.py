import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt

class Grid: 
    def __init__(self, size): 
        self.size = size 
        self.graph = nx.grid_2d_graph(size, size)

    def plot(self):
        pos = {(x, y): (x, y) for x, y in self.graph.nodes()}
        nx.draw(self.graph, pos=pos, with_labels=True, node_size=600, node_color='lightblue')
        plt.show()

    def manhattan_distance(self, node1, node2):
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))