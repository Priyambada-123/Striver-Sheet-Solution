class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        p=""
        for i in range(n):
            if i not in nums:
                p+=str(i)
        if n not in nums:
            p+=str(n)
        
        return int(p)