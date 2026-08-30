class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        # Find indices of minimum and maximum
        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        # Put smaller index first
        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        # 3 possible cases:
        # 1. Remove both from the front
        front = right + 1

        # 2. Remove both from the back
        back = n - left

        # 3. Remove one from front and one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)