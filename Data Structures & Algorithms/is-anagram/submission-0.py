class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        s_dict = {}
        t_dict = {}
        while i >= 0 and j >= 0 and i == j:
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1

            if t[j] not in t_dict:
                t_dict[t[j]] = 1
            else:
                t_dict[t[j]] += 1

            i -= 1
            j -= 1

        return i == j and s_dict == t_dict