from typing import List
class Solution:
     def sortColors(self, nums: List[int]) -> None:
          def sorting(arr:List[int]):
               for i in range(1, len(arr)):
                    key = arr[i]
                    j = i - 1
                    while j >= 0 and key < arr[j]:
                         arr[j + 1] = arr[j]
                         j -= 1
                    arr[j + 1] = key
          res = sorting(nums)
          return res
     
arr = [2,0,2,1,1,0]
print(Solution().sortColors(arr))

def sorting(arr:List[int]):
     n = len(arr)
     for i in range(n):
          min_index = i
          for j in range(i + 1, n):
               if arr[j] < arr[min_index]:
                    min_index = j
          arr[j], arr[min_index] = arr[min_index], arr[j]
     return arr

print(sorting(arr))

def insertion_sort(arr):
     for i in range(1, len(arr)):
          key = arr[i]
          j = i - 1
          while j >= 0 and key < arr[j]:
               arr[j + 1] = arr[j]
               j -= 1
          arr[j + 1] = key

insertion_sort(arr)
print(arr)