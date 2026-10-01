class Solution:
    def findTarget(self, root, k):
        seen = set()

        def search(node):
            if node is None:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)

            return search(node.left) or search(node.right)

        return search(root)