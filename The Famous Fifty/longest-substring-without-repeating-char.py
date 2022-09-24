'''
Given a string str made of alphabetical letters only,
create a function that returns the length of the longest 
substring without repeating characters.
'''

# brute force [T - O(n^3)]

'''
def withoutrepeating(str):
    visited = [False] * 128 #including 128 ASCII characters
    for ch in str:
        if visited[ord(ch)]: # using ord function to get the equivalent element of a character
            return False
        else:
            visited[ord(ch)] = True
    return True

def longestSubstringWithoutRepeating(str):
    maxLength = 0
    for i in range(len(str)):
        for j in range(i, len(str)):
            substr = str[i:j+1]
            if withoutrepeating(substr) and len(substr) > maxLength:
                maxLength = len(substr)
    return maxLength
'''
# better approach [T - O(n)]

def longestSubstringWithoutRepeating(str):
    maxLength = 0
    start = 0
    indexes = [-1] * 128
    for i in range(len(str)):
        if indexes[ord(str[i])] >= start:
            start = indexes[ord(str[i])] + 1
        indexes[ord(str[i])] = i
        maxLength = max(maxLength, i - start+1)
    return maxLength

str1 = "abcdbeghef"
result = longestSubstringWithoutRepeating(str1)
print(result)