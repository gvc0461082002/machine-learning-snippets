import networkx as nx
import matplotlib.pyplot as plt
import math
#initialize a direct graph
G = nx.DiGraph()
#read edges from test.link
with open('test.link') as f:
    lines = f.read().splitlines()
    #print(type(lines))
    #print(lines[0].rsplit('\t'))
    #print(stringarray)
for lineitem in lines:
    edgesitem = lineitem.rsplit('\t')
    G.add_edge(edgesitem[1],edgesitem[0])

print(G.node())


# Need to create a layout when doing
# separate calls to draw nodes and edges
options = {
   # 'node_color': 'blue',
    #'node_size': 100,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 6,
}
#pos = nx.shell_layout(G)
pos = nx.spring_layout(G,k=5/math.sqrt(G.order()) )

#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size = 500)
#nx.draw_networkx_labels(G, pos)
#nx.draw_networkx_edges(G, pos, arrows=True,**options)
nx.draw(G, pos, node_size=1200, node_color='lightblue',linewidths=0.25, font_size=10, font_weight='bold', with_labels=True, dpi=1000,)

fig = plt.figure(figsize=(20,15))

plt.show()
