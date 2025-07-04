"""
Depth-First Search (DFS) – Graph Traversal
-------------------------------------------
DFS explores as far as possible along each branch before backtracking.

Use Cases:
- Detecting cycles
- Topological sorting
- Maze solving

Time Complexity: O(V + E)
Space Complexity: O(V) for visited set and recursion stack
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)

    def dfs(self, start):
        visited = set()
        traversal = []

        def dfs_recursive(node):
            if node in visited:
                return
            visited.add(node)
            traversal.append(node)
            for neighbor in self.adj_list[node]:
                dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("DFS Traversal starting from node 0:")
    print(g.dfs(0))  # Output: [0, 1, 3, 5, 2, 4]
