class Solution:
     def findPeakElement(self, nums: List[int]) -> int:
          mx = max(nums)
          index = nums.index(mx)
          return abs(index)