class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()

        result = []

        for i in range(len(s) - 1, -1, -k):
            start = max(0, i - k + 1)
            result.append(s[start:i + 1])

        return "-".join(result[::-1])