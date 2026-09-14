class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numSet = defaultdict(int)

        for number in range (0,len(numbers)):
            numSet[numbers[number]] = number

        for i in range (0, len(numbers)):
            i1 = numbers[0]
            diff = target - i1
            if diff in numSet.keys():
                return [i+1, numSet[diff]+1]
            else:
                del numbers[0]
        
        return []
