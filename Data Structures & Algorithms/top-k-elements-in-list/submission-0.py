class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse= True)

    # Extract just the elements (keys) from the first k items
        return [sorted_items[i][0] for i in range(k)]







        