class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + chr(len(s)) + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            word_len = ord(s[i])
            result.append(s[i+1:i+word_len+1])
            i = i + word_len + 1
        return result
