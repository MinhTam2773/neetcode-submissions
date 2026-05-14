class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            if (nums[i - 1] == num and i > 0):
                continue
            while l < r:
                cur = num + nums[l] + nums[r]
                if cur>0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], num])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

        return res