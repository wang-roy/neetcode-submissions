class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maintain a dp array of max and min (most positive prod up to this point, most negative/smallest prod up to this point?)
        lastNegIndex = -1

        maxRunningSum = 1
        minRunningSum = 1
        maxProduct = float('-inf')
        for num in nums:
            tempMax = maxRunningSum
            tempMin = minRunningSum
            maxRunningSum = max(num, num * tempMax, num * tempMin)
            minRunningSum = min(num, num * tempMax, num * tempMin)

            if maxProduct < maxRunningSum:
                maxProduct = maxRunningSum
            print(maxRunningSum)
            print(minRunningSum)
        return maxProduct


        