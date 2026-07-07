class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            else:
                s_chars[char] += 1
        
        for char in t:
            if char in s_chars:
                s_chars[char] -= 1
                if s_chars[char] == 0:
                    s_chars.pop(char)
            else:
                return False
        
        return len(s_chars) == 0