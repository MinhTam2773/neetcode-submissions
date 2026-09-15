from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        for i in range(0,k):
            most = max(count, key=count.get)
            res.append(most)
            count.pop(most, None)
        return res