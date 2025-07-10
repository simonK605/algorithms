"""
Huffman Encoding (Greedy Algorithm)
-------------------------------------
Huffman Encoding is a compression algorithm that assigns variable-length
prefix codes to characters based on their frequencies. Characters with
higher frequencies get shorter codes.

Algorithm:
- Build a min-heap of nodes based on character frequency.
- Combine the two smallest nodes until one root remains (greedy choice).
- Traverse the final tree to assign binary codes.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heapq to compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Combine two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # root of the tree


def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = current_code

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes


def huffman_encoding(text):
    if not text:
        return {}, ""

    root = build_huffman_tree(text)
    codes = generate_codes(root)

    encoded_text = ''.join(codes[char] for char in text)
    return codes, encoded_text


def huffman_decoding(encoded_text, codes):
    # Build reverse lookup
    reverse_codes = {v: k for k, v in codes.items()}
    decoded = ""
    current_code = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded += reverse_codes[current_code]
            current_code = ""
    return decoded


if __name__ == "__main__":
    sample_text = "huffman encoding example"

    print("Original text:", sample_text)
    codes, encoded = huffman_encoding(sample_text)
    print("Huffman Codes:", codes)
    print("Encoded:", encoded)

    decoded = huffman_decoding(encoded, codes)
    print("Decoded:", decoded)
