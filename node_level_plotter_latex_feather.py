import numpy as np
from tqdm import tqdm
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import karateclub

from scipy import sparse
import math

from karateclub.dataset import GraphReader
import random


def create_D_inverse(graph):
    """
    Creating a sparse inverse degree matrix.
    Arg types:
        * **graph** *(NetworkX graph)* - The graph to be embedded.
    Return types:
        * **D_inverse** *(Scipy array)* - Diagonal inverse degree matrix.
    """
    index = np.arange(graph.number_of_nodes())
    values = np.array([1.0/graph.degree[node] for node in range(graph.number_of_nodes())])
    shape = (graph.number_of_nodes(), graph.number_of_nodes())
    D_inverse = sparse.coo_matrix((values, (index, index)), shape=shape)
    return D_inverse




def create_sketch(graph, order):
    A = nx.adjacency_matrix(graph, nodelist = range(graph.number_of_nodes()))
    D_inverse = create_D_inverse(graph) 
    A_tilde = D_inverse.dot(A)

    x = np.array([math.log(nx.degree(graph,node)) for node in range(graph.number_of_nodes())])
    #x = np.array([graph.degree(node) for node in range(graph.number_of_nodes())])
    theta = np.array([float(i)/200 for i in range(1,501)])
    X = np.cos(np.outer(x, theta))



    feature_blocks = []
    for _ in range(order):
        X = A_tilde.dot(X)
    #X = np.concatenate(feature_blocks, axis=1)
    #pooled_x = np.mean(X, axis=0)
    return X





def plotter(graph, y, order, classes, dataset):
    Z = create_sketch(graph, order)
    for node_cl in range(classes):
        X = Z[y==node_cl, :]
        theta = np.array([float(i)/200 for i in range(1,501)])
        X_mean = np.mean(X, axis=0)
        X_error = np.std(X, axis=0)
        for i in range(500):
            print("("+str(round(theta[i],4))+str(",") +str(round(X_mean[i],4))+")")
        for i in range(500):
            print("("+str(round(theta[i],4))+str(",") +str(round(X_mean[i]+X_error[i],4))+")")
        for i in range(500):
            print("("+str(round(theta[i],4))+str(",") +str(round(X_mean[i]-X_error[i],4))+")")


dataset = "twitch"

reader = GraphReader(dataset)

graph = reader.get_graph()

y = reader.get_target()

plotter(graph, y, 3, 2, dataset)
