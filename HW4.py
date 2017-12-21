
# coding: utf-8

# In[421]:

import json
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import warnings
warnings.filterwarnings("ignore")


# # Part 1

# In[422]:

#function for reading files
def readFile(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    dataset = json.loads(data)
    return dataset


# In[423]:

#create inverted index with authorId as key and pubIds as values
#create all nodes for authors
#create dictionary with authorId as label and name as key
def invertedAuth(dataset):
    inv = {}
    labels={}
    for i in dataset:  
        for author in i["authors"]:
            aid = author['author_id']
            labels[aid]=author['author']
            G.add_node(aid, label= True)
            if(aid in inv.keys()):
                inv[aid]+= [i['id_publication_int']]
            else:
                inv[aid] = [i['id_publication_int']]
    return inv


# In[424]:

#connect all nodes with the weight calculated by Jaccard similarity
def jacsim(aids):
    for i in range(len(aids)-1):
        x = aids[i]
        for j in range(i+1, len(aids)):
            y = aids[j]
            inter = set(inv[x]).intersection(set(inv[y]))
            if len(inter)>0:
                a = len(inter)
                b = len(set(inv[x]).union(set(inv[y])))
                w = 1-a/b
                G.add_edge(x,y,weight=w)


# In[425]:

#read file
print("Loading Data...")
dataset = readFile('reduced_dblp.json')
#dataset = readFile('full_dblp.json')
#create graph
G=nx.Graph()
#function for inverted index
print("Creating Dict inv...")
inv = invertedAuth(dataset)
#list with all authorIds
aids = list(inv.keys())
#function for connecting nodes
print("Calculating Similarities...")
jacsim(aids)



# In[426]:

#plot the graph
#plt.clf()
#nx.draw(G, pos=nx.spring_layout(G), node_size=35, linewidths= 0.3, width=0.1 )
#plt.show()


# # 2a

# In[427]:

#create inverted index with confId as key and authorIds as values
def invertedAuth(dataset):
    invconf = {}
    for i in dataset:
        lst = []
        cid = i['id_conference_int']
        for author in i["authors"]:
            lst.append(author['author_id'])
        if(cid in invconf.keys()):
            invconf[cid]+=lst 
        else:   
            invconf[cid] = lst
    return invconf


# In[454]:

#function for plotting smaller graphs
def plotGraph(Graph, x):
    d=nx.degree(H)
    dict1={}
    for i in d.values():
    if 51<=i<=100:
        dict1[i] = 'cyan'
    if 21<=i<=50:
        dict1[i] = 'yellow'
    if 11<=i<=20:
        dict1[i] = 'pink'
    if i >= 10:
        dict1[i] = 'black'
    if 5<i<=9:
        dict1[i] = 'green'
    if 3<=i<=5:
        dict1[i] = 'red'
    if i == 2:
        dict1[i] = 'purple'
    if i == 1 or i == 0:
        dict1[i] = 'orange'
    
    plt.figure(figsize=(20,10))
    plt.clf()
    if x == "random":
        nx.draw(H,  pos=nx.random_layout(H), node_list=d.keys(), node_size=[v*50 for v in d.values()], 
            node_color= [dict1[i] for i in d.values()], linewidths= 0.3, width=0.1)
    else:
        nx.draw(H,  pos=nx.spring_layout(H), node_list=d.keys(), node_size=[v*50 for v in d.values()], 
            node_color= [dict1[i] for i in d.values()], linewidths= 0.3, width=0.1)
        
    plt.show()


# In[459]:

#plot subgraph for a confId
def my2a():
    invconf = invertedAuth(dataset)
    conf = input("Please enter a conference number: ")
    try:
        conf = int(conf)
        H = G.subgraph(invconf[conf])
        plotGraph(H)
    except:
        print("Input is not valid")


# In[430]:

#betweenness centrality
#bc=nx.betweenness_centrality(H)
#bc


# In[431]:

#cc=nx.closeness_centrality(H)
#cc


# In[432]:

#dc=nx.degree_centrality(H)
#dc


# # 2b

# In[433]:

#creates a list with all nodes in the hopdistance d
def hopDist(auth, d):
    hopdict = {}
    hopdict[0] = [auth]
    subauths = [auth]
    for i in range(1,d+1):
        mylist = hopdict[i-1]
        lst = []
        for j in mylist: 
            lst += list(G[j].keys())
        lst2 = []
        for x in lst:
            if x not in subauths:
                lst2 += [x]
        if len(lst2)==0:
            break
        hopdict[i] = lst2
        subauths += lst2
    return subauths


# In[461]:

#plot the subgraph for a specific authorid and hop distance
def my2b():
    auth = input("Please enter an author id: ")
    d = input("Please enter d: ")
    try:
        auth = int(auth)
        d = int(d)
        subauths = hopDist(auth, d)
        H = G.subgraph(subauths)
        plotGraph(H)
    except:
        print("Input is not valid")


# In[170]:

#plt.clf()
#nx.draw(H, pos=nx.spring_layout(H), arrows= True, with_labels= True, node_size=100, linewidths= 0.3, width=0.1)
#plt.show()


# # 3a

# In[435]:

#find id of aris
#for i in dataset:
#    for j in i['authors']:
#        if j['author'].startswith('aris'):
#            print(i)


# In[436]:

#end node
aris = 256176


# In[437]:

#dijkstra function
def mydistance(G, auth, end):
    if nx.has_path(G,auth,end):
        q = []
        visited = set()
        lst = G[auth]
        visited.add(auth)
        for i in lst:
                heapq.heappush(q, ( lst[i]['weight'], i))
        while q:
            a = heapq.heappop(q)
            w = a[0]
            aid = a[1]
            if aid == end:
                result = "The Distance between "+str(auth)+" and "+str(end)+" is "+str(w)
            visited.add(aid)
            lst = G[aid] #all connection
            for i in lst:
                if i not in visited:
                    isinside = False
                    for j in q: 
                        if j[1] == i:
                            isinside = True
                            if j[0] > lst[i]['weight']+w:
                                q.remove(j)
                                heapq.heappush(q, (lst[i]['weight']+w, i))
                            break
                    if isinside == False:
                        heapq.heappush(q, (lst[i]['weight']+w, i))
    else:
        result = "There is no path between "+str(auth)+" and "+str(end)
    return result


# In[464]:

def my3a():
    auth = input("Please enter an author id: ")
    try:
        auth = int(auth)
        r = mydistance(G, auth, aris)
        print(r)
    except:
        print("The input is not valid")



# # 3b

# In[440]:

#calculte the groupNumbers
def calcGrNr(mlst, T):
    dist = {}
    gnr = {}
    for i in T:
        mydists = []
        subdict = {}
        if i not in mlst:
            for end in mlst:
                if nx.has_path(T,i,end):
                    q = []
                    visited = set()
                    lst = T[i]
                    visited.add(i)
                    for j in lst:
                            heapq.heappush(q, ( lst[j]['weight'], j))
                    aid = 0
                    while aid != end:
                        a = heapq.heappop(q)
                        w = a[0]
                        aid = a[1]
                        if aid == end:
                            result = a
                            subdict[end]=w
                        visited.add(aid)
                        if aid in dist.keys():
                            if end in dist[aid].keys():
                                heapq.heappush(q, (dist[aid][end]+w, end))
                        else:
                            lst = T[aid] #all connection
                            for x in lst:
                                if x not in visited:
                                    isinside = False
                                    for y in q: 
                                        if y[1] == x:
                                            isinside = True
                                            if y[0] > lst[x]['weight']+w:
                                                q.remove(y)
                                                heapq.heappush(q, (lst[x]['weight']+w, x))
                                            break
                                    if isinside == False:
                                        heapq.heappush(q, (lst[x]['weight']+w, x))
                
                    heapq.heappush(mydists, result[0])                   
            dist[i] = subdict
            if len(mydists)>0:
                gnr[i] = heapq.heappop(mydists)
            else:
                gnr[i] = "No connection"
    return gnr


# In[463]:

def my3b():
    inp = input("Please enter Author IDs (max 21) separated by a space: ")
    print("---------------")
    try:    
        myAuths = list(map(int, inp.split()))
        if(len(myAuths)<=21):
            H = G.subgraph(myAuths)
            print(calcGrNr(myAuths,G))
        else:
            print("Number of Authors are bigger than 21")
    except:
        print("Input is not valid")
    
    
    
#test = [560214, 461659,490729,256176]
#test = [255206, 255208, 255207, 16585]


# In[471]:

#ask for next operation
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



