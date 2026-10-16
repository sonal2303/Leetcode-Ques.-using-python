class Solution:
    def findSpecialInteger(self, arr):
        count = {}
        n = len(arr)

        for num in arr:
            count[num] = count.get(num, 0) + 1

            if count[num] > n / 4:
                return num