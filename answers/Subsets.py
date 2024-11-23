class Solution:
     def subsets(self, nums: List[int]) -> List[List[int]]:
          res = [[]]
          for num in nums:
               res += [temp + [num] for temp in res]
          return res