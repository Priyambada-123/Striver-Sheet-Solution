class Solution:
    def merge(self, Intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in sorted(Intervals):
            if(res and res[-1][1]>=i[0]):
                res[-1][1]=max(res[-1][1],i[1])
            else:
                res.append(i)
        return res
                