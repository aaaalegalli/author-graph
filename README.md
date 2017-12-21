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
Json files and HW4.py have to be in the same folder.

To run the code, write `python HW4.py` in the prompt and follow the instruction
- Choose the file you want to use (r for reduced, f for full)
The program will automatically create a graph whose nodes are the authors; two of them are connected if they share one publications at least. Edges is weighted according to jaccard similarity using `jacsim` function that takes as input the author ids and returns a graph.
- Choose which exercise you want to run (2a, 2b, 3a or 3b)

### 2A
#### You are asked to choose a conference, it returns a subgraph that contains authors who published at that conference at least once

The functions used are:
```python
invertedConf(dataset)
b_centrality(graph)
c_centrality(graph)
d_centrality(graph)
```

### 2B
#### You are asked to select an author id and an integer d, it returns and visualizes the subgraph induced by the nodes that have a number of edges at most equal to d as distance from the author selected (hop distance)

The functions used are:
```python
hopDist(aid, d)
plotGraph(graph, shape)

```

### 3A
#### You are asked to choose an author, it returns the weight of shortest path from the author in input to Aris

The functions used are:
```python
mydistance(graph, start, end)
```

### 3B
#### You are asked to choose a subset of authors id (at most 21), it returns for each node of the graph its GroupNumber (generalized version of Erdös number)

The functions used are:
```python
calcGrNr(aids, graph)
```
