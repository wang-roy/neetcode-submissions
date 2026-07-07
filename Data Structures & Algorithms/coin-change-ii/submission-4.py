class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        state_dict = {}
        def dfs(amount, i):
            state = (amount, i)
            if state in state_dict:
                return state_dict[state]
            if amount < 0 or i == len(coins):
                return 0
            if amount == 0:
                return 1
            
            ways = dfs(amount, i+1)
            mult = amount // coins[i]
            for j in (1, mult+1):
                ways += dfs(amount - coins[i] * j, i)
            
            state_dict.update({state: ways})
            return ways
        
        return dfs(amount, 0)