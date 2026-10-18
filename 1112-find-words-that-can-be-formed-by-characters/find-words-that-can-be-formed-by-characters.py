class Solution:
    def countCharacters(self, words, chars):
        available = {}

        for ch in chars:
            available[ch] = available.get(ch, 0) + 1

        total = 0

        for word in words:
            count = {}

            for ch in word:
                count[ch] = count.get(ch, 0) + 1

            valid = True

            for ch in count:
                if count[ch] > available.get(ch, 0):
                    valid = False
                    break

            if valid:
                total += len(word)

        return total