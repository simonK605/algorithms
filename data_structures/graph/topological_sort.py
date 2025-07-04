"""
Topological Sort (DFS-based)
-----------------------------
Topological sorting of a Directed Acyclic Graph (DAG) is a linear ordering
of vertices such that for every directed edge u → v, vertex u comes before v.

Applicable to:
- Task Scheduling
- Build Systems
- Course Prerequisites

Time Complexity: O(V + E)
Space Complexity: O(V) for visited set and recursion stack
"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices  # number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = set()
        stack = []

        def dfs(v):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(v)

        for vertex in range(self.vertices):
            if vertex not in visited:
                dfs(vertex)

        return stack[::-1]  # reverse to get topological order


if __name__ == "__main__":
    # Sample DAG:
    # 5 → 0 ← 4
    # ↓        ↑
    # 2 → 3 → 1

    g = Graph(6)
    g.add_edge(5, 0)
    g.add_edge(5, 2)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    order = g.topological_sort()
    print("Topological Order:", order)
    # Output (example): [4, 5, 2, 3, 1, 0]
