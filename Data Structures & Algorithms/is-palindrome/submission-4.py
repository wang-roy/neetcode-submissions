class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        alphanumer = "abcedfghijlkmnopqrstuvwxyz1234567890"
        s_alphanum = ''.join([char if char in alphanumer else '' for char in s])
        l = 0
        r = len(s_alphanum) - 1
        while l <= r:
            if s_alphanum[l] != s_alphanum[r]:
                return False
            l += 1
            r -= 1
        
        return True
