class Solution:
    def findMode(self, root):
        count = {}

        def traverse(node):
            if node is None:
                return

            count[node.val] = count.get(node.val, 0) + 1

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        maximum = max(count.values())

        result = []

        for value in count:
            if count[value] == maximum:
                result.append(value)

        return result