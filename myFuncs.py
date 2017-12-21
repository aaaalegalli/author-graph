import networkx as nx
import heapq

# In[423]:

# create inverted index with authorId as key and pubIds as values
# create all nodes for authors
# create dictionary with authorId as label and name as key
def invertedAuth(dataset, G):
    inv = {}
    labels = {}
    for i in dataset:
        for author in i["authors"]:
            aid = author['author_id']
            labels[aid] = author['author']
            G.add_node(aid, label=True)
            if (aid in inv.keys()):
                inv[aid] += [i['id_publication_int']]
            else:
                inv[aid] = [i['id_publication_int']]
    return inv


# In[424]:

# connect all nodes with the weight calculated by Jaccard similarity
def jacsim(aids, G, inv):
    for i in range(len(aids) - 1):
        x = aids[i]
        for j in range(i + 1, len(aids)):
            y = aids[j]
            inter = set(inv[x]).intersection(set(inv[y]))
            if len(inter) > 0:
                a = len(inter)
                b = len(set(inv[x]).union(set(inv[y])))
                w = 1 - a / b
                G.add_edge(x, y, weight=w)
    return G


# In[427]:

# create inverted index with confId as key and authorIds as values
def invertedConf(dataset):
    invconf = {}
    for i in dataset:
        lst = []
        cid = i['id_conference_int']
        for author in i["authors"]:
            lst.append(author['author_id'])
        if (cid in invconf.keys()):
            invconf[cid] += lst
        else:
            invconf[cid] = lst
    return invconf

# In[433]:

# creates a list with all nodes in the hopdistance d
def hopDist(auth, d, G):
    hopdict = {}
    hopdict[0] = [auth]
    subauths = [auth]
    for i in range(1, d + 1):
        mylist = hopdict[i - 1]
        lst = []
        for j in mylist:
            lst += list(G[j].keys())
        lst2 = []
        for x in lst:
            if x not in subauths:
                lst2 += [x]
        if len(lst2) == 0:
            break
        hopdict[i] = lst2
        subauths += lst2
    return subauths

# In[437]:

# dijkstra function
def mydistance(G, auth, end):
    if nx.has_path(G, auth, end):
        q = []
        visited = set()
        lst = G[auth]
        visited.add(auth)
        for i in lst:
            heapq.heappush(q, (lst[i]['weight'], i))
        while q:
            a = heapq.heappop(q)
            w = a[0]
            aid = a[1]
            if aid == end:
                result = "The Distance between " + str(auth) + " and " + str(end) + " is " + str(w)
            visited.add(aid)
            lst = G[aid]  # all connection
            for i in lst:
                if i not in visited:
                    isinside = False
                    for j in q:
                        if j[1] == i:
                            isinside = True
                            if j[0] > lst[i]['weight'] + w:
                                q.remove(j)
                                heapq.heappush(q, (lst[i]['weight'] + w, i))
                            break
                    if isinside == False:
                        heapq.heappush(q, (lst[i]['weight'] + w, i))
    else:
        result = "There is no path between " + str(auth) + " and " + str(end)
    return result

# In[440]:

# calculte the groupNumbers
def calcGrNr(mlst, T):
    dist = {}
    gnr = {}
    for i in T:
        mydists = []
        subdict = {}
        if i not in mlst:
            for end in mlst:
                if nx.has_path(T, i, end):
                    q = []
                    visited = set()
                    lst = T[i]
                    visited.add(i)
                    for j in lst:
                        heapq.heappush(q, (lst[j]['weight'], j))
                    aid = 0
                    while aid != end:
                        a = heapq.heappop(q)
                        w = a[0]
                        aid = a[1]
                        if aid == end:
                            result = a
                            subdict[end] = w
                        visited.add(aid)
                        if aid in dist.keys():
                            if end in dist[aid].keys():
                                heapq.heappush(q, (dist[aid][end] + w, end))
                        else:
                            lst = T[aid]  # all connection
                            for x in lst:
                                if x not in visited:
                                    isinside = False
                                    for y in q:
                                        if y[1] == x:
                                            isinside = True
                                            if y[0] > lst[x]['weight'] + w:
                                                q.remove(y)
                                                heapq.heappush(q, (lst[x]['weight'] + w, x))
                                            break
                                    if isinside == False:
                                        heapq.heappush(q, (lst[x]['weight'] + w, x))

                    heapq.heappush(mydists, result[0])
            dist[i] = subdict
            if len(mydists) > 0:
                gnr[i] = heapq.heappop(mydists)
            else:
                gnr[i] = "No connection"
    return gnr