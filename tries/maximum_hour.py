from typing import Final

stre = "?4:26"
stre2 = "??:26"
stre3 = "??:??"
stre4 = "1?:??"
stre5 = "15:??"

MAXIMUM_TIME:Final = "23:59"
MINUMUM_TIME:Final = "00:00"
class Solution:
     def sol(self, s:str) -> str:

          mem = ["1", "2", "3", "5", "9"]
          if s[1] != "?":
               if int(s[1]) < 9:
                    s = s.replace(s[0], mem[0], 1)
          if s[0] and s[1] == "?" and s[3] and s[4] !="?":
               s = s.replace(s[0], mem[1], 1)
               s = s.replace(s[1], mem[2], 1)
          if s[0] or s[1] != "?" and s[3] and s[4] =="?":
               s = s.replace(s[3], mem[1], 1)
               s = s.replace(s[4], mem[2], 1)
          if s[0] and s[1] and s[3] and s[4] == "?":
               s = "23:59" 
          print(s)
               
if __name__ == '__main__':
     Solution().sol(stre)
     Solution().sol(stre2)
     Solution().sol(stre3)
     Solution().sol(stre4)
     Solution().sol(stre5)