"""
Breadth-First Search (BFS) – Graph Traversal
--------------------------------------------
BFS visits all vertices of a graph in breadth-wise manner from a given source node.

Use Cases:
- Finding shortest path in unweighted graphs
- Crawling friend suggestions in social networks
- Level-order traversal in trees

Time Complexity: O(V + E)
Space Complexity: O(V) – for visited and queue
"""

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return traversal


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("BFS Traversal starting from node 0:")
    print(g.bfs(0))  # Output: [0, 1, 2, 3, 4]
