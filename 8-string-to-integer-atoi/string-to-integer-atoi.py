class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Check overflow before adding digit
            if result > 214748364 or (
                result == 214748364 and digit > 7
            ):
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648

            result = result * 10 + digit
            i += 1

        return sign * result