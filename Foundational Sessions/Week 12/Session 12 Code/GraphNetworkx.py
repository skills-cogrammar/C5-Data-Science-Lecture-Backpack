import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
eg_graph = nx.Graph()

# Add a node to the graph
eg_graph.add_node("a")

# Add a list of nodes to the graph
nodes = ["b", "c", "d", "e"]

# You can also add node atrributes to each node using the form:
# ("b", {colour: "blue"})

# Add an edge to the node
eg_graph.add_edge("a", "b")

# Edges can be added after edge creation or at the same time
eg_graph.add_edge("a", "c", weight=4)
eg_graph["a"]["b"]["weight"] = 10

# Multiple edges and weights can be added at once
eg_graph.add_edges_from([("b", "d", {"weight": 3}), 
                         ("d", "c", {"weight": 7}), 
                         ("e", "d", {"weight": 2})])

# We can visualise the Graph like this
nx.draw(eg_graph, with_labels=True, font_weight='bold')
plt.figure()

# To create a directed graph, we use a different constructor
eg_digraph = nx.DiGraph()

# Adding nodes and edges can be done the same way
# We can also import the edges and nodes from another graph
eg_digraph.add_nodes_from(eg_graph)
eg_digraph.add_edges_from(eg_graph.edges)

# Let's visualise the graph
nx.draw(eg_digraph, with_labels=True, font_weight='bold')
plt.show()

