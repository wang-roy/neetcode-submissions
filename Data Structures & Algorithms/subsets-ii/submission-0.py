class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def hashify(subset):
            # count occurences
            subset_hashed = {}
            for num in subset:
                if num not in subset_hashed:
                    subset_hashed.update({num:1})
                else:
                    subset_hashed.update({num:subset_hashed[num]+1})
            # stringify occurences
            stringify = ""
            for i in range(-20, 21):
                count = 0 
                if i in subset_hashed:
                    count = subset_hashed[i]
                stringify += str(count)
            return stringify

        def recursive_helper(nums, dup_checker=set()):
            if len(nums) == 0:
                return [[]], set(hashify([]))

            next_subsets, dup_checker = recursive_helper(nums[1:], dup_checker)
            curr = nums[0]
            with_curr = []

            for subset in next_subsets:
                new_subset = subset+[curr]
                subset_hashed = hashify(new_subset)
                if subset_hashed not in dup_checker:
                    with_curr.append(new_subset)
                    dup_checker.add(subset_hashed)
            subsets = next_subsets + with_curr
            return subsets, dup_checker

        subsets, _ = recursive_helper(nums)
        return subsets
        