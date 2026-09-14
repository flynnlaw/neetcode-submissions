class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            capacity = (r-l) * min(heights[l], heights[r])

            if res < capacity:
                res = capacity
            
            if heights[l] > heights[r]:
                r -=1
            elif heights[l] < heights[r] or heights[l] == heights[r]:
                l +=1 
        
        return res


