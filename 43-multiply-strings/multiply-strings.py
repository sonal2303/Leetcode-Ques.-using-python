class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                total = product + result[i + j + 1]

                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        # Remove leading zeros
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(str(x) for x in result[start:])