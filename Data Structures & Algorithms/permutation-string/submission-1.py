from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_1 = Counter(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            count_2 = Counter(s2[l: r + 1])
            if count_2 == count_1:
                return True
            
            r += 1
            l += 1

        return False