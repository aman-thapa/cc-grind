'''
Given a binary tree of integers root, create 3 functions
to print the elements, one for preorder, one for inorder,
and one in post order.
'''
# DFS - Depth First Search
# T - O(n)

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def dfsPreorder(root):
    if root is None:
        return
    print(root.data)
    dfsPreorder(root.left)
    dfsPreorder(root.right)

def dfsInorder(root):
    if root is None:
        return
    dfsInorder(root.left)
    print(root.data)
    dfsInorder(root.right)

def dfsPostorder(root):
    if root is None:
        return
    dfsPostorder(root.left)
    dfsPostorder(root.right)
    print(root.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print(dfsPreorder(root))
print(dfsInorder(root))
print(dfsPostorder(root))