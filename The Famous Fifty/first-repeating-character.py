'''
Given a string str, create a function that returns the first
repeating character(the first character that we have seen before).
If such a character doesn't exist, return the null character '\0'
'''
# brute force method [T - O(n^2)]

'''
def firstRepeatingCharacter(str):
    for i in range(len(str)): # i starts from 0 and goes to len of str
        for j in range(i): # j starts from 0 and stops at i
            if str[i] == str[j]:
                return str[i]
    return '\0'
'''
# hash table [t - O(n)]

def firstRepeatingCharacter(str):
    visited = {}
    for ch in str:
        if visited.get(ch):
            return ch
        else:
            visited[ch] = True
    return '\0'

ip = input()
result = firstRepeatingCharacter(ip)
print(result)