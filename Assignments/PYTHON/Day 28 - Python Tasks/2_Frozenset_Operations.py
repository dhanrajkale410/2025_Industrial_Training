"""
Assignment 2: FrozenSet Operations
Task:
Create two frozen sets:
A = frozenset([10, 20, 30, 40])
B = frozenset([30, 40, 50, 60])
Perform the following operations and print the results:
Union of A and B.
Intersection of A and B.
Difference (A - B).
Symmetric Difference (A ^ B).
Check if A is a superset of {10, 20}.
Try to add an element to A (observe the error since frozensets are immutable).
Print the length of A and B.
"""

A = frozenset([10, 20, 30, 40])
B = frozenset([30, 40, 50, 60])

print("Union : ",(A|B))
print("Intersection : ",(A&B))
print("Difference : ",(A-B))
print("Symmetric Difference : ",(A^B))