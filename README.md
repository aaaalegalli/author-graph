
# Group11

## HW - Algorithmic Methods of Data Mining

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

This python program is organized in four modules: 
- `main.py`
- `readFile.py` It contains the functions to read json files
- `myFuncs.py` It contains all the functions needed to calculate indexes and creating graphs
- `draw.py` It contains the functions needed to plot graphs

To run the code, write `python main.py` in the prompt and follow the instructions.
At the beginning, choose the file you want to use (r for reduced, f for full).
The program will automatically create a graph whose nodes are the authors; two of them are connected if they share one publication at least. Edges are weighted according to jaccard similarity. 

The functions used are:

- `readFile(file)`
(readFile.py) It takes as input the file name (json file) as a string and return the dataset.
- `invertedAuth(dataset, graph)`
(myFuncs.py) It takes as input the whole dataset and a graph and returns the inverted index with authors as keys and their publications as values. Furthermore it adds nodes to the graph, one for each authors.
- `invertedPub(dataset)`
(myFuncs.py) It takes as input the whole dataset and returns the inverted index with publication id as keys and the authors as values.
- `jacsim(aids, graph, invertedAuth)`
(myFuncs.py) It takes as input the author ids (list), a graph and the results (dictionary) of `invertedAuth` function, calculates jaccard similarity, sets the weight of each link between nodes that are connected and returns the graph.

Then, choose which exercise you want to run (2a, 2b, 3a or 3b).

### 2A
#### You are asked to choose a conference, it returns a subgraph that contains authors who published at that conference at least once

The functions used are:

- `invertedConf(dataset)`
(myFuncs.py) It takes as input the whole dataset and returns the inverted index with conference id as keys and the authors as values.
- `b_centrality(graph)`
(draw.py) It calculates betweeness centrality of the nodes of the graph given as input and plots an histogram of the index calculated.
- `c_centrality(graph)`
(draw.py) It calculates closeness centrality of the nodes of the graph given as input and plots an histogram of the index calculated.
- `d_centrality(graph)`
(draw.py) It calculates degree centrality of the nodes of the graph given as input and plots an histogram of the index calculated.

### 2B
#### You are asked to select an author id and an integer d, it returns and visualizes the subgraph induced by the nodes that have a number of edges at most equal to d as distance from the author selected (hop distance)

The functions used are:

- `hopDist(aid, d)`
(myFuncs.py) It takes as input the id of one author and an integer d and returns a list of the subset of author ids which have hop distance at most equal to d.
- `plotGraph(graph, shape)`
(draw.py) It takes as input the entire graph and the shape of the plot (as a string, random or round) you want as result. It plots the subgraph of the `hopDist` results.

### 3A
#### You are asked to choose an author, it returns the weight of shortest path from the author in input to Aris

The functions used are:

- `mydistance(graph, start, end)`
(myFuncs.py) It calculates the shortest path (and returns the weight of it) between two authors (start and end as ids) inside the graph according to the Djikstra algorithm. In this case end is equal to the Aris id.

### 3B
#### You are asked to choose a subset of authors id (at most 21), it returns for each node of the graph its GroupNumber (generalized version of Erdös number)

The functions used are:

- `calcGrNr(aids, graph)`
(myFuncs.py) Given a graph and a subset of nodes (list of author ids), returns the GroupNumber of each node in the graph. It is the minimum shortest path between the node itself and the subset's nodes.
