class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq = freq_dict.get(num, 0)
            freq_dict[num] = freq + 1
        print(freq_dict)
        n = len(nums)
        freq_buckets = [None] * n
        print(freq_dict.items())
        for num, freq in freq_dict.items():
            if freq_buckets[freq-1]:
                freq_buckets[freq-1].append(num)
            else:
                freq_buckets[freq-1] = [num]
            print(freq_buckets)
        
        count = k
        i = n-1
        kMostFreq = []
        while i >= 0 and count > 0:
            if freq_buckets[i]:
                count -= len(freq_buckets[i])
                kMostFreq.extend(freq_buckets[i])
            i -= 1
        
        return kMostFreq



        
