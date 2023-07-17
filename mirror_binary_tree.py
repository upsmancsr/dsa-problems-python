# Given the root node of a binary tree, swap the ‘left’ and ‘right’ children for each node. 
# The below example shows how the mirrored binary tree should look like.
#          4
#       /    \
#     10      40
#    /  \    /  \
#  15   50  30   60
# 
# mirrored:
#          4
#       /    \
#     40      10
#    /  \    /  \
#  60   30  50   15

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def swap_children(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    swap_children(node.left)
    swap_children(node.right)

def main():
    # build a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # swap the children
    swap_children(root)

    # validate the result
    assert root.left.value == 3
    assert root.right.value == 2
    assert root.right.left.value == 5
    assert root.right.right.value == 4

main()