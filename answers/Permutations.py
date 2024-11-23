class Solution(object):
     def permute(self, nums: list[int]) -> list[int]:
          permutedList = []
          def recursive(new_p, aft):
               if not aft:
                    # No more elements to permute, add the current path to the result
                    permutedList.append(new_p)
                    return
               for i in range(len(aft)):
                    # Recur with the current element added to the path
                    # and the remaining elements excluding the current one
                    recursive(new_p + [aft[i]], aft[:i] + aft[i+1:])
      
            #yield nums[i] + nums[0:1] + nums[i:]
               #a.append(nums[-1::])
            
            #a.append(nums)
            #a.insert((i), [nums[i - 1], nums[i]])
            #a.insert((i), [nums[i + 1], nums[i], nums[i - 1]])
      
          recursive([], nums)
          return permutedList
      
   
array = [0, 1]
print(Solution().permute(array))
array2 = [1]
print(Solution().permute(array2))
array3 = [1, 2, 3]
print(Solution().permute(array3))