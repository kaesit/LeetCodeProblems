class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
          lngth = len(s)
          x = set(wordDict)
          answer:bool = False 
          res = [False] * (lngth + 1)
          res[0] = [""]
          for i in range(1, lngth + 1):
               for j in range(i):
                    if res[j] and s[j:i] in x:
                         res[i] = True
                         break
          return res[lngth]