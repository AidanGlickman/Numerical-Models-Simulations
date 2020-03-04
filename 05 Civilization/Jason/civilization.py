#!/usr/bin/env python
import numpy as np
import math
from numpy.polynomial.polynomial import polyfit
import networkx as nx
import random
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.centrality import betweenness_centrality
import matplotlib.pyplot as plt

graph_path = "countries.txt"

# Read file
adj_list = []
with open("countries.txt", "r") as f:
    for line in f:
        adj_list.append([int(i)-1 for i in line.strip().split(" ")])

# Quick check
def check_reciprocal_connections(adj_list):
    for i in range(len(adj_list)):
        for j in adj_list[i]:
            if i not in adj_list[j]:
                print("--- Error in graph: country {} not connected reciprocally with {} ---".format(j+1, i+1))

# Convert adj_list to dict_of_lists
d = {}
for i in range(len(adj_list)):
    d[str(i)] = [str(j) for j in adj_list[i]]

# Use nx to visualize graph
def visualize(d):
    G = nx.from_dict_of_lists(d)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=10)
    nx.draw_networkx_edges(G, pos)
    plt.show()
# visualize(d)

def simulate(adj_list, start_node, turns):
    countries = [0] * len(adj_list)
    occupy_count = []
    countries[start_node] = 1

    for turn in range(turns):
        occupy_count.append(sum(countries))
        countries_copy = countries.copy()
        for c in range(len(countries_copy)):
            if countries_copy[c]:
                possible_moves = []  # unoccupied neighbors
                for j in adj_list[c]:
                    if countries[j] == 0:
                        possible_moves.append(j)

                if len(possible_moves) == 0:
                    continue
                elif len(possible_moves) == 1:
                    u = possible_moves[0]
                    countries[c] = 1
                    countries[u] = 1
                else:
                    u, v = random.sample(possible_moves, 2)
                    countries[c] = 0
                    countries[u] = 1
                    countries[v] = 1

    return occupy_count


total = []
for i in range(len(adj_list)):
    sim = np.array(simulate(adj_list, i, 20))
    total.append(sim)
    plt.plot(sim)
plt.plot(np.average(total, axis=0))
plt.show()

print(np.maximum.reduce(total))
np.savetxt("results20.txt", tuple(total), fmt="%d")