"""
Depth-First Search (Graph Traversal)
-------------------------------------
DFS is an algorithm for traversing or searching tree or graph data structures.
It explores as far as possible along each branch before backtracking.

Applications:
- Cycle detection
- Topological sorting
- Connectivity checks
- Pathfinding

Time Complexity: O(V + E)
Space Complexity: O(V) for recursion or visited set

Works for:
- Directed and undirected graphs
- Connected and disconnected graphs
"""

def dfs(graph, node, visited=None, result=None):
    """Recursive DFS traversal from a starting node."""
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(node)
    result.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result


if __name__ == "__main__":
    # Graph as adjacency list (undirected or directed)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("DFS Traversal starting from 'A':")
    print(dfs(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']
