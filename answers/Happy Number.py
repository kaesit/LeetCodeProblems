class Solution:
     def isHappy(self, n: int) -> bool:
          i = 0
          c = False
          res = 0
          while n > 0:
               i = n % 10
               res = res + i * i
               n = n // 10
          if res == 1:
               c = True
          elif res == 7:
               c = True
          elif res < 10:
               c = False
          else:
               """for i in str(temp):
                    res += int(i) ** 2
                    if res == 1:
                         c = True
                         break
                    elif res != 1:
                         c = False
                    else:
                         self.isHappy(n)
                         c = False"""
               return self.isHappy(res)
          return c
        