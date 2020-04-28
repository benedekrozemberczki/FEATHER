"""Parameter parsing."""

import argparse

def parameter_parser():
    """
    Parsing the parameters from the command line.
    """
    parser=argparse.ArgumentParser(description="Run FEATHER / FEATHER-G.")

    parser.add_argument('--graph-input',
                        nargs='?',
                        default="./input/edges/ER_edges.csv",
	                help='Input edge list csv.')

    parser.add_argument('--feature-input',
                        nargs='?',
                        default="./input/features/ER_features.csv",
	                help='Input features csv.')

    parser.add_argument('--graphs-input',
                        nargs='?',
                        default='./input/graphs/ER_graphs.json',
	                help='Input graphs as JSON.')

    parser.add_argument('--output',
                        nargs='?',
                        default='./output/ER_node_embedding.csv',
	                help='Embeddings path.')

    parser.add_argument('--eval-points',
                        type=int,
                        default=25,
	                help='Number of evaluation points. Default is 25.')

    parser.add_argument('--order',
                        type=int,
                        default=5,
	                help='Order of adjancency matrix powers. Default is 5.')

    parser.add_argument('--theta-max',
                        type=float,
                        default=2.5,
	                help='Largest characteristic function evaluation point. Default is 2.5.')

    parser.add_argument('--model-type',
                        nargs='?',
                        default='FEATHER',
	                help='Fit FEATHER node embedding. Default is FEATHER.')

    return parser.parse_args()
