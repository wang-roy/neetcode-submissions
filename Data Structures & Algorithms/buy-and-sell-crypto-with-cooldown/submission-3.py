class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def recursiveHelper(priceList, own=False):
            if len(priceList)==0:
                return 0
            
            print(priceList)
            currVal = priceList[0]
            # if own, consider selling
            if own:
                transaction = recursiveHelper(priceList[2:], own=False) + currVal
                print(f'after selling at {currVal}: {transaction}')
                no_move = recursiveHelper(priceList[1:], own=True)
                print(f'after holding {currVal}: {no_move}')
            # if not own, consider buying
            else:
                transaction = recursiveHelper(priceList[1:], own=True) - currVal
                print(f'profit after buying {currVal}: {transaction}')
                no_move = recursiveHelper(priceList[1:], own=False)
                print(f'profit after not buying: {no_move}')
            return max(transaction, no_move)
        
        return recursiveHelper(prices, own=False)
            