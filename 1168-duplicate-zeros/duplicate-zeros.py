class Solution:
    def duplicateZeros(self, arr):
        result = []

        for num in arr:
            result.append(num)

            if num == 0:
                result.append(0)

        arr[:] = result[:len(arr)]