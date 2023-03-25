# def maxProfit(self, prices) -> int:
#     p = 0
#     lb = 0
    
#     if(prices[0]!=max(prices)):
#         lb = prices[0]
#         for i in prices:
#             if(lb<prices[i]):
#                 lp = sellProfit(lb,prices[i])
#                 p = p + lp
#             if(lp>prices[i]):
#                 lb = prices[i]
#     else:
#         lb = prices[1]
#         i = 1
#         for i in range(len(prices)-1):
#             if(lb<prices[i]):
#                 lp = sellProfit(lb,prices[i])
#                 p = p + lp
#             if(lp>prices[i]):
#                 lb = prices[i]
#     return p
            
# def sellProfit(purchased, selling):
#     result = selling - purchased 
#     return result

# prices = [7,1,5,3,6,4]
# result = maxProfit(0, prices)
# print(result)


from ast import List
def maxProfit(self, prices: List[int]):
    max_profit = 0
    for i in range(1,len(prices)):
        if(prices[i]>prices[i-1]):
            max_profit += prices[i] - prices[i-1]
    return max_profit
    

    