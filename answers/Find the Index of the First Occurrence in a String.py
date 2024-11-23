class Solution:
     def strStr(self, haystack: str, needle: str) -> int:
          index = 0
          if 1 <= len(haystack) and len(needle) <= 104:
               index = haystack.find(needle)
          return index