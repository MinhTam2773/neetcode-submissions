class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i,x in enumerate(nums):
            diff = target - x
            if diff in num_dict:
                return [num_dict[diff],i]

            num_dict[x] = i