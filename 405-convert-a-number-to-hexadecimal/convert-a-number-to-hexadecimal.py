class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        num = num & 0xffffffff
        digits = "0123456789abcdef"
        result = ""

        while num > 0:
            remainder = num & 15
            result = digits[remainder] + result
            num = num >> 4

        return result