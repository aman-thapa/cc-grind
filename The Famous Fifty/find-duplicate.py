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

'''
def findDuplicate(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]
'''

# hash table approach [T - O(n)]

'''
def findDuplicate(arr):
    visited = {}
    for element in arr:
        if visited.get(element):
            return element
        else:
            visited[element]  = True

arr = [4, 3, 1, 2, 1]
result = findDuplicate(arr)
print(result)
'''

# Floyd's cycle detection algorithm
# used to detect cycyles in a linked list

# T = O(n) and S = O(1)
def findDuplicate(arr):
    tortoise = arr[0]
    hare = arr[arr[0]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise

arr = [4, 3, 1, 2, 1]
result = findDuplicate(arr)
print(result)