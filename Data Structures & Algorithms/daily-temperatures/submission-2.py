class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            r = i
            while temperatures[i] >= temperatures[r]:
                r += 1
                if r == len(temperatures):
                    break
            if r == len(temperatures):
                res.append(0)
            else:
                res.append(r - i)
        return res
            