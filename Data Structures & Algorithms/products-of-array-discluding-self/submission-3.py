class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_no_zero = 1
        zero_count = 0 
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zero_count += 1
            else:
                product_no_zero *= num

        product_list = []
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if zero_count > 1:
                    product_list.append(0)
                else:
                    product_list.append(product_no_zero)
            else:
                if zero_count == 0:
                    product_list.append(product_no_zero // num)
                else:
                    product_list.append(0)
            
            
                
       
        
        return product_list