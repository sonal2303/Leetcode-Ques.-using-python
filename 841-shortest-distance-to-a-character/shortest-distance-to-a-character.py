class Solution:
    def shortestToChar(self, s, c):
        n = len(s)
        result = [float('inf')] * n

        distance = float('inf')

        for i in range(n):
            if s[i] == c:
                distance = 0
            else:
                distance += 1

            result[i] = distance

        distance = float('inf')

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                distance = 0
            else:
                distance += 1

            result[i] = min(result[i], distance)

        return result