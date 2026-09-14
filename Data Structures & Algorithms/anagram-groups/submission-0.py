from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = self.get_key(word)
            groups[key].append(word)

        return list(groups.values())
    
    def get_key(self, string: str):
        counts = [0] * 26

        for letter in string:
            counts[ord(letter) - ord('a')] += 1

        return tuple(counts)