import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

import json
import pandas as pd
import numpy as np
from tqdm import tqdm
import networkx as nx
from karateclub import Graph2Vec, GL2Vec, SF, FGSD 
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression

import numpy as np
import karateclub
import networkx as nx
from scipy import sparse
import math
from tqdm import tqdm
from karateclub.dataset import GraphSetReader
import pandas as pd
import random
from karateclub import DeepWalk, FGSD
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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

    theta = np.array([float(i)/20 for i in range(1,51)])
    X = np.cos(np.outer(x, theta))



    feature_blocks = []
    for _ in range(order):
        X = A_tilde.dot(X)
        feature_blocks.append(X)
    X = np.concatenate(feature_blocks, axis=1)
    pooled_x = np.mean(X, axis=0)
    return pooled_x




def tester(y, X):
    aucs = []
    for i in range(10):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
        downstream_model = LogisticRegression(random_state=0,solver ="saga").fit(X_train, y_train)
        y_hat = downstream_model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_hat)
        print(auc)
        aucs.append(auc)
    print(round(np.mean(aucs),3))
    print(round(np.std(aucs),3))


def stat_calculator(graphs):
    print("graph count")
    print(len(graphs))
    print("nodes")
    print(min([g.number_of_nodes() for g in graphs]))
    print(max([g.number_of_nodes() for g in graphs]))
    #print("density")
    #print(round(min([nx.density(g) for g in graphs]),3))
    #print(round(max([nx.density(g) for g in graphs]),3))
    #print("diameter")
    #print(round(min([nx.diameter(g) for g in graphs]),3))
    #print(round(max([nx.diameter(g) for g in graphs]),3))

def runner(name):
    print("-------------------------------------------------")
    print(name)
    print("-------------------------------------------------")
    graphs = json.load(open("./graph_level/"+name+"_edges.json"))
    y = np.array(pd.read_csv("./graph_level/"+name+"_target.csv")["target"])
    y = y[0:10000]
    graphs = [nx.from_edgelist(graphs[str(i)]) for i in tqdm(range(y.shape[0]))]


    X = np.array([create_sketch(graph, 5) for graph in tqdm(graphs)])
    tester(y, X)
    
    #print("-------------------------------------------------")
    #print("SF")
    #model = SF()
    #model.fit(graphs)
    #X = model.get_embedding()
    #tester(y, X)

    #print("-------------------------------------------------")
    #print("FGSD")
    #model = FGSD()
    #model.fit(graphs)
    #X = model.get_embedding()
    #tester(y, X)


runner("reddit")
