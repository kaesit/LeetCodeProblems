class Solution:
     def isHappy(self, n: int) -> bool:
          l = 0
          sum = 0
          while n > 0:
               l = n % 10
               sum = sum + l * l
               n = n // 10
          if sum == 1:
               return True
          elif sum == 7: return True #only one happy number(7) b/w 1 and 10
          elif sum < 10: return False
          else:
               return self.isHappy(sum)

print(Solution().isHappy(19))