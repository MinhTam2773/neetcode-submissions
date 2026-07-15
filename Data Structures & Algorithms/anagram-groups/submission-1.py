from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We use a dictionary to store anagrams: the key are the anagrams, the values are arrays of strings in strs array
        #that have the same anagrams
        dict_ana = {}
        
        #Iterate the strs array
        for string in strs:
            #We convert the current string into a dictionary of char and frequencies, for example,
            # "act" will be {"a": 1, "c":1, "t":1}
            char_count = Counter(string)

            #We have to convert from dict to tuple because ana_dict CAN NOT contain dictionary as key
            s_tuple = tuple(sorted(char_count.items()))

            # We check if the dictionary we just converted is in the dict_ana
            # If no, we add the anagram and initiate an array containing the current string only
            if s_tuple not in dict_ana:
                dict_ana[s_tuple] = [string]
            else:
                dict_ana[s_tuple].append(string)

        return list(dict_ana.values())