"""
Graph Representation: Adjacency List
-------------------------------------
This file defines a simple undirected/directed graph using an adjacency list.

Supports:
- Adding vertices
- Adding edges
- Printing the graph

Time Complexity:
- Add Vertex: O(1)
- Add Edge: O(1)
- Print: O(V + E)
"""

class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.add_vertex(src)
        if dest not in self.adj_list:
            self.add_vertex(dest)

        self.adj_list[src].append(dest)
        if not self.directed:
            self.adj_list[dest].append(src)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


if __name__ == "__main__":
    # Undirected graph example
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    print("Adjacency List of Undirected Graph:")
    g.print_graph()

    print("\nDirected Graph Example:")
    dg = Graph(directed=True)
    dg.add_edge(1, 2)
    dg.add_edge(1, 3)
    dg.add_edge(2, 4)
    dg.add_edge(3, 4)

    dg.print_graph()
