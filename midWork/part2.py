
# coding: utf-8

# In[ ]:

#2A


# In[ ]:

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


# In[ ]:

#function for plotting smaller graphs
def plotGraph(Graph):
    plt.clf()
    nx.draw(Graph,  with_labels=True, node_size=100, linewidths= 0.3, width=0.1)
    #nx.draw_networkx_labels(H, pos=nx.spring_layout(H),labels=labels, font_size=16)
    plt.show()


# In[ ]:

#plot subgraph for a confId
invertedAuth(dataset)
conf = input("Please enter a conference number: ")
try:
    conf = int(conf)
    H = G.subgraph(invconf[conf])
    plotGraph(H)
except:
    print("Input is not valid")


# In[ ]:

bc=nx.betweenness_centrality(H)
bc


# In[ ]:

cc=nx.closeness_centrality(H)
cc


# In[ ]:

dc=nx.degree_centrality(H)
dc


# In[ ]:

#2B


# In[ ]:

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


# In[ ]:

#plot the subgraph for a specific authorid and hop distance
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

