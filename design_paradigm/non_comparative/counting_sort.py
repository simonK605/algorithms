"""
Counting Sort
Time Complexity: O(n + k), where k is the range of the input
Description: Non-comparison sort. Only for non-negative integers or bounded range.
"""

def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    output = []
    for i, c in enumerate(count):
        output.extend([i] * c)
    return output

if __name__ == "__main__":
    print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
