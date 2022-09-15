'''
Given an array of integers arr, create a function that returns
an array that contains the values of arr without duplicates
(the order doesn't matter)
'''
# brute force [T - O(n^2)]

'''
def removeDuplicates(arr):
    noDuplicateArr = []
    for element in arr:
        if element not in noDuplicateArr: # traverse again and again
            noDuplicateArr.append(element)
    return noDuplicateArr

'''

# sorting method [T - O(nlogn)]

'''
def removeDuplicates(arr):
    if len(arr) == 0: # since we are reading the first element 
        return []
    arr.sort()
    noDuplicateArr = [arr[0]]
    for i in range (1, len(arr)):
        if arr[i] != arr[i-1]:
            noDuplicateArr.append(arr[i])
    return noDuplicateArr
'''

# hash table [T - ] 

def removeDuplicates(arr):
    visited = {}
    for element in arr:
        visited [element] = True
    return list(visited.keys())

arr = [4, 2, 3, 2, 4, 4, 1]
result = removeDuplicates(arr)
print(result)