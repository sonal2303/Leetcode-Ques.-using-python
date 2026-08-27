class Solution(object):
    def lexGreaterPermutation(self, s, target):
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        n = len(s)
        i = 0

        # Match target as much as possible
        while i < n and count[ord(target[i]) - ord('a')] > 0:
            count[ord(target[i]) - ord('a')] -= 1
            i += 1

        while True:

            # Try to make current position bigger
            if i < n:
                x = ord(target[i]) - ord('a')

                for c in range(x + 1, 26):
                    if count[c] > 0:

                        count[c] -= 1

                        answer = target[:i]
                        answer += chr(c + ord('a'))

                        # Add remaining characters in sorted order
                        for k in range(26):
                            answer += chr(k + ord('a')) * count[k]

                        return answer

            # If we reached the beginning, no answer exists
            if i == 0:
                break

            # Move one position backward
            i -= 1
            count[ord(target[i]) - ord('a')] += 1

        return ""