from typing import List
class Solution:
     def findPeakElement(self, nums: List[int]) -> int:
          ln = len(nums)
          def largest(nums,  n,  i):
               # Last index return the element
               if (i == n - 1):
                    return nums[i]
               
               # Find the maximum from rest of the array
               recMax = largest(nums, n, i + 1)
               
               # Compare with i-th element and return
               return max(recMax, nums[i])

          def search(nums, mx):
               n = len(nums)
               left = 0
               right = n - 1
               mid = (left - right) // 2
               while left <= right:
                    if nums[mid] == mx:
                         return mid
                    elif nums[mid] < mx:
                         right = mid + 1
                    else:
                         right = mid - 1
               return -1
          mx = max(nums)
          index = nums.index(mx)
          return abs(index)
          #return index



nums = [1,2,3,1]
nums2 = [2,1]
n = len(nums2)
print(max(nums2))
print(Solution().findPeakElement(nums))   
print(Solution().findPeakElement(nums2))