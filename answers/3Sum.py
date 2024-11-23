class Solution:
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