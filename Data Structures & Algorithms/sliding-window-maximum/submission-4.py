class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []

        for i in range (len(nums)):
            heapq.heappush(window, (-nums[i],i))
            if i >= k-1:
                while window[0][1] <= i-k:
                    heapq.heappop(window)
                res.append(-window[0][0])
        return res


        
