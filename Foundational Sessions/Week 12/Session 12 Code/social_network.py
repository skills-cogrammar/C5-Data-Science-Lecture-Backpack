import networkx as nx
import matplotlib.pyplot as plt

class SocialNetwork:
    """
    Simulates a social network using graph theory concepts.
    Supports addition of new unique members and finding the shortest path between members.
    """
    def __init__(self):
        self.network = nx.Graph()

    def add_member(self, member_name):
        """
        Adds a new unique member to the social network.
        :param member_name: Name of the member to add.
        """
        if member_name not in self.network:
            self.network.add_node(member_name)

    def add_connection(self, member1, member2):
        """
        Adds a connection (edge) between two members in the social network.
        :param member1: Name of the first member.
        :param member2: Name of the second member.
        """
        self.network.add_edge(member1, member2)

    def total_members(self):
        """
        Reports the total number of members in the social network.
        :return: Total number of members.
        """
        return len(self.network.nodes)

    def shortest_connection_path(self, member1, member2):
        """
        Finds the shortest path (minimum number of connections) between two members.
        :param member1: Name of the first member.
        :param member2: Name of the second member.
        :return: List representing the shortest path or a message if no path exists.
        """
        try:
            return nx.shortest_path(self.network, member1, member2)
        except nx.NetworkXNoPath:
            return "No connection path exists between these members."

    def visualize_network(self):
        """
        Visualizes the social network graph.
        """
        plt.figure(figsize=(8, 6))
        nx.draw_networkx(self.network, with_labels=True, node_color='skyblue', edge_color='gray')
        plt.title("Social Network Graph")
        plt.show()

