from typing import List
from itertools import permutations
class Solution:
     def searchRange(self, nums: List[int], target: int) -> List[int]:
          nums.sort()
          start_at = -1
          n = len(nums)
          res = []
          if nums == []:
               res = [-1,-1]
          if target not in nums:
               res = [-1,-1]
          while True:
               try:
                    loc = nums.index(target,start_at+1)
               except ValueError:
                    break
               else:
                    res.append(loc)
                    start_at = loc
          return res
nums1, target1 = [5,7,7,8,8,10], 8
nums2, target2 = [5,7,7,8,8,10], 6
nums3, target3 = [], 0
nums4, target4 = [], 5


print(Solution().searchRange(nums1, target1))
print(Solution().searchRange(nums2, target2))
print(Solution().searchRange(nums3, target3))
print(Solution().searchRange(nums4, target4))

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

source = [1,2,3,4,7,7,8,8,10]
print(list_duplicates_of(source, 8))

arr = [4,5,6,7,0,1,2]
arr.sort()
print(arr.index(0))
arr_str = ''.join(str(x) for x in arr)
print(arr_str)
class Solution4():
     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
          #print(candidates)
          n = len(candidates)
          idx = 0
          t = 0
          sum_list = []
          if (target < 0):
               return []
          def find_number(index, total, list_):
               if index >= n:
                    if total == target:
                         sum_list.append(list_)
                    return
               find_number(index + 1, total, list_)
               if total + candidates[index] <= target:
                    find_number(index, total + candidates[index], list_ + [candidates[index]]) 
                    
          find_number(idx, t, []) 
          return sum_list 

array1, array2, array3 = [2,3,6,7], [2,3,5], []
print(Solution4().combinationSum(array1, 7))
print(Solution4().combinationSum(array2, 5))
perms = []

for i in range(1, len(arr_str)+1):
    for c in permutations(arr_str, i):
        perms.append("".join(c))

print(max(perms))

while True:
     arr = [4,5,6,7,0,1,2]
     target = int(input("Type a number: "))
     if target in arr:
          print(arr.index(target))
          input("")
          break
     else:
          print("Target is not in the list")
          continue
     