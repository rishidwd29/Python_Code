arr = [1,8,6,2,5,4,8,3,7]
print(arr.index(max(arr)))
# def maxArea(self, height):
#     areamax= 0
#     for l in range(len(height)):
#         for r in range(l+1, len(height)):
#             area = (r-l)*(min(height[l],height[r]))
#             areamax = max(area,areamax)
#     return areamax

def maxArea(self, height):
    areamax = 0
    l,r = 0, len(height)-1
    while(l<r):
        area = (r-1) * (min(height[l], height[r]))
        areamax = max(area,areamax)
        if(height[l]<height[r]):
            l = l+1
        else:
            r = r-1
    return areamax
    