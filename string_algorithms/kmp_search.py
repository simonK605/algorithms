"""
KMP (Knuth-Morris-Pratt) Substring Search Algorithm
-----------------------------------------------------
Efficient algorithm for finding occurrences of a pattern within a text.

It avoids re-checking previously matched characters using a prefix table
(called the "Longest Prefix Suffix" or LPS array).

Time Complexity:
- Preprocessing LPS array: O(m)
- Searching: O(n)
Overall: O(n + m)

Where:
- n = length of the text
- m = length of the pattern
"""

def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array.
    LPS[i] = length of the longest proper prefix of pattern[0:i+1]
             which is also a suffix of pattern[0:i+1]
    """
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # fallback
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Perform KMP search of `pattern` in `text`.
    Returns a list of starting indices where pattern is found.
    """
    if not pattern:
        return []

    lps = compute_lps(pattern)
    result = []

    i = j = 0  # i = index for text, j = index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]  # continue searching

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # fallback
            else:
                i += 1

    return result


if __name__ == "__main__":
    text = "abxabcabcaby"
    pattern = "abcaby"
    matches = kmp_search(text, pattern)
    print(f"Pattern '{pattern}' found at positions: {matches}")
