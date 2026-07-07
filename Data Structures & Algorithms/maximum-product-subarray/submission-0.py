class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float("-inf")
        for i in range(len(nums)):
            maxProductFromI = nums[i]
            product = nums[i]
            for j in range(i+1, len(nums)):
                product *= nums[j]
                if maxProductFromI < product:
                    maxProductFromI = product
                print(product)
            print('end of each idx: ' + str(maxProductFromI))
            if maxProduct < maxProductFromI:
                maxProduct = maxProductFromI
        return maxProduct