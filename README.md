# Group11

## Homework4 ADM

In this project we carry out information from Computer Scientists network, using the DBLP dataset.
Two datasets (json file) were provided:
- [reduced network](www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/reduced_dblp.json.zip)
- [entire network](http://www.diag.uniroma1.it/~fazzone/Teaching/AMD_2017/full_dblp.json.zip)

To let the code run, these libraries are needed:
```python
import json
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import warnings
```
Json files and all .py files have to be in the same folder. The files in the midWork folder can be omitted.

To run the code, write `python main.py` in the prompt and follow the instructions.
At the beginning, choose the file you want to use (r for reduced, f for full).
The program will automatically create a graph whose nodes are the authors; two of them are connected if they share one publication at least. Edges are weighted according to jaccard similarity. 

The functions used are:

- `readFile(file)`
It takes as input the file name (json file) as a string and return the dataset.
- `invertedAuth(dataset, graph)`
It takes as input the whole dataset and a graph and returns the inverted index with authors as keys and their publications as values. Furthermore it adds nodes to the graph, one for each authors.
- `jacsim(aids, graph, invertedAuth)`
It takes as input the author ids (list), a graph and the results of `invertedAuth` (dictionary) function, calculates jaccard similarity, sets the weight of each link between nodes that are connected and returns the graph.

Then, choose which exercise you want to run (2a, 2b, 3a or 3b).

### 2A
#### You are asked to choose a conference, it returns a subgraph that contains authors who published at that conference at least once

The functions used are:

- `invertedConf(dataset)`
It takes as input the whole dataset and returns the inverted index with authors as keys and their publications as values.
- `b_centrality(graph)`
It calculates and returns the betweeness centrality (as a list) of the nodes of the graph given as input.
- `c_centrality(graph)`
It calculates and returns the closeness centrality (as a list) of the nodes of the graph given as input.
- `d_centrality(graph)`
It calculates and returns the degree centrality (as a list) of the nodes of the graph given as input.

### 2B
#### You are asked to select an author id and an integer d, it returns and visualizes the subgraph induced by the nodes that have a number of edges at most equal to d as distance from the author selected (hop distance)

The functions used are:

- `hopDist(aid, d)`
- `plotGraph(graph, shape)`

### 3A
#### You are asked to choose an author, it returns the weight of shortest path from the author in input to Aris

The functions used are:

- `mydistance(graph, start, end)`

### 3B
#### You are asked to choose a subset of authors id (at most 21), it returns for each node of the graph its GroupNumber (generalized version of Erdös number)

The functions used are:

- `calcGrNr(aids, graph)`
