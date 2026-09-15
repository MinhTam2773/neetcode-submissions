from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        sorted_count = sorted(count.items(), key=lambda kv: kv[1])

        for i in range(0, k):
            res.append(sorted_count[len(sorted_count) - 1 - i][0])
        return res