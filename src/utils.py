"""Reading data and printing."""

import json
import numpy as np
import pandas as pd
import networkx as nx
from texttable import Texttable

def tab_printer(args):
    """
    Function to print the logs in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable()
    t.add_rows([["Parameter", "Value"]] + [[k.replace("_", " ").capitalize(), args[k]] for k in keys])
    print(t.draw())

def load_graph(graph_path):
    """
    Reading a NetworkX graph.
    :param graph_path: Path to the edge list.
    :return graph: NetworkX object.
    """
    data = pd.read_csv(graph_path)
    edges = data.values.tolist()
    edges = [[int(edge[0]), int(edge[1])] for edge in edges]
    graph = nx.from_edgelist(edges)
    graph.remove_edges_from(nx.selfloop_edges(graph))
    return graph

def load_features(features_path):
    """
    Reading the features from drive.
    :param features_path: Location of features on drive.
    :return features: Features Numpy array.
    """
    features =  np.array(pd.read_csv(features_path))
    return features

def load_graphs(graphs_path):
    """
    Reading a NetworkX graph.
    :param graphs_path: Path to the graphs JSON file.
    :return graphs: List of NetworkX graphs. 
    """
    graphs = json.load(open(graphs_path))
    graphs = [nx.from_edgelist(graphs[str(k)]) for k in range(len(graphs))]
    return graphs

def save_embedding(X, output_path):
    """
    Saving the node embedding.
    :param X: Node embedding array.
    :param output_path: Path for saving the node embedding.
    """
    embedding = np.concatenate([np.arange(X.shape[0]).reshape(-1, 1), X], axis=1)
    columns = ["id"] + ["x_" + str(x) for x in range(X.shape[1])]
    embedding = pd.DataFrame(embedding, columns=columns)
    embedding.to_csv(output_path, index=None)
