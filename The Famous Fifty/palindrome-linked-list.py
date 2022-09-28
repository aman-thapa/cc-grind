'''
Given a linked list of integers list, create a boolean
function that checks if it's a palindrome linked list
in constant space complexity.
'''

# T - O(n^2)

'''
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
'''

# better approach [T - O(n)]
# by reversing the right half then comparing

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
def reverseList(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def isPalindromeList(list):
    slow = fast = list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = reverseList(slow)
    head = list.head
    while slow:
        if slow.data != head.data:
            return False
        slow = slow.next
        head = head.next
    return True

lst1 = [1, 2, 3, 4, 3, 2, 1]
result = isPalindromeList(lst1)
print(result)