import json
import networkx as nx
import matplotlib.pyplot as plt

#processing json file
f = open('reduced_dblp.json', 'r')
data = f.read()
f.close()

dataset = json.loads(data)

#creating graph
G=nx.Graph()

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

inv

aids = list(inv.keys())

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

plt.clf()
nx.draw(G, pos=nx.spring_layout(G), node_size=35, linewidths= 0.3, width=0.1 )
plt.show()

#given a conference, creating the subgraph

conf = input("Please enter a conference number: ")
try:
    conf = int(conf)
except:
    print("Input is not a number")


invconf = {}
for i in dataset:
    lst = []
    #dicty={}
    cid = i['id_conference_int']
    for author in i["authors"]:
        #dicty[author['author_id']]=author['author']
        lst.append(author['author_id'])
    if(cid in invconf.keys()):
        invconf[cid]+=lst 
    else:   
        invconf[cid] = lst

H = G.subgraph(invconf[conf])

plt.clf()
#nx.draw(H,  with_labels=True, node_size=100, linewidths= 0.3, width=0.1)
nx.draw_networkx_labels(H, pos=nx.spring_layout(G),labels=labels, font_size=16)
plt.show()

#computing some measures

#betweenness centrality
bc=nx.betweenness_centrality(H)


cc=nx.closeness_centrality(H)


dc=nx.degree_centrality(H)


#plot

### 2b
#subgraph with hop distance

auth = input("Please enter an author id: ")
try:
    auth = int(auth)
except:
    print("Input is not a number")
d = input("Please enter d: ")
try:
    d = int(d)
except:
    print("Input is not a number")


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

H = G.subgraph(subauths)

plt.clf()
nx.draw(H, pos=nx.spring_layout(H), arrows= True, with_labels= True, node_size=100, linewidths= 0.3, width=0.1)
plt.show()

