class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        n = len(s)
        if n == 0:
            return 0
        l = 0
        r = 1
        occurence_dict = {s[0]: 0}
        max_len = 1
        while r < n:
            next_ch = s[r]
            last_occurence = occurence_dict.get(next_ch, None)
            if last_occurence is not None and l <= last_occurence:
                l = occurence_dict[next_ch] + 1
            occurence_dict[next_ch] = r
            r += 1

            print('left: ' + str(l))
            print('right: ' + str(r))
            print(occurence_dict)
            if max_len < (r - l):
                max_len = r - l
        return max_len

