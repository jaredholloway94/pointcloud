import numpy as np
import scipy as sp
import networkx as nx
import matplotlib.pyplot as plt

pts = np.genfromtxt("bunny.csv", delimiter=",", dtype=np.float32)
pts = np.unique(pts,axis=0)

K = 5

pt_distances = sp.spatial.distance.cdist(pts,pts)
pt_neighbors = pt_distances.argsort(axis=1)[:, 1:K+1]
pt_neighbor_coordinates = pts[pt_neighbors]

tpos = np.mean(pt_neighbor_coordinates, axis=1)
tpo_distances = sp.spatial.distance.cdist(tpos,tpos)
tpo_neighbors = tpo_distances.argsort(axis=1)[:, 1:K+1]
tpo_neighbor_coordinates = tpos[tpo_neighbors]

tpo_graph = nx.Graph()
tpo_graph.add_nodes_from([
    (i, {'x':t[0], 'y':t[1], 'z':t[2]})
    for i,t in enumerate(tpos)
    ])
tpo_graph.add_edges_from([
    (i, int(n), {'weight':tpo_distances[i][n]})
    for i,t in enumerate(tpo_neighbors)
    for n in t
    ])

nx.draw(tpo_graph)
plt.show()

