"""
Activity Selection Problem (Greedy)
Time Complexity: O(n log n)
"""

def activity_selection(activities):
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    result = [activities[0]]
    last_end = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_end:
            result.append((start, end))
            last_end = end

    return result


if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(activity_selection(activities))
