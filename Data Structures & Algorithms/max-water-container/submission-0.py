class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water min(height)*(i1-i2)
        i,j=0,len(heights)-1
        max_water=0
        while i<len(heights) and j>=0:
            water=min(heights[i],heights[j])*abs(j-i)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
            max_water=max(water,max_water)
        return max_water