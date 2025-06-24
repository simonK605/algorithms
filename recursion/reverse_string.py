"""
Reverse a String (Recursion)
Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string(s):
    """
    Recursively reverses a string.
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("hello"))  # Output: "olleh"
