FEATHER
============================================
The reference implementation of "Characteristic Functions on Graphs: Birds of a Feather from Statistical Descriptors to Parametric Models."
<p align="center">
  <img width="800" src="feather.jpg">
</p>

### Abstract

<p align="justify">
In this paper, we propose a flexible notion of characteristic functions defined on graph vertices to describe the distribution of vertex features at multiple scales. We describe FEATHER a computationally efficient algorithm to calculate a specific variant of these characteristic functions where the probability weights of the characteristic function are defined by the transition probabilities of truncated random walks. We argue, that features extracted by this procedure are useful for node level machine learning tasks. We discuss that the pooling of these node representations results in compact descriptors of graphs which can serve as features for graph classification algorithms. We analytically prove that FEATHER describes isomorphic graphs with the same representation and exhibits robustness to data corruption. Using the node feature characteristic functions we define parametric models where evaluation points of the functions are learned parameters of supervised classifiers. Our experiments on a number of real world large datasets show that our proposed algorithms create high quality node and graph representations, perform transfer learning efficiently, robust to hyperparameter changes and scale linearly with the input size.</p>

The datasets are also available on [SNAP](http://snap.stanford.edu/).

The model is now also available in the package [Karate Club](https://github.com/benedekrozemberczki/karateclub).

This repository provides the reference implementation for FEATHER as described in the paper:
> Characteristic Functions on Graphs: Birds of a Feather from Statistical Descriptors to Parametric Models.
> [Benedek Rozemberczki](http://homepages.inf.ed.ac.uk/s1668259/) and [Rik Sarkar](https://homepages.inf.ed.ac.uk/rsarkar/).
> 2020.


### Table of Contents

1. [Citing](#citing)  
2. [Requirements](#requirements)
3. [Options](#options) 
4. [Examples](#examples)

### Citing

If you find MUSAE useful in your research, please consider citing the following paper:
```bibtex
>@misc{rozemberczki2020feather,    
       title = {Characteristic Functions on Graphs: Birds of a Feather from Statistical Descriptors to Parametric Models},   
       author = {Benedek Rozemberczki and Rik Sarkar},   
       year = {2020}
       }
```
### Requirements
The codebase is implemented in Python 3.5.2. package versions used for development are just below.
```
networkx          2.4
tqdm              4.28.1
numpy             1.15.4
pandas            0.23.4
texttable         1.5.0
scipy             1.1.0
argparse          1.1.0
```
### Options

Learning of the embedding is handled by the `src/main.py` script which provides the following command line arguments.

#### Input and output options
```
  --graph-input      STR   Input edge list csv.     Default is `input/edges/chameleon_edges.csv`.
  --features-input   STR   Input features json.     Default is `input/features/chameleon_features.json`.
  --output           STR   Embedding output path.   Default is `output/chameleon_embedding.csv`.
  --log              STR   Log output path.         Default is `logs/chameleon.json`.
```
#### Model options
```
  --model                 STR        Pooled or multi-scla model (AE/MUSAE).       Default is `musae`.
  --approximation-order   INT        Matrix powers approximated.                  Default is 3.
  --down-sampling         FLOAT      Length of random walk per source.            Default is 0.001.
```

### Examples

Training a MUSAE model for a 10 epochs.
```sh
$ python src/main.py --epochs 10
```
Changing the dimension size.
```sh
$ python src/main.py --dimensions 32
```
