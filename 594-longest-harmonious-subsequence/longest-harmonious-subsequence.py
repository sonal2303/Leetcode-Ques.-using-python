class Solution:
    def findLHS(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        longest = 0

        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                longest = max(longest, length)

        return longest