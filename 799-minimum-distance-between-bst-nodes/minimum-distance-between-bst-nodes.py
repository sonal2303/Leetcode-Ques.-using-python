class Solution:
    def minDiffInBST(self, root):
        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        minimum = float('inf')

        for i in range(1, len(values)):
            difference = values[i] - values[i - 1]

            if difference < minimum:
                minimum = difference

        return minimum