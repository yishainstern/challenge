import networkx as nx
G = nx.read_edgelist("graph.csv", delimiter=",", data=[("weight", int)],nodetype=int)
print(G.edges(data=True));