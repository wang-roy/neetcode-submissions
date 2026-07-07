class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'}': '{', ')': '(', ']': '['}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != bracket_dict.get(char):
                    return False
                stack.pop(-1)
        return len(stack) == 0

