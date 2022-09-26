'''
Given a non-empty array of integers arr, create a function
that returns the index of a peak element. 
We consider an element as peak if it's greater than or equal 
to its neighbors, the next and previous element, and the first 
element have at most one neighbor only. And if there are 
mutipe peaks in arr, just return the index of one of them.
'''

# tranverse through array [T - O(n)]

'''
def findPeak(arr):
    for i in range(len(arr)):
        if(i == 0 or arr[i] >= arr[i-1]) and (i == len(arr)-1 or arr[i] >= arr[i+1]):
            return i

'''
# Binary Search approach
# Binary search is a searching algorithm that can be applied on a sorted array to search for a value in O(logn).
# T - O(logn)

def findPeak(arr):
    left = 0
    right = len(arr)- 1
    while left< right:
        mid = (left + right)//2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left

arr1 = [1, 5, 8, 8, 3, 9]
arr2 = [1, 3, 9, 10, 5, 2, 6, 7, 4]
result = findPeak(arr2)
print(result)