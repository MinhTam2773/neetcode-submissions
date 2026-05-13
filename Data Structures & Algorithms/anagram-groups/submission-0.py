class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for s in strs:
            dict_str = {}

            for c in s:
                if c not in dict_str:
                    dict_str[c] = 1
                else:
                    dict_str[c] += 1
            s_tuple = tuple(sorted(dict_str.items()))

            if s_tuple not in ana_dict:
                ana_dict[s_tuple] = [s]
            else:
                ana_dict[s_tuple].append(s)
            
        return list(ana_dict.values())