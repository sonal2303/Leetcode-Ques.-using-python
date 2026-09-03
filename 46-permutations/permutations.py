class Solution(object):
    def permute(self, nums):
        result = []
        used = [False] * len(nums)
        current = []

        def backtrack():
            # If current permutation is complete
            if len(current) == len(nums):
                result.append(current[:])
                return

            # Try every number
            for i in range(len(nums)):
                if not used[i]:
                    # Choose
                    used[i] = True
                    current.append(nums[i])

                    # Explore
                    backtrack()

                    # Undo choice
                    current.pop()
                    used[i] = False

        backtrack()
        return result