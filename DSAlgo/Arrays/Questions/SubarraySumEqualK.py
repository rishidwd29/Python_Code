# def subarraySum(self, nums ,k):
#     c = 0
#     l,r = 0, l+1
#     while(r<len(nums)):
#         if(nums[l]+nums[r] < k):
#             r = r+1
#         elif(nums[l]+nums[r] > k):
#             l = l+1
#         elif(l==r):
#             if(nums[r] ==k):
#                 c = c+1
#                 r = r+1
#             else:
#                 r =r+1
#         elif(nums[l]+nums[r] == k):
#             c = c+1
#             r = r+1
#     return c
def subarraySum(self, nums , k):
    res = 0
    curSum = 0
    prefixSums = {0:1}
    
    for n in nums:
        curSum  = curSum + n
        diff  = curSum -k
        res = res + prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
    return res