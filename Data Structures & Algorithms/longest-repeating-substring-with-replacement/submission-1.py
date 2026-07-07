class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## variable sliding window
        def get_freq_char(unique_chars):
            max_count = 0
            freq_char = ""
            for (char, count) in unique_chars.items():
                if count > max_count:
                    max_count = count
                    freq_char = char
            return freq_char, max_count
        
        def update_char_dict(unique_chars, curr_char):
            count = 0
            if curr_char in unique_chars:
                count = unique_chars[curr_char] 
            unique_chars.update({curr_char: count+1})
            return unique_chars
        max_repeat = 0
        unique_chars = {}

        window_start = 0
        window_end = 0
        while window_end < len(s):
            unique_chars = update_char_dict(unique_chars, s[window_end])
            
            print(s[window_start:window_end+1])
            char, most_freq_char_count = get_freq_char(unique_chars)
            substr_len = window_end - window_start + 1
            print(substr_len)
            print(most_freq_char_count)
            ## check if it is valid
            if substr_len - most_freq_char_count > k:
                unique_chars[s[window_start]] -= 1
                window_start += 1
                
            elif substr_len > max_repeat:
                max_repeat = substr_len

            window_end += 1    
            
            
        return max_repeat
            