from ast import List
def removeDuplicates(self, nums: List[int])-> int:
    l = 1
    for r in range(1, len(nums)):
        if(nums[i]!=nums[i-1]):
            nums[l] = nums[r]
            l+=1
    return l