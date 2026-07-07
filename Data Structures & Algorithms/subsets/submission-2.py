class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current_subset = [[]]
        if len(nums) == 0:
            return current_subset
        
        next_subs = self.subsets(nums[1:])
        with_current = [sub + [nums[0]] for sub in next_subs]
        # print(next_subs)
        # print(with_current)
        return next_subs + with_current

