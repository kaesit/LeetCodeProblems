from typing import List
list1 = [2, 3, 5, 7, 9, 9, 11]
lng = len(list1) 

def remove_element(l:list, val:int) -> list:
     for i in range(lng - val):
          if l[i] == l[i + 1]:
               if l[i] and l[i + 1] == val:
                    l.remove(l[i + 1])
                    l.remove(l[i])
                    i+=1
               else:
                    break
               
          #i += 1
     return l

class Solution:
     def removeElement(self, nums: List[int], val: int) -> int:
          index = 0
          for i in range(len(nums)):
               if nums[i] != val:
                    nums[index] = nums[i]
                    index += 1
          return index
     
print(remove_element(list1, 9))
print()
Solution().removeElement(list1, 5)