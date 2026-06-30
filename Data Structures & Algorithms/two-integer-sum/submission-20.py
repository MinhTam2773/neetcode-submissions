class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, x in enumerate(nums):
            remaining = target - x
            if remaining in num_dict:
                return [num_dict[remaining], i]

            num_dict[x] = i