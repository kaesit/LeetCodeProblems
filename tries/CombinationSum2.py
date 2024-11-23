class Solution():
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
                         if sum_list[index] == sum_list:
                              sum_list.pop(index)
                    return
               find_number(index + 1, total, list_)
               if total + candidates[index] <= target:
                    find_number(index, total + candidates[index], list_ + [candidates[index]]) 
                    
          find_number(idx, t, []) 
          """for i in range(0, n):
               new_list.append(candidates[i])
               #for x in len(res):
               sum_list.append([new_list[i]])
                    
                    #print(total)
               #total.insert(i, ([candidates[i]], candidates[i:] + candidates[i+1:]))"""
               
          return sum_list 
     

array1, array2, array3, array4 = [1, 2, 2, 5, 3], [2,3,6,7], [2,3,5], []
print(Solution().combinationSum(array1, 5))

