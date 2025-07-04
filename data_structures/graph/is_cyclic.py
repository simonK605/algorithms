"""
Cycle Detection in Graph (DFS-based)
-------------------------------------
This script checks whether a cycle exists in a graph.

- For Undirected Graphs:
    A cycle exists if during DFS we revisit a node that isn't the parent.
- For Directed Graphs:
    A cycle exists if we visit a node that's already in the recursion stack.

Time Complexity: O(V + E)
Space Complexity: O(V) for visited/recStack sets
"""

from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def is_cyclic_undirected(self):
        visited = set()

        def dfs(v, parent):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    def is_cyclic_directed(self):
        visited = set()
        rec_stack = set()

        def dfs(v):
            visited.add(v)
            rec_stack.add(v)

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(v)
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex):
                    return True
        return False


if __name__ == "__main__":
    # Test for Undirected Graph
    g1 = Graph(directed=False)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)

    print("Undirected graph has cycle:", g1.is_cyclic_undirected())  # True

    # Test for Directed Graph
    g2 = Graph(directed=True)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)

    print("Directed graph has cycle:", g2.is_cyclic_directed())  # True

    # Acyclic directed graph
    g3 = Graph(directed=True)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)

    print("Directed graph has cycle:", g3.is_cyclic_directed())  # False
