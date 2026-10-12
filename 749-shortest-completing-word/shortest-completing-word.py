class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        required = {}

        for ch in licensePlate.lower():
            if ch.isalpha():
                required[ch] = required.get(ch, 0) + 1

        result = None

        for word in words:
            count = {}

            for ch in word.lower():
                count[ch] = count.get(ch, 0) + 1

            valid = True

            for ch in required:
                if count.get(ch, 0) < required[ch]:
                    valid = False
                    break

            if valid:
                if result is None or len(word) < len(result):
                    result = word

        return result