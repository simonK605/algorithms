"""
Minimum Platforms (Greedy Algorithm)
-------------------------------------
Given arrival and departure times of trains, find the minimum number of
platforms required at the station so that no train waits.

Greedy Strategy:
- Sort arrivals and departures separately
- Use a two-pointer approach to track current platforms in use

Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary (after sorting)

Example:
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
"""

def find_min_platforms(arrivals, departures):
    n = len(arrivals)
    arrivals.sort()
    departures.sort()

    platforms_needed = 0
    max_platforms = 0

    i = j = 0  # pointers for arrival and departure

    while i < n and j < n:
        if arrivals[i] < departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return max_platforms


if __name__ == "__main__":
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

    print("Minimum platforms needed:", find_min_platforms(arrivals, departures))  # Output: 3
