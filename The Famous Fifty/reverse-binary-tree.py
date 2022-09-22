'''
Given a binary tree of integers root, create a function
that reverses it left to right in-place.
'''
# T- O(n)
def revreseTree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    revreseTree(tree.left)
    revreseTree(tree.right)
