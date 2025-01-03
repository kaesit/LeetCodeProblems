class Solution:
     def mySqrt(self, x: int) -> int:
          left = 0
          right = x
          if ((2**31) - 1) >= x >= 0:
               while left <= right:
                    mid = (left + right) // 2
                    if mid * mid < x:
                         left = mid + 1
                    elif mid * mid > x:
                         right = mid - 1
                    else:
                         return (mid)
          return right