class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current_subset = [[]]
        if len(nums) == 0:
            return current_subset
        
        next_subs = self.subsets(nums[1:])
        with_current = []
        for sub in next_subs:
            with_current.append(sub + [nums[0]])
        print(next_subs)
        print(with_current)
        return next_subs + with_current

