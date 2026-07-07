class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def generateCombinations(s, digit_map):
            if len(s) == 0:
                return []
            if len(s) == 1:
                return digit_map[s[0]]
                
            combsAhead = generateCombinations(s[1:], digit_map)
            print(s)
            print(combsAhead)
            combinations = []
            letters = digit_map[s[0]]
            for comb in combsAhead:
                for letter in letters:
                    combinations.append(letter + comb)
            return combinations

        digit_dict = {'2': ['a', 'b', 'c'], 
                      '3': ['d', 'e', 'f'], 
                      '4': ['g', 'h', 'i'], 
                      '5': ['j', 'k', 'l'], 
                      '6': ['m', 'n', 'o'], 
                      '7': ['p', 'q', 'r', 's'], 
                      '8': ['t', 'u', 'v'], 
                      '9': ['w', 'x', 'y', 'z'], 
                      '0': ['+']}
        return generateCombinations(digits, digit_dict)
