class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
          lngth = len(s)
          x = set(wordDict)
          res = [[] for _ in range(lngth + 1)]
          res[0] = [""]
          for i in range(1, lngth + 1):
               temp = []
               for j in range(i):
                    suffix = s[j:i]
                    if suffix in x:
                         for substring in res[j]:
                              temp.append(f"{substring}{' ' if substring else ''}{suffix}")
               res[i] = temp
          return res[lngth]
