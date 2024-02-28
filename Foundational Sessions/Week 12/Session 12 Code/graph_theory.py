import networkx as nx
import matplotlib.pyplot as plt

def introduce_graph_types():
    """
    Introduces different types of graphs and discusses their characteristics.
    Covers directed, undirected, weighted, unweighted, cyclic, and acyclic graphs.
    Includes visualization of each graph type.
    """
    # Example of a directed graph (digraph)
    # Edges have a direction associated with them.
    # Useful in applications like route mapping, where direction matters.
    digraph = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
    plt.figure(figsize=(5, 4))
    nx.draw_networkx(digraph, arrows=True)
    plt.title("Directed Graph")
    plt.show()

    # Example of an undirected graph
    # Edges have no direction. Useful in networks where direction is irrelevant, like social networks.
    undirected_graph = nx.Graph([(1, 2), (2, 3), (3, 1)])
    plt.figure(figsize=(5, 4))
    nx.draw_networkx(undirected_graph)
    plt.title("Undirected Graph")
    plt.show()

    # Example of a weighted graph
    # Assigns weights to edges, crucial in applications like shortest path problems.
    weighted_graph = nx.Graph()
    weighted_graph.add_edge(1, 2, weight=4.5)
    weighted_graph.add_edge(2, 3, weight=3.2)
    weighted_graph.add_edge(1, 3, weight=2.1)
    edge_labels = nx.get_edge_attributes(weighted_graph, 'weight')
    plt.figure(figsize=(5, 4))
    nx.draw_networkx(weighted_graph)
    nx.draw_networkx_edge_labels(weighted_graph, pos=nx.spring_layout(weighted_graph), edge_labels=edge_labels)
    plt.title("Weighted Graph")
    plt.show()

    # Example of an unweighted graph
    # Does not assign any weight to edges, useful for simpler models.
    unweighted_graph = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])
    plt.figure(figsize=(5, 4))
    nx.draw_networkx(unweighted_graph)
    plt.title("Unweighted Graph")
    plt.show()

    # Example of a cyclic graph
    # Contains cycles, which are paths that start and end at the same node. Common in network routing problems.
    cyclic_graph = nx.Graph([(1, 2), (2, 3), (3, 1)])
    plt.figure(figsize=(5, 4))
    nx.draw_networkx(cyclic_graph)
    plt.title("Cyclic Graph")
    plt.show()

    # Example of an acyclic graph
    # Does not contain any cycles. Key in applications like dependency trees in project management.
    acyclic_graph = nx.Graph([(1, 2), (2, 3), (3, 4)])
    plt.figure(figsize=(5, 4))
    nx.draw_networkx(acyclic_graph)
    plt.title("Acyclic Graph")
    plt.show()

def calculate_node_degree(graph, node):
    """
    Calculates the degree of a given node in a graph.
    The degree is the number of edges connected to the node.
    :param graph: A NetworkX graph object.
    :param node: The node whose degree is to be calculated.
    :return: Degree of the node.
    """
    return graph.degree[node]

def calculate_shortest_path_length(graph, source, target):
    """
    Calculates the shortest path length between two nodes in a graph.
    Uses Dijkstra's algorithm for weighted graphs and breadth-first search for unweighted graphs.
    :param graph: A NetworkX graph object.
    :param source: The starting node.
    :param target: The target node.
    :return: Length of the shortest path.
    """
    try:
        # Using Dijkstra's algorithm for weighted graphs
        if nx.is_weighted(graph):
            path_length = nx.dijkstra_path_length(graph, source, target)
        # Using breadth-first search for unweighted graphs
        else:
            path_length = nx.shortest_path_length(graph, source, target)
        return path_length
    except nx.NetworkXNoPath:
        return "No path exists between the nodes."

def prims_minimum_spanning_tree(graph):
    """
    Implements Prim's algorithm to find the minimum spanning tree of an unweighted, undirected graph.
    The algorithm is a greedy method that builds the spanning tree by adding the smallest edge at each step.
    :param graph: A NetworkX graph object.
    :return: A set of edges constituting the minimum spanning tree.
    """
    # Ensure the graph is undirected
    if not nx.is_directed(graph):
        spanning_tree = set()
        # Select an arbitrary node to start the tree
        start_node = next(iter(graph.nodes))
        # Edges to be considered, starting with those connected to the start node
        edges_to_consider = list(graph.edges(start_node))
        while edges_to_consider:
            # Choose the edge with the smallest number of new nodes (since it's unweighted)
            edge = min(edges_to_consider, key=lambda e: (e not in spanning_tree, e))
            edges_to_consider.remove(edge)
            if edge not in spanning_tree:
                spanning_tree.add(edge)
                # Add new edges to consider, avoiding cycles
                for next_edge in graph.edges(edge[1]):
                    if next_edge not in spanning_tree:
                        edges_to_consider.append(next_edge)
        return spanning_tree
    else:
        return "Prim's algorithm is not applicable to directed graphs."



introduce_graph_types()


