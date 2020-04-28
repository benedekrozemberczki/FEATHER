"""Running FEATHER."""

from utils import tab_printer
from feather import FEATHER, FEATHERG
from param_parser import parameter_parser
from utils import load_graph, load_features, load_graphs, save_embedding

def main(args):
    """
    Characteristic function embedding wrapper.
    :param args: Arguments object parsed up.
    """
    if args.model_type == "FEATHER":
        print("\nFitting a node embedding.\n")
        graph = load_graph(args.graph_input)
        features = load_features(args.feature_input)
        model = FEATHER()
        model.fit(graph, features)
    elif args.model_type == "FEATHER-G":
        print("\nFitting a graph level embedding.\n")
        graphs = load_graphs(args.graphs_input)
        model = FEATHERG()
        model.fit(graphs)
    else:
        quit()
    X = model.get_embedding()
    save_embedding(X, args.output)

if __name__ == "__main__":
    args = parameter_parser()
    tab_printer(args)
    main(args)
