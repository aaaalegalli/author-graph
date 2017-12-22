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

# create inverted index with confId as key and authorIds as values
def invertedPub(dataset):
    invpub = {}
    for i in dataset:
        lst = []
        pid = i["id_publication_int"]
        for author in i["authors"]:
            lst.append(author['author_id'])
        if (pid in invpub.keys()):
            invpub[pid] += lst
        else:
            invpub[pid] = lst
    return invpub



        # In[424]:

 # connect all nodes with the weight calculated by Jaccard similarity
def jacsim(G, inv, invpub):
    pids = list(invpub.keys())
    for n in pids:
        aids = invpub[n]
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
        dij = {}
        q = []
        visited = set()
        lst = G[auth]
        visited.add(auth)
        for i in lst:
            heapq.heappush(q, (lst[i]['weight'], i))
            dij[i] = lst[i]['weight']
        aid = -1
        while q:
            a = heapq.heappop(q)
            w = a[0]
            aid = a[1]
            if aid == end:
                result = "The Distance between " + str(auth) + " and " + str(end) + " is " + str(w)
                break
            visited.add(aid)
            lst = G[aid]  # all connection
            for i in lst:
                if i not in visited:
                    if i in dij.keys():
                        if dij[i] > lst[i]['weight'] + w:
                            for j in q:
                                if j[1] == i:
                                    q.remove(j)
                                    heapq.heappush(q, (lst[i]['weight'] + w, i))
                                    dij[i] = lst[i]['weight'] + w
                                    break
                    else:
                        heapq.heappush(q, (lst[i]['weight'] + w, i))
                        dij[i] = lst[i]['weight'] + w
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
                    dij = {}
                    visited = set()
                    lst = T[i]
                    visited.add(i)
                    for j in lst:
                        heapq.heappush(q, (lst[j]['weight'], j))
                    while q:
                        a = heapq.heappop(q)
                        w = a[0]
                        aid = a[1]
                        if aid == end:
                            result = a
                            subdict[end] = w
                            break
                        visited.add(aid)
                        if aid in dist.keys():
                            if end in dist[aid].keys():
                                heapq.heappush(q, (dist[aid][end] + w, end))
                        else:
                            lst = T[aid]  # all connection
                            for x in lst:
                                if x not in visited:
                                    if x in dij.keys():
                                        if dij[x] > lst[x]['weight'] + w:
                                            for y in q:
                                                if y[1] == x:
                                                    q.remove(y)
                                                    heapq.heappush(q, (lst[x]['weight'] + w, x))
                                                    dij[x] = lst[x]['weight'] + w
                                                    break
                                    else:
                                        heapq.heappush(q, (lst[x]['weight'] + w, x))
                                        dij[x] = lst[x]['weight'] + w
                    heapq.heappush(mydists, result[0])
            dist[i] = subdict
            if len(mydists) > 0:
                gnr[i] = heapq.heappop(mydists)
            else:
                gnr[i] = "No connection"
    return gnr