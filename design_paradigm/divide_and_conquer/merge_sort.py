"""
Merge Sort (Divide and Conquer)
Time Complexity: O(n log n)
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # divide array in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    print(merge_sort([5, 2, 4, 1, 3]))
