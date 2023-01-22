def maxProfit(self, prices: List[int]) -> int:
        #[7,1,5,3,6,4]
        largestProfit =0
        minSofar = float("inf")
        
        for i in range(0,len(prices)):
            if prices[i]< minSofar:
                minSofar=prices[i]
            else:
                largestProfit = max(largestProfit, prices[i] - minSofar)
        return largestProfit
        