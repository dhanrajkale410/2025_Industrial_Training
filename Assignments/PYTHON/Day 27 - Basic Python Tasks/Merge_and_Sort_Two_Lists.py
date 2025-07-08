"""
Task 2: Merge and Sort Two Lists
Write a Python function that takes two lists, merges them, removes duplicates, and sorts the result in ascending order.
"""

def mergeAndSort(list1,list2) :
    return sorted(list1+list2)

list1 = [24,56,12,67,90,78]
list2 = [69,23,89,12,34,19]
print(mergeAndSort(list1,list2))