from typing import List
class Solution:
     def generateParenthesis(self, n: int) -> List[str]:
          
          def replacing(n:int):
               pass
          res = []
          a = "".join("()")
          if 1 <= n <= 8:
               if n == 1:
                    res.append("()")
               else:
                    for i in range(n+2):
                         a = " ".join(f"{('(())' * i)}")
                         #res.insert(i, "()")
               res.append(a)

          return res
     
print(Solution().generateParenthesis(3))



class Solution2:
     def generateParenthesis(self, n: int) -> List[str]:
          def replacing(n:int):
               pass
     
print(Solution2().generateParenthesis(3))

def generateParenthesis(left, right, s, answer):
    # terminate
    if left == 0 and right == 0:
        answer.append(s)
    if left > right or left < 0 or right < 0:
        # wrong
        return
    s += '{'
    generateParenthesis(left - 1, right, s, answer)
    s = s[:-1]
    s += '}'
    generateParenthesis(left, right - 1, s, answer)
    s = s[:-1]


n = 3
# list ans is created to store all the possible valid
# combinations of the parentheses.
ans = []
s = ""
# initially we are passing the counts of open and close
# as 0, and the string s as an empty string.
generateParenthesis(n, n, s, ans)
# Now, here we print out all the combinations.
print(ans)