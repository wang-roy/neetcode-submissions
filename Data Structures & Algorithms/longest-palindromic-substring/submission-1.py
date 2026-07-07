class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(s, l, r):
            length_wo_center = 0
            
        maxLength = 0
        longestPal = ""
        n = len(s)
        for i in range(n):
            currLength = 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < n:   
                if s[l] != s[r]:
                    break;
                l -= 1
                r += 1
                currLength += 2
            if currLength > maxLength:
                maxLength = currLength
                longestPal = s[l+1:r]
            
            if i + 1 < n and s[i] == s[i + 1]:
                l = i - 1
                r = i + 2
                currLength = 2
                while l >= 0 and r < n:   
                    if s[l] != s[r]:
                        break;
                    l -= 1
                    r += 1
                    currLength += 2
                if currLength > maxLength:
                    maxLength = currLength
                    longestPal = s[l+1:r]
        return longestPal
