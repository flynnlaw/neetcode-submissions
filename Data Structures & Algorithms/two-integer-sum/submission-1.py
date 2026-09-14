class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = defaultdict(int)
        returnlist = []
        for index in range(0, len(nums)):
            num = nums[index]
            difference = target - num
            if difference in numsdict.keys():
                returnlist.append(numsdict[difference])
                returnlist.append(index)
                return returnlist
            else:
                numsdict[num] = index
        
        return returnlist.sort()