class Solution:
     def lengthOfLastWord(self, s: str) -> int:
          a = s.split()
          n = len(a[-1])
          return n