class Solution:
     def maxArea(self, height: List[int]) -> int:
          n = len(height)
          left = 0
          right = n - 1
          res = 0
          while left <= right:
               res = max(res, (right - left) * min(height[left], height[right]))
               if height[left] < height[right]:
                    left += 1
               else:
                    right -= 1
               #print(temp)
          return res