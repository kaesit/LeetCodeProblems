class Solution:
     def threeSum(self, nums: list[int]) -> list[list[int]]:
          res = []
          nums.sort()
          total = 0
          for i in range(len(nums)):
               if i > 0 and nums[i] == nums[i - 1]:
                    continue
               
               j = i + 1
               k = len(nums) - 1
               
               while k < len(nums):
                    total = nums[i] + nums[j] + nums[k]
                    if total > 0:
                         k -= 1
                    elif total < 0:
                         j += 1
                    else:
                         res.append([nums[i], nums[j], nums[k]])
                         j += 1
                         

                         while nums[j] == nums[j - 1] and j < k:
                              j += 1
           
          """for i in range(0, len(nums) - 3):
               total = 0
               total += nums[i] + nums[i + 1] + nums[i + 2]
               if total == 0:
                    res.append([nums[i], nums[i + 1], nums[i + 2]])"""
               #print(total)
          return res



def triple_sum_of_a_list(nums:list[int], res):
     i = 0
     j = 0
     k = 0
     total = 0
     for i in range(len(nums) - 2):
          #total = 0
          total+=nums[i] + nums[i + 1] + nums[i + 2]
          if total == 0:
               res.append([nums[i], nums[i + 1], nums[i + 2]])
    
     print(res)

array = [-1,0,1,2,-1,-4]
#triple_sum_of_a_list(array, [])
#print(Solution().threeSum(array))



class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    res.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[+1]:
                        k -= 1
        return res
print(Solution2().threeSum(array))

















class mySolution():
     def threeSum(self, nums: list[int]) -> list[list[int]]:
          res = []
          nums.sort()
          length = len(nums)
          for i in range(length):
               if i != 0 and nums[i] == nums[i - 1]:
                    continue
               
               j = i + 1
               k = length - 1
               if i!=j and i!=k and j!=k:
                    pass
               while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    #print(total)
                    if total < 0:
                         j += 1
                    elif total > 0:
                         k -= 1
                    else:
                         res.append([nums[i], nums[j], nums[k]])
                         j+=1
                         k-=1
                         while j < k and nums[j] == nums[j - 1]:
                              j+=1
                         while j < k and nums[k] == nums[+1]:
                              k-=1
          return res
               
print(mySolution().threeSum(array))