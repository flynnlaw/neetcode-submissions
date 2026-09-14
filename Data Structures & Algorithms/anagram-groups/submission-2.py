from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sortedword = ''.join(sorted(word))
            groups[sortedword].append(word)
        
        return list(groups.values())
            