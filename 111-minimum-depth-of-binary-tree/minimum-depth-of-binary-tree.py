class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # If there is no left child
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If there is no right child
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Both children exist
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return 1 + min(left, right)