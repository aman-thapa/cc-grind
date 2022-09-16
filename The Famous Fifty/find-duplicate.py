'''
Given an array of integers arr that contains n+1 elements
between 1 and n inclusive, create a function that returns
the duplicate element (the element that appears more than once)

Assume that:
- there is only one duplicate number
- the duplicate number can be repeated more than once
'''

#brute force [T - O(n^2) ]

'''
def findDuplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

'''
# sorting approach [T - O(nlogn)]

def findDuplicate(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]