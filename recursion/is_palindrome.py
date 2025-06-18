"""
Check if String is a Palindrome (Recursion)
Time Complexity: O(n)
Space Complexity: O(n) – due to recursive calls
"""

def is_palindrome(s):
    """
    Recursively checks if a string is a palindrome.
    Ignores case and spacing by default.
    """
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


if __name__ == "__main__":
    print(is_palindrome("racecar"))      # Output: True
    print(is_palindrome("hello"))        # Output: False
    print(is_palindrome("A man a plan a canal Panama"))  # Output: True
