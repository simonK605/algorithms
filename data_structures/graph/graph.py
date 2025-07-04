"""
Graph Data Structure
---------------------
This file provides a basic graph structure with support for:
- Adding vertices and edges
- Directed or undirected graphs
- Retrieving neighbors
- Printing the full graph

Internally uses an adjacency list representation.

Time Complexity:
- Add Vertex: O(1)
- Add Edge: O(1)
- Get Neighbors: O(1)
- Print Graph: O(V + E)
"""

from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def get_neighbors(self, v):
        return self.adj_list[v]

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")


if __name__ == "__main__":
    # Example usage
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    print("Graph structure:")
    g.print_graph()

    print("\nNeighbors of D:", g.get_neighbors("D"))
