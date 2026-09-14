class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []

        for i in range (len(nums)):
            num1 = sortedNums[i]
            
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue

            l = i + 1
            r = len(nums)-1

            while l < r:
                current_sum = sortedNums[l] + sortedNums[r]
                if current_sum > -num1:
                    r -= 1  # Fixed: Decrease r to lower the sum
                elif current_sum < -num1:
                    l += 1  # Increase l to raise the sum
                else:
                    res.append([num1, sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1  # Fixed: Decrease r to move inward

                    # Fixed: Check l < r first, and use sortedNums
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1
                    while l < r and sortedNums[r] == sortedNums[r + 1]:
                        r -= 1
            
            
        return res




