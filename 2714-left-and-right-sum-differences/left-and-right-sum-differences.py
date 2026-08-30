class Solution(object):
    def leftRightDifference(self, nums):
        total = sum(nums)
        left = 0
        result = []

        for num in nums:
            # Remove current element from right side
            total -= num

            # Difference between left and right
            result.append(abs(left - total))

            # Add current element to left side
            left += num

        return result