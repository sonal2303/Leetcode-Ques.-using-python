class Solution:
    def findErrorNums(self, nums):
        seen = set()
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        n = len(nums)
        missing = n * (n + 1) // 2 - (sum(nums) - duplicate)

        return [duplicate, missing]