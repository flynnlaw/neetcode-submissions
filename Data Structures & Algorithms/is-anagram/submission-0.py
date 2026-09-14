class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        llist1 = defaultdict(int)
        llist2 = defaultdict(int)
        for letter in s:
            llist1[letter] += 1
        for letter in t:
            llist2[letter] += 1
        
        return llist1 == llist2
        

