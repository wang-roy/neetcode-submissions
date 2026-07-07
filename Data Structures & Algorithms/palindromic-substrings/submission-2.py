class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromesHelper(s, i):
            count = 1 # account for s[i] being a palindrome on its own
            print(s[i])
            l = i - 1
            r = i + 1
            # odd palindromes
            while l < r and l >= 0 and r < len(s):
                if s[l] == s[r]:
                    print(s[l:r+1])
                    l -= 1
                    r += 1
                    count += 1
                else:
                    break
                
            ## even palindromes
            l = i - 1
            r = i + 1
            if r < len(s) and s[i] == s[r]: ## start the even palindrome, if there is one
                print(s[i:r+1])
                r += 1
                count += 1
                while l < r and l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
            return count
        
        totalCount = 0
        for i in range(len(s)):
            totalCount += countPalindromesHelper(s, i)
        
        return totalCount
       
