class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # If this is a leaf node
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Check left and right subtrees
        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))