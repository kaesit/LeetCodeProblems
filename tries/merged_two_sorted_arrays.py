from typing import Optional
class Solution:
     def mergeTwoLists(self, list1: list, list2: list) -> list:
          list1.sort()
          list2.sort()
          res_lst = list1 + list2
          res_lst.sort()
          return res_lst
     

l1, l2 = [1, 2, 3], [2, 5, 5]
l3, l4 = [], [0]
print(Solution().mergeTwoLists(l1, l2))
print(Solution().mergeTwoLists(l3, l4))