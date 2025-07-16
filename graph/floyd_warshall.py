"""
Floyd-Warshall Algorithm (All-Pairs Shortest Path)
---------------------------------------------------
The Floyd-Warshall algorithm finds the shortest distances between
all pairs of vertices in a weighted graph (with positive or negative edge weights,
but no negative weight cycles).

It uses dynamic programming and works by incrementally improving the estimate
of the shortest path between any two vertices.

Time Complexity: O(V^3)
Space Complexity: O(V^2)

Input:
- A graph represented as an adjacency matrix.
"""

INF = float('inf')

def floyd_warshall(graph):
    """
    Runs the Floyd-Warshall algorithm on the input adjacency matrix.

    :param graph: 2D list (matrix) representing the weighted graph.
                  graph[i][j] is the weight from node i to j (or INF if no edge).
    :return: 2D list containing the shortest distances between all pairs.
    """
    V = len(graph)
    dist = [row[:] for row in graph]  # Deep copy of the graph matrix

    for k in range(V):  # Intermediate node
        for i in range(V):  # Source node
            for j in range(V):  # Destination node
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(matrix):
    for row in matrix:
        print(["INF" if x == INF else x for x in row])


if __name__ == "__main__":
    # Example graph with 4 vertices
    graph = [
        [0,     5,   INF,   10],
        [INF,   0,     3,   INF],
        [INF, INF,     0,     1],
        [INF, INF, INF,     0]
    ]

    print("Original graph (adjacency matrix):")
    print_matrix(graph)

    print("\nShortest distances between every pair of vertices:")
    result = floyd_warshall(graph)
    print_matrix(result)
