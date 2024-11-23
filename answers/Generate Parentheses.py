class Solution:
     def generateParenthesis(self, n: int) -> List[str]:
          res = []
          def combination(left, right, s="", answer=res):
               if left == 0 and right == 0:
                    answer.append(s)
               if left > right or left < 0 or right < 0:
                # wrong
                    return
               s += '('
               combination(left - 1, right, s, answer)
               s = s[:-1]
               s += ')'
               combination(left, right - 1, s, answer)
               s = s[:-1]
        
          if 1 <= n <= 8:
               if n == 1:
                    res.append("()")
               else:
                    combination(n, n)

          return res
            
        
        