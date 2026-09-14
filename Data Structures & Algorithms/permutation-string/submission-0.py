class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tocheck = sorted(s1)
        for l in range (len(s2)):
            if s2[l] in s1: 
                snapshot = sorted(s2[l:l+len(s1)])
                if tocheck == snapshot:
                    return True

        return False


