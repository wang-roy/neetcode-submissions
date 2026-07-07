class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## my original solution doesn't utilize bucket sort to keep track of occurences
        # (this is O(1) since constant # of characters)
        # def generate_occurences(s):
        #     s_dict = {}
        #     for ch in s:
        #         count = 0
        #         if ch in s_dict:
        #             count = s_dict[ch]
        #         s_dict.update({ch: count+1})
        #     return s_dict

        # s1_dict = generate_occurences(s1)
        def generate_freq_count(s, alphabet):
            s_arr = [0] * 26
            for c in s:
                idx = alphabet.index(c)
                s_arr[idx] += 1
            return s_arr

        if len(s1) > len(s2):
            return False
        lower_c_alphabet = "abcdefghijklmnopqrstuvwxyz"
        s1_arr = generate_freq_count(s1, lower_c_alphabet)

        window_start = 0
        window_end = len(s1)
        substr_arr = generate_freq_count(s2[window_start:window_end], lower_c_alphabet)
        while window_end <= len(s2):
            print(s2[window_start:window_end])
            # substr_dict = generate_occurences(s2[window_start:window_end])
            if s1_arr == substr_arr:
                return True
            elif window_end == len(s2):
                break
            
            ch_to_remove = s2[window_start]
            substr_arr[lower_c_alphabet.index(ch_to_remove)] -= 1

            ch_to_add = s2[window_end]
            substr_arr[lower_c_alphabet.index(ch_to_add)] += 1

            window_start += 1
            window_end += 1
        
        return False