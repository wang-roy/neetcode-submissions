class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}
        def recursiveHelper(i=0, own=False):
            if i >= len(prices):
                return 0
            
            state = (i, own)
            if state in memory:
                return memory[state]
            print(prices)
            currVal = prices[i]
            # if own, consider selling
            if own:
                transaction = recursiveHelper(i+2, own=False) + currVal
                print(f'after selling at {currVal}: {transaction}')
                no_move = recursiveHelper(i+1,  own=True)
                print(f'after holding {currVal}: {no_move}')
            # if not own, consider buying
            else:
                transaction = recursiveHelper(i+1,  own=True) - currVal
                print(f'profit after buying {currVal}: {transaction}')
                no_move = recursiveHelper(i+1, own=False)
                print(f'profit after not buying: {no_move}')
            profit = max(transaction, no_move)
            memory.update({state: profit})
            return profit
        
        return recursiveHelper(i=0, own=False)
            