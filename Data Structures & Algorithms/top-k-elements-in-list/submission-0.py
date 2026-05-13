class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        sorted_items = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)
        sorted_keys = [item[0] for item in sorted_items]

        return sorted_keys[:k]