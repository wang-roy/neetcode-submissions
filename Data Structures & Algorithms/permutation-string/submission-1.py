class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def generate_occurences(s):
            s_dict = {}
            for ch in s:
                count = 0
                if ch in s_dict:
                    count = s_dict[ch]
                s_dict.update({ch: count+1})
            return s_dict

        s1_dict = generate_occurences(s1)
        
        window_start = 0
        window_end = len(s1)
        while window_end <= len(s2):
            substr_dict = generate_occurences(s2[window_start:window_end])
            if s1_dict == substr_dict:
                return True
            
            window_start += 1
            window_end += 1
        
        return False