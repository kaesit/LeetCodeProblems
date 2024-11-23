from typing import List

class Solution():
     def missNumber(self, nums: List[int]) -> int:
          n = len(nums)
          for i in range(0, n):
               n += i - nums[i]
          return n
     
arr = [3,0,1]
arr2 = [9,6,4,2,3,5,7,0,1]
arr3 = [0,1]
print(Solution().missNumber(arr))
print(Solution().missNumber(arr2))
print(Solution().missNumber(arr3))