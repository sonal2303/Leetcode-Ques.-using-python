class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s = {}
        map_t = {}

        for a, b in zip(s, t):
            if a in map_s and map_s[a] != b:
                return False

            if b in map_t and map_t[b] != a:
                return False

            map_s[a] = b
            map_t[b] = a

        return True