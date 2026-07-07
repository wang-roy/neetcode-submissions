class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memory = {}
        def getLCS(s1, s2):
            if not s1 or not s2:
                return 0
            key = (s1, s2)
            if key in memory:
                return memory[key]
            ch1 = s1[0]
            idx = s2.find(ch1)
            case1 = 0
            if idx != -1:
                case1 = 1 + getLCS(s1[1:], s2[idx+1:])
            case2 = getLCS(s1[1:], s2)

            sub_LCS = max(case1, case2)
            memory.update({key: sub_LCS})
            return sub_LCS
        return getLCS(text1, text2)