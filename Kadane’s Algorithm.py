class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma=-9999999999999
        mp=0
        for i in range(len(nums)):
            mp+=nums[i]
            if mp<nums[i]:
                mp=nums[i]
            if ma<mp:
                ma=mp
        return ma