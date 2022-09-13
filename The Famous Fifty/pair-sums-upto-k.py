'''
Q. Given an array of integers arr and an interger k, 
create boolean function that checks if there exists two elements
in arr such that we get k when we add them together. 
'''
# brute force solution
'''
def findPair(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
            
    return False
'''
# t.c= O(n^2) and s.c = O(1)

# sort array approach
'''
def findPair(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left<right:
        if arr[left] + arr[right] == k:
            return True
        elif arr[left] + arr[right] <k:
            left += 1
        else:
            right -= 1
    return False
'''
# t.c = O(nlogn) and s.c = O(1)

# hash table approach
def findPair(arr, k):
    dict = {}
    for element in arr:
        if dict.get(k-element):
            return True
        else:
            dict[element] = True
    return False
    
arr = [] 
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    arr.append(ele)

k = int(input())
result = findPair(arr, k)
print(result)


