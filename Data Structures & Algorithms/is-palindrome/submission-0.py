class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = re.sub(r'[^a-zA-Z0-9]', '', s)
        sentence = stripped.lower()
        i = 0
        j = len(sentence) - 1

        while i < j:
            if sentence[i] != sentence[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True
