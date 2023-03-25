from ast import List
def removeDuplicates(self, nums):
    
    for i in range(1, len(nums)):    
        if(nums[i]==nums[i-1]):
            nums.remove(nums[i])
    return nums
result = removeDuplicates(0,[1,1,2])
print (result)