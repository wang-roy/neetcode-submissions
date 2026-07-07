class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for char in s:
            s_chars[char] = 1 + s_chars.get(char, 0)
        
        for char in t:
            if char in s_chars:
                s_chars[char] -= 1
                if s_chars[char] == 0:
                    s_chars.pop(char)
            else:
                return False
        
        return len(s_chars) == 0