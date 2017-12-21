import matplotlib.pyplot as plt
import networkx as nx
import warnings
warnings.filterwarnings("ignore")


# In[430]:
#centralities
def b_centrality(Graph):
    bc = nx.betweenness_centrality(Graph)
    dic = {}
    for k, v in bc.items():  # dictionary given by the function for bc, cc, dc
        if v not in dic.keys():
            dic[v] = 1
        else:
            dic[v] += 1

    ax = range(len(dic))
    ay = [i for i in dic.values()]
    plt.figure(figsize=(20, 10))
    plt.bar(ax, ay)
    plt.xticks(ax, sorted(('%3f' % elem for elem in dic.keys())), rotation=90)
    plt.title('Betweenness Centrality')
    plt.xlabel('values')
    plt.ylabel('frequency')
    plt.show()


def c_centrality(Graph):
    cc = nx.closeness_centrality(Graph)
    dic = {}
    for k, v in cc.items():  # dictionary given by the function for bc, cc, dc
        if v not in dic.keys():
            dic[v] = 1
        else:
            dic[v] += 1

    ax = range(len(dic))
    ay = [i for i in dic.values()]
    plt.figure(figsize=(20, 10))
    plt.bar(ax, ay)
    plt.xticks(ax, sorted(('%3f' % elem for elem in dic.keys())), rotation=90)
    plt.title('Closeness Centrality')
    plt.xlabel('values')
    plt.ylabel('frequency')
    plt.show()

def d_centrality(Graph):
    dc = nx.degree_centrality(Graph)
    dic = {}
    for k, v in dc.items():  # dictionary given by the function for bc, cc, dc
        if v not in dic.keys():
            dic[v] = 1
        else:
            dic[v] += 1

    ax = range(len(dic))
    ay = [i for i in dic.values()]
    plt.figure(figsize=(20, 10))
    plt.bar(ax, ay)
    plt.xticks(ax, sorted(('%3f' % elem for elem in dic.keys())), rotation=90)
    plt.title('Degree Centrality')
    plt.xlabel('values')
    plt.ylabel('frequency')
    plt.show()


# In[454]:

# function for plotting smaller graphs
def plotGraph(Graph, x):
    d = nx.degree(Graph)
    dict1 = {}
    for i in d.values():
        if 51 <= i <= 100:
            dict1[i] = 'cyan'
        elif 21 <= i <= 50:
           dict1[i] = 'yellow'
        elif 11 <= i <= 20:
            dict1[i] = 'pink'
        elif 5 < i <= 10:
            dict1[i] = 'green'
        elif 3 <= i <= 5:
            dict1[i] = 'red'
        elif i == 2:
            dict1[i] = 'purple'
        else:
            dict1[i] = 'orange'

    plt.figure(figsize=(20, 10))
    plt.clf()
    if x == "random":
        nx.draw(Graph, pos=nx.random_layout(Graph), node_list=d.keys(), node_size=[v * 50 for v in d.values()],
                node_color=[dict1[i] for i in d.values()], linewidths=0.3, width=0.1)
    else:
        nx.draw(Graph, pos=nx.spring_layout(Graph), node_list=d.keys(), node_size=[v * 50 for v in d.values()],
                node_color=[dict1[i] for i in d.values()], linewidths=0.3, width=0.1)

    plt.show()

