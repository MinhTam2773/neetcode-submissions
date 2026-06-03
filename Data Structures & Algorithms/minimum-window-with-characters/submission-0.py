from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {}

        matches = 0
        l = r = 0
        res = ""

        for r in range(len(s)):
            have[s[r]] = 1 + have.get(s[r], 0)

            if s[r] in need and have[s[r]] == need[s[r]]:
                matches += 1

            while matches == len(need):
                window = s[l: r + 1]
                if not res or len(window) < len(res):
                    res = window
                    print(res)

                if s[l] in need and have[s[l]] == need[s[l]]:
                    matches -= 1
                
                have[s[l]] -= 1
                l += 1

        return res
