# Python Implementation of Weighted, Undirected/Directed Graph

class Node:
    # Constructor of a node with edges defined
    # Edges are a dictionary with a key of the destination node (can be empty)
    # And a value of the weight of the edge
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges
    
    # Add an edge to a node
    def add_edge(self, dest_node, weight):
        self.edges[dest_node] = weight


class Graph:
    # Constructor for a graph with no nodes
    def __init__(self):
        self.nodes = []

    # Add disconnected node to the graph
    def add_node(self, node):
        self.nodes.append(Node(node, {}))
    
    # Add an edge to the graph from a source node to a destination
    def add_edge(self, source, dest, weight):
        source_index = "not found"
        dest_index = "not found"

        for i, node in enumerate(self.nodes):
            if node.label == source:
                source_index = i
            if node.label == dest:
                dest_index = i

            if (source_index != "not found") and (dest_index != "not found"):
                break
        
        if (source_index == "not found") or (dest_index == "not found"):
            return 0
        else:
            self.nodes[source_index].add_edge(self.nodes[dest_index], weight)

    def print_graph(self):
        for node in self.nodes:
            print("".join(["(",node.label, ")"]))

            edges_string = []
            for edge in node.edges:
                edges_string.append("".join(["-------  ", 
                                             str(node.edges[edge]), 
                                             "  -------  (", 
                                             edge.label, 
                                             ")"]))
            print(", ".join(edges_string))

eg_graph = Graph()
nodes = ["a", "b", "c", "d"]
for node in nodes:
    eg_graph.add_node(node)

edges = [["a", "b"], ["a", "c"], ["b", "d"], ["d", "c"]]
weights = [10, 4, 3, 7]
for i, edge in enumerate(edges):
    eg_graph.add_edge(edge[0], edge[1], weights[i])

eg_graph.print_graph()
            



        


                


    