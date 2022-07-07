class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        mi=100000
        pri=0
        for i in range(n):
            if mi>prices[i]:
                mi=prices[i]
            if pri<prices[i]-mi:
                pri=prices[i]-mi
        return pri