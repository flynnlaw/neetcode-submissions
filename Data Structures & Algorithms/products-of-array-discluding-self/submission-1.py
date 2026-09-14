class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        res = [0] * len(nums)
        
        pre[0] = 1
        suf[len(nums)-1] = 1

        for number in range (1, len(nums)):
            pre[number] = nums[number-1] * pre[number-1]

        for number in range(len(nums) - 2, -1, -1):
            suf[number] = nums[number+1] * suf[number+1]
        
        for number in range (0, len(nums)):
            res[number] = pre[number] * suf[number]

        return res

