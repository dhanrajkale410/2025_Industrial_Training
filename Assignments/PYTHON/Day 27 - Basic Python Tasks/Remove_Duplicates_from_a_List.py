""" 
Task 1: Remove Duplicates from a List
Write a Python function that takes a list and returns a new list with duplicates removed while maintaining the original order.
"""

def removeDuplicates(lst) :
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list

list1 = ["Java","Python","C","C++","Python"]
print(removeDuplicates(list1))