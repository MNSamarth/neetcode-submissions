class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        maxprofit=0
        while(sell<len(prices)):
            if prices[sell]>prices[buy]:
                profit=prices[sell]-prices[buy]
                maxprofit=max(maxprofit,profit)
            else:
                buy=sell
            sell+=1
        return maxprofit
