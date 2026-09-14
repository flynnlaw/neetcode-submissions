class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        numsSet = set(nums)
        sortedSet = sorted(numsSet)

        longestseq = 1
        currentseq = 1
        prev = sortedSet[0]

        for i in range (1, len(sortedSet)):
            if sortedSet[i] == prev + 1:
                currentseq += 1
                prev = sortedSet[i]
            else:
                if currentseq > longestseq:
                    longestseq = currentseq
                prev = sortedSet[i]
                currentseq = 1

        return max(longestseq, currentseq)
                
