class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_set = set()
        n = len(nums)
        print('test')
        sorted_nums = sorted(nums)
        print(sorted_nums)
        for i in range(n):
            num = sorted_nums[i]
            target = -1 * num
            left = i+1
            right = n-1
            while left < right:
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]
                if left_num + right_num > target:
                    right -= 1
                elif left_num + right_num < target:
                    left += 1
                else:
                    if (num, left_num, right_num) not in triplet_set:
                        triplet_set.add((num, left_num, right_num))
                    right -= 1
            
        triplets = [list(triplet) for triplet in triplet_set]
        return triplets