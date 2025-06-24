"""
Tower of Hanoi (Recursion)
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solves the Tower of Hanoi problem for n disks.
    Prints steps to move disks from source to target using auxiliary.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


if __name__ == "__main__":
    tower_of_hanoi(3, 'A', 'B', 'C')
    # Output:
    # Move disk 1 from A to C
    # Move disk 2 from A to B
    # Move disk 1 from C to B
    # Move disk 3 from A to C
    # Move disk 1 from B to A
    # Move disk 2 from B to C
    # Move disk 1 from A to C
