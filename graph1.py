import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_node('A', weight=3)
G.add_node('B', weight=3)
G.add_node('C', weight=4)
G.add_node('D', weight=6)
G.add_node('E', weight=5)
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('A', 'D')
G.add_edge('B', 'E')
G.add_edge('C', 'E')
G.add_edge('D', 'E')
labels = {n: str(n) + '     ' + str(G.nodes[n]['weight']) for n in G.nodes}
colors = [G.nodes[n]['weight'] for n in G.nodes]
nx.draw(G, with_labels=True, labels=labels, node_color=colors)

plt.show()          