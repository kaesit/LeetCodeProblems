class Solution:
     def threeSumClosest(self, nums: List[int], target: int) -> int:
          nums.sort()
          ln = len(nums)
          total = 0
          closest_sum = float('inf')
          """if target == 0:
               total = 1
               return total"""
          for i in range(ln - 2):
               left, right = i + 1, ln - 1
               while left < right:
                    total = nums[i] + nums[left] + nums[right]

                    if total == target:
                         return total

                    if abs(total - target) < abs(closest_sum - target):
                         closest_sum = total

                    if total < target:
                         left += 1

                    elif total > target:
                         right -= 1
                    else:
                         return total
          return closest_sum