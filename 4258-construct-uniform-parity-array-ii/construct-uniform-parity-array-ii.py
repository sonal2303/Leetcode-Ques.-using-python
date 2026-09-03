class Solution(object):
    def uniformArray(self, nums1):
        # Find the smallest odd number
        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # If there are no odd numbers,
        # all elements are already even
        if min_odd == float('inf'):
            return True

        # Every even number must be >= min_odd
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True