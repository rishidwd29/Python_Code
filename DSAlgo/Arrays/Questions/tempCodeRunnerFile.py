def maxProfit(prices):
    p = 0
    lb = 0
    
    if(prices[0]!=max(prices)):
        lb = prices[0]
        
        
        for i in prices:
            if(lb<prices[i]):
                lp = sellProfit(lb,prices[i])
                p = p + lp
            if(lp>prices[i]):
                lb = prices[i]
    else:
        lb = prices[1]
        i = 1
        for i in prices:
            if(lb<prices[i]):
                lp = sellProfit(lb,prices[i])
                p = p + lp
            if(lp>prices[i]):
                lb = prices[i]
            
def sellProfit(purchased, selling):
    result = selling - purchased 
    return result