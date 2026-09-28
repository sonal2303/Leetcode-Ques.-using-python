class Solution:
    def findSecondMinimumValue(self, root):
        values = set()

        def traverse(node):
            if node is None:
                return

            values.add(node.val)

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        if len(values) < 2:
            return -1

        values = sorted(values)

        return values[1]