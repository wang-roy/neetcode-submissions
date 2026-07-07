class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recursiveHelper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            print(n)
            oneStep = memo.get(n-1, recursiveHelper(n-1))
            twoSteps = memo.get(n-2, recursiveHelper(n-2))
            totalWays = oneStep + twoSteps
            memo.update({n: totalWays})

            return totalWays
        return recursiveHelper(n)

            
