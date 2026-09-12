class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_seen_nums = set()

        for num in nums:
            if num in unique_seen_nums:
                return True
            unique_seen_nums.add(num)
        return False

        