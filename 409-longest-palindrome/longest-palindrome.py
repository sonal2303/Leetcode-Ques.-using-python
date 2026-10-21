
class Solution:
    def longestPalindrome(self, s):
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
            
        length = 0
        
        for freq in count.values():
            length += (freq // 2) * 2
            
        if length < len(s):
            length += 1
            
        return length
