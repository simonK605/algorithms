"""
Topological Sort (Directed Acyclic Graph - DAG)
------------------------------------------------
Topological sort of a Directed Acyclic Graph (DAG) is a linear ordering
of vertices such that for every directed edge u → v, vertex u comes
before v in the ordering.

This implementation uses Kahn's Algorithm (BFS-based).

Applications:
- Task scheduling
- Course prerequisite resolution
- Dependency resolution in build systems

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Note: Only works on DAGs.
"""

from collections import defaultdict, deque


def topological_sort(graph):
    """
    Perform topological sort using Kahn's algorithm.

    :param graph: Dictionary where key is node and value is list of neighbors
    :return: List of nodes in topological order or an empty list if cycle is detected
    """
    in_degree = defaultdict(int)

    # Initialize in-degree of all vertices
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        in_degree[u] += 0  # Ensure even nodes with no out-edges are in map

    # Collect nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topo_order contains all nodes, return it
    if len(topo_order) == len(in_degree):
        return topo_order
    else:
        return []  # Graph has a cycle


if __name__ == "__main__":
    # Sample DAG
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
        'G': [],
        'H': []
    }

    result = topological_sort(graph)
    if result:
        print("Topological Sort Order:")
        print(result)
    else:
        print("The graph has a cycle. Topological sort not possible.")
