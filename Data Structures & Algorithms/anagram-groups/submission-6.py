class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## key: how to get unique identifier for each group?
        def get_canonical_form(string):
            char_dict = {}
            for char in string:
                if char not in char_dict:
                    char_dict.update({char: 1})
                else:
                    count = char_dict[char]
                    char_dict.update({char: count+1})

            alphabet = "abcdefhijklmnopqrstuvwxyz"
            canonical_form = ""
            for letter in alphabet:
                if letter in char_dict:
                    phrase = letter + str(char_dict[letter])
                    canonical_form += phrase
                    # print(canonical_form)
            return canonical_form
            
        n = len(strs)
        anagram_dict = {}
        for string in strs:
            canonical_form = get_canonical_form(string)
            if canonical_form not in anagram_dict:
                anagram_dict.update({canonical_form: [string]})
            else:
                group = anagram_dict[canonical_form]
                group.append(string)
                anagram_dict.update({canonical_form: group})

        anagram_list = [group for _, group in anagram_dict.items()]
        
        return anagram_list
            
