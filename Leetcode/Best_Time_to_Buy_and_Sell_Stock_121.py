def maxProfit( prices ) -> int:
    if not prices:
        return 0
    mn = prices[0]
    mx =0
    for p in range(1,len(prices)):
        mx = max(mx , prices[p]-mn)
        mn = min(mn,prices[p])
    return mx

prices = [3,2,6,5,0,3]
print(maxProfit(prices))



