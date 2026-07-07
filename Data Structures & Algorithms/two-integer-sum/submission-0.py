class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_index_dict = {}
        for i in range(n):
            num = nums[i]
            target_pair = target - num
            if target_pair in num_index_dict:
                pair_index = num_index_dict[target_pair][0]
                return [pair_index, i]
            elif num in num_index_dict:
                indices = num_index_dict[num]
                indices.append(i)
            else:
                num_index_dict.update({num: [i]})