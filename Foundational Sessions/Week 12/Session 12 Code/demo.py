from graph_theory import introduce_graph_types, calculate_node_degree, calculate_shortest_path_length, prims_minimum_spanning_tree
from social_network import SocialNetwork
import networkx as nx

# Demonstrate graph theory concepts
def demonstrate_graph_theory():
    print("Introducing Graph Types:")
    introduce_graph_types()  # This will visualize different graph types

    # Create a sample graph for demonstration
    graph = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
    print("\nCalculating Node Degrees:")
    for node in graph.nodes():
        print(f"Degree of node {node}: {calculate_node_degree(graph, node)}")

    print("\nCalculating Shortest Path Length:")
    print(f"Shortest path length from 1 to 4: {calculate_shortest_path_length(graph, 1, 4)}")

    print("\nDemonstrating Prim's Algorithm:")
    mst_edges = prims_minimum_spanning_tree(graph)
    print(f"Edges in the minimum spanning tree: {mst_edges}")

# Demonstrate social network simulation
def demonstrate_social_network():
    sn = SocialNetwork()

    # Adding members to the social network
    for member in ['Alice', 'Bob', 'Charlie', 'Daisy', 'Eva']:
        sn.add_member(member)

    # Creating connections between members
    connections = [('Alice', 'Bob'), ('Bob', 'Charlie'), ('Charlie', 'Daisy'), ('Daisy', 'Eva'), ('Eva', 'Alice')]
    for connection in connections:
        sn.add_connection(*connection)

    print("\nSocial Network Simulation:")
    print(f"Total members in the network: {sn.total_members()}")
    print(f"Shortest connection path from Alice to Daisy: {sn.shortest_connection_path('Alice', 'Daisy')}")
    sn.visualize_network()

# Run the demonstrations
demonstrate_graph_theory()
demonstrate_social_network()
