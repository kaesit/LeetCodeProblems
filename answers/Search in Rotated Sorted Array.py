class Solution:
     def search(self, nums: List[int], target: int) -> int:
          #nums.sort()
          if target in nums:
               return nums.index(target)
          else:
               return -1
          return -1