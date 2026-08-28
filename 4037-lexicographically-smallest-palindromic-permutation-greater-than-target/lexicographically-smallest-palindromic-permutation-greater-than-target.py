class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        # Count characters
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check if palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Characters available for left half
        half = [0] * 26
        for i in range(26):
            half[i] = count[i] // 2

        half_len = n // 2
        prefix = []

        # Check whether current prefix can be completed
        # to a palindrome greater than target
        def possible():
            remaining = []

            for i in range(26):
                remaining += [chr(ord('a') + i)] * half[i]

            left = ''.join(prefix) + ''.join(reversed(remaining))

            palindrome = left + middle + left[::-1]

            return palindrome > target

        # Build left half greedily
        for _ in range(half_len):
            found = False

            for i in range(26):
                if half[i] == 0:
                    continue

                ch = chr(ord('a') + i)

                half[i] -= 1
                prefix.append(ch)

                if possible():
                    found = True
                    break

                prefix.pop()
                half[i] += 1

            if not found:
                return ""

        left = ''.join(prefix)
        answer = left + middle + left[::-1]

        if answer > target:
            return answer

        return ""