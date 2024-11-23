class Solution:
     def singleNumber(self, nums: List[int]) -> int:
          n = len(nums)
          single_one = 0
          duplicate = set()
          duplicate_plus = duplicate.add
          duplicates = set( x for x in nums if x in duplicate or duplicate_plus(x) )
          if n == 1:
               single_one = nums[0]
          for i in range(0, n - 1):
               if nums[i] not in list(duplicates):
                    single_one = nums[i]
               elif nums[i + 1] not in list(duplicates):
                    single_one = nums[i + 1]
               

          return single_one