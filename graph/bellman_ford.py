"""
Bellman-Ford Algorithm (Graph - Single Source Shortest Path)
-------------------------------------------------------------
Finds the shortest path from a single source vertex to all other vertices in a weighted graph.
Handles negative edge weights (unlike Dijkstra) and can detect negative weight cycles.

Time Complexity: O(V * E)
Space Complexity: O(V)

Usage:
- Works with graphs that have negative weights.
- Detects negative weight cycles.

Input:
- Graph as a list of edges: (u, v, weight)
- Number of vertices
- Source vertex
"""

def bellman_ford(edges, vertex_count, source):
    # Step 1: Initialize distances
    dist = [float('inf')] * vertex_count
    dist[source] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(vertex_count - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Step 3: Check for negative-weight cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return dist


if __name__ == "__main__":
    # Graph with 5 vertices (0 through 4)
    # Each tuple represents an edge: (source, destination, weight)
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]

    vertex_count = 5
    source_vertex = 0

    try:
        distances = bellman_ford(edges, vertex_count, source_vertex)
        print(f"Shortest distances from vertex {source_vertex}:")
        for i, d in enumerate(distances):
            print(f"Vertex {i}: {d}")
    except ValueError as e:
        print(e)
