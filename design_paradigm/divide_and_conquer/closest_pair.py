"""
Closest Pair of Points (Divide and Conquer)
--------------------------------------------
Given a list of 2D points, this algorithm finds the pair of points
with the smallest Euclidean distance between them.

Time Complexity: O(n log n)
Space Complexity: O(n)

This is much faster than the brute-force O(n^2) method.
"""

import math


def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force(points):
    min_dist = float('inf')
    closest = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest = (points[i], points[j])
    return closest, min_dist


def closest_split_pair(px, py, delta, best_pair):
    mid_x = px[len(px) // 2][0]
    in_strip = [p for p in py if mid_x - delta < p[0] < mid_x + delta]

    min_dist = delta
    n = len(in_strip)
    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):  # at most 6 comparisons
            p1, p2 = in_strip[i], in_strip[j]
            dist = euclidean(p1, p2)
            if dist < min_dist:
                min_dist = dist
                best_pair = (p1, p2)
    return best_pair, min_dist


def divide_and_conquer(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)

    mid = n // 2
    qx = px[:mid]
    rx = px[mid:]
    midpoint = px[mid][0]

    qy = list(filter(lambda x: x[0] <= midpoint, py))
    ry = list(filter(lambda x: x[0] > midpoint, py))

    (p1, d1) = divide_and_conquer(qx, qy)
    (p2, d2) = divide_and_conquer(rx, ry)

    delta = min(d1, d2)
    best_pair = p1 if d1 < d2 else p2

    (split_pair, split_dist) = closest_split_pair(px, py, delta, best_pair)

    if split_dist < delta:
        return split_pair, split_dist
    else:
        return best_pair, delta


def closest_pair(points):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return divide_and_conquer(px, py)


if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    pair, distance = closest_pair(points)
    print("Closest pair:", pair)
    print("Distance:", round(distance, 4))
