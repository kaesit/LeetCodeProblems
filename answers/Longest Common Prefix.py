class Solution:
     def longestCommonPrefix(self, strs: List[str]) -> str:
          res = ""
          strs.sort()
          first_let = strs[0]
          last_let = strs[-1]
          print(first_let)
          print(last_let)
          for i in range(min(len(first_let), len(last_let))):
               if first_let[i] != last_let[i]:
                    return res
               res += first_let[i]
          return res