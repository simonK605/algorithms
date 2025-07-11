"""
Breadth-First Search (Graph Traversal)
---------------------------------------
BFS is an algorithm for traversing or searching graph data structures.
It starts at a source node and explores all its neighbors before moving
to the next level neighbors.

Applications:
- Shortest path in unweighted graphs
- Level order traversal
- Connectivity checks

Time Complexity: O(V + E)
Space Complexity: O(V)

Works for:
- Undirected or directed graphs
- Connected or disconnected graphs
"""

from collections import deque, defaultdict

def bfs(graph, start):
    """Perform BFS on a graph from a starting node."""
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neigh for neigh in graph[node] if neigh not in visited)

    return result


if __name__ == "__main__":
    # Graph as adjacency list (undirected)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS Traversal starting from 'A':")
    print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
