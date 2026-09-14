class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n
        leftMax[0] = height[0]
        rightMax[n-1]= height[n-1]

        for i in range (0, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        for i in range (n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        for i in range (n):
            water += min(leftMax[i], rightMax[i]) - height[i]

        return water

