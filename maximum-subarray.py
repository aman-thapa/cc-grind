'''
Given an array of integers arr, create a function that 
returns the sum of the subarray that has the greatest 
sum. And we don't consider the empty array as a subarray.
'''

# What is a subarray?
# A subarray of arr is a contiguous block of elements of arr.

#brute force [T - O(n^3)]

'''
def maximumSubarray(arr):
    maxSum = float("-inf")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            actualSum = 0
            for k in range(i, j+1):
                actualSum += arr[k]
            maxSum = max(maxSum, actualSum)
    return maxSum
'''

# brute force solution with cumulative sum
# T - O(n^2)

'''
def maximumSubarray(arr):
    maxSum = float("-inf")
    for i in range(len(arr)):
        cumulativeSum = 0
        for j in range(i, len(arr)):
            cumulativeSum += arr[j]
            maxSum = max(maxSum, cumulativeSum)
    return maxSum
'''
