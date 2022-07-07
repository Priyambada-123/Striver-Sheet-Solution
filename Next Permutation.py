class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length=len(nums)
        if length<=2:
            return nums.reverse()
        po=length-2
        while po>=0 and nums[po]>=nums[po+1]:
            po-=1
        if po==-1:
            return nums.reverse()
        for i in range(length-1,po,-1):
            if nums[po]< nums[i]:
                nums[po],nums[i]=nums[i],nums[po]
                break
        nums[po+1:]=reversed(nums[po+1:])