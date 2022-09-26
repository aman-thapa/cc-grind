'''
Given a non-empty array of integers arr, create a function
that returns the index of a peak element. 
We consider an element as peak if it's greater than or equal 
to its neighbors, the next and previous element, and the first 
element have at most one neighbor only. And if there are 
mutipe peaks in arr, just return the index of one of them.
'''

# tranverse through array

def findPeak(arr):
    for i in range(len(arr)):
        if(i == 0 or arr[i] >= arr[i-1]) and (i == len(arr)-1 or arr[i >= arr[i+1]]):
            return i