class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def stringify(comb):
            occurence_list = [0] * (30 - 2 + 1)
            for i in comb:
                occurence_list[i-1] += 1

            s = ''
            for i in occurence_list:
                s += str(i)
            return s
        
        all_combs = []
        unique = set()
        def dfs(nums, total, path):
            if total >= target:
                if total == target:
                    if stringify(path) not in unique:
                        unique.add(stringify(path))
                        all_combs.append(path)
                return
            for num in nums:
                dfs(nums, total+num, path + [num])
        
        dfs(nums, 0, [])
        return all_combs
