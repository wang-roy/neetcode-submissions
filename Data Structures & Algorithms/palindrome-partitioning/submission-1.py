class Solution:
    def partition(self, s: str) -> List[List[str]]:
        all_parts = []
        current_part = []
        def check_palindrome(string, i, j):
            left = i
            right = j
            while left <= right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        def dfs(i):
            print(current_part)
            if i >= len(s):
                all_parts.append(current_part.copy())
                return
            
            for j in range(i, len(s)):
                if check_palindrome(s, i, j):
                    current_part.append(s[i:j+1])
                    dfs(j+1)
                    current_part.pop(-1)
        dfs(0)
        return all_parts

