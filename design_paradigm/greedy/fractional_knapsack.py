"""
Fractional Knapsack Problem (Greedy)
-------------------------------------
Given weights and values of items, and a knapsack with a capacity,
the goal is to get the maximum value in the knapsack by taking
fractions of items if necessary.

This problem is solved using a greedy approach:
- Sort items by value-to-weight ratio (descending)
- Take as much as possible from the item with highest ratio first

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) if sorting in-place

Note: This differs from the 0/1 Knapsack which is solved by dynamic programming.
"""

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"(v={self.value}, w={self.weight})"


def fractional_knapsack(items, capacity):
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            # Take whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take fractional part
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is full

    return total_value


if __name__ == "__main__":
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]
    capacity = 50

    max_value = fractional_knapsack(items, capacity)
    print(f"Maximum value in knapsack of capacity {capacity}: {max_value:.2f}")
