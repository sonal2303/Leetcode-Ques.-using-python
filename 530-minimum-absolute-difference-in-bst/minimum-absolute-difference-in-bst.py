class Solution:
    def getMinimumDifference(self, root):
        self.prev = None
        self.minimum = float('inf')

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.prev is not None:
                difference = node.val - self.prev
                self.minimum = min(self.minimum, difference)

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return self.minimum