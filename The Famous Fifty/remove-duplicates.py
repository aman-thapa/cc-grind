'''
Given an array of integers arr, create a function that returns
an array that contains the values of arr without duplicates
(the order doesn't matter)
'''
# brute force [T - O(n^2)]

def removeDuplicates(arr):
    noDuplicateArr = []
    for element in arr:
        if element not in noDuplicateArr: # traverse again and again
            noDuplicateArr.append(element)
    return noDuplicateArr
