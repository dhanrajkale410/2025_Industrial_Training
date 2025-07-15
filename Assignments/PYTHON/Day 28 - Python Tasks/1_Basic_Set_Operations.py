""""
Assignment 1: Basic Set Operations
Task:
Write a Python program that performs the following operations on sets:
Create two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
Perform the following operations and print the results:
Union of set1 and set2.
Intersection of set1 and set2.
Difference (set1 - set2).
Symmetric Difference (elements in either set, but not in both).
Check if set1 is a subset of set2.
Add an element 9 to set1 and remove 8 from set2.
Print the final modified sets.
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Intersection : ",set1.intersection(set2))
print("Union : ",set1.union(set2))
print("Difference : ",set1.difference(set2))
print("Symmetric Difference : ",set1.intersection(set2))