class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        results = [0] * n
        for j in range(n):
            print(stack)
            curr_temp = temperatures[j]
            ## update stack
            while len(stack) > 0 and curr_temp > stack[-1][0]:
                temp, i = stack[-1]
                results[i] = j-i
                stack.pop(-1)
            stack.append((curr_temp, j))
        
        return results
        