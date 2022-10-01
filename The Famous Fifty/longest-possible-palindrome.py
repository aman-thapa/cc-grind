'''
Given a string str made of alphabetical letters only, 
create a function that returns the length of the longest
palindrome string that can be made from letters of str.
'''

# T - O(n)
def longestPalindrome(str):
    occurrences = [0] * 128 # all elements initialized to 0
    for letter in str:
        occurrences[ord(letter)] += 1
    # for each letter in str, incrementing the element at the ASCII code of that letter
    # get ASCII code by using ord() function

    length = 0
    for occu in occurrences:
        length += occu if occu % 2 == 0 else occu - 1

    if length < len(str):
        length += 1

    return length

str1 = "abdccdceeebebc"
result = longestPalindrome(str1)
print(result)