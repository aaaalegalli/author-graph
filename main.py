# coding: utf-8

# In[421]:

import networkx as nx

#modules
import draw as dr
import readFile as rf
import myFuncs as mf

# In[459]:

# plot subgraph for a confId
def my2a():
    invconf = mf.invertedConf(dataset)
    conf = input("Please enter a conference number: ")
    try:
        conf = int(conf)
        H = G.subgraph(invconf[conf])
        dr.plotGraph(H, 'random')
        dr.b_centrality(H)
        dr.c_centrality(H)
        dr.d_centrality(H)
    except:
        print("Input is not valid")


# In[461]:

# plot the subgraph for a specific authorid and hop distance
def my2b():
    auth = input("Please enter an author id: ")
    d = input("Please enter d: ")
    try:
        auth = int(auth)
        d = int(d)
        subauths = mf.hopDist(auth, d, G)
        H = G.subgraph(subauths)
        dr.plotGraph(H, 'round')
    except:
        print("Input is not valid")


# # 3a

# In[435]:

# find id of aris
# for i in dataset:
#    for j in i['authors']:
#        if j['author'].startswith('aris'):
#            print(i)


# In[436]:

# end node
aris = 256176


# In[464]:

def my3a():
    auth = input("Please enter an author id: ")
    try:
        auth = int(auth)
        r = mf.mydistance(G, auth, aris)
        print(r)
    except:
        print("The input is not valid")


# In[463]:

def my3b():
    inp = input("Please enter Author IDs (max 21) separated by a space: ")
    print("---------------")
    try:
        myAuths = list(map(int, inp.split()))
        if (len(myAuths) <= 21):
            H = G.subgraph(myAuths)
            print(mf.calcGrNr(myAuths, G))
        else:
            print("Number of Authors are bigger than 21")
    except:
        print("Input is not valid")

#read file
dataq = input("Please enter 'r' for reduced dataset or 'f' for full dataset: ")
try:
    if dataq == "f":
        print("Loading full Data...")
        dataset = rf.readFile('full_dblp.json')
    elif dataq == "r":
        print("Loading reduced Data...")
        dataset = rf.readFile('reduced_dblp.json')
    else:
        print("Wrong input, loading reduced Data...")
        dataset = rf.readFile('reduced_dblp.json')
    # create graph
    G = nx.Graph()
    # function for inverted index
    print("Creating inverted Dict...")
    inv = mf.invertedAuth(dataset, G)
    # list with all authorIds
    aids = list(inv.keys())
    # function for connecting nodes
    print("Calculating Similarities...")
    G = mf.jacsim(aids, G, inv)
    ex = 0
    while ex != "q":
        ex = input("Please enter the number of the exercise you want to run (2a, 2b, 3a or 3b) or 'q' for quit: ")
        if ex == "2a":
            my2a()
        elif ex == "2b":
            my2b()
        elif ex == "3a":
            my3a()
        elif ex == "3b":
            my3b()
        elif ex == "q":
            print("Nice to see you")
        else:
            print("Invalid input")
except:
    print("Something went wrong.")