class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    p1 = 0
    res = 0

    for p2 in range(len(s)):

      while s[p2] in seen:
        seen.remove(s[p1])
        p1 += 1

      seen.add(s[p2])
      res = max(res, p2 - p1 + 1)

    return res
