'''
Given a linked list of integers list, create a boolean
function that checks if it's a palindrome linked list
in constant space complexity.
'''

# T - O(n^2)

def isPalindromeList(list):
    length = 0
    temp = list.head
    while temp:
        length += 1
        temp = temp.next
    left = list.head
    for i in range(length//2):
        right = list.head
        for j in range(length-i-1):
            right = right.next
        if left.data != right.data:
            return False
        left = left.next
    return True