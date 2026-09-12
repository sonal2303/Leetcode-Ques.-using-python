class Solution:
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            w = set(word.lower())

            for row in rows:
                if w.issubset(row):
                    result.append(word)
                    break

        return result