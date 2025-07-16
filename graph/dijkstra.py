"""
Dijkstra's Algorithm (Graph - Single Source Shortest Path)
------------------------------------------------------------
Finds the shortest path from a single source node to all other nodes
in a graph with non-negative edge weights.

Data Structure: Min-Heap (Priority Queue)

Time Complexity:
- O((V + E) log V) using priority queue
- Space Complexity: O(V)

Limitation:
- Does NOT work correctly with negative edge weights (use Bellman-Ford instead)
"""

import heapq
from collections import defaultdict

def dijkstra(graph, source):
    """
    Compute the shortest path from the source node to all other nodes.
    :param graph: Dict with node -> list of (neighbor, weight)
    :param source: Starting node
    :return: Dict with node -> shortest distance from source
    """
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    visited = set()
    min_heap = [(0, source)]

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist


if __name__ == "__main__":
    # Graph represented as adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    source = 'A'
    shortest_distances = dijkstra(graph, source)

    print(f"Shortest distances from node '{source}':")
    for node, distance in shortest_distances.items():
        print(f"{node}: {distance}")
