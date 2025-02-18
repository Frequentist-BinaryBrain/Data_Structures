#   https://youtu.be/rKnD7rLT0lI?si=BuLvNFzVaGOn_Q8r
#   https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # Function to flatten the root tree and return the list tail
        def dfs(root):  # Depth First Search
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # If left side is not empty
            if root.left:
                leftTail.right = root.right  # Connect the right subtree of the left subtree to the right of the root
                root.right = root.left  # Move the left subtree to the right
                root.left = None  # Set the left child to None

            # Determine the last node of the flattened tree
            last = rightTail or leftTail or root
            return last

        dfs(root)

