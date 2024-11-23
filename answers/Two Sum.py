"""class Solution():
    def twoSum(self, nums, target):
        new_nums = []
        for i in range(0, len(nums) - 1):
            if target == nums[i] + nums[i + 1]:
                new_nums = [int(nums.index(nums[i])), int(nums.index(nums[i + 1]))]
            elif target == nums[i - 1] + nums[i + 1]:
                new_nums = [int(nums.index(nums[i])), int(nums.index(nums[2]))]
            elif target == nums[0] + nums[2]:
                new_nums = [int(nums.index(nums[0])), int(nums.index(nums[2]))]
        if target == nums[0]  + nums[1] and nums[0] == nums[1]:
            new_nums = [0, 1]
        return (new_nums) 

nums1 = [3, 3]

a = Solution()
a.twoSum(nums1, 6) """

class Solution:
     def twoSum(self, nums, target):
          hash_map = {} 
          for i, num in enumerate(nums): 
               hash_map[num] = i 
          for i, num in enumerate(nums): 
               if target - num in hash_map and hash_map[target - num] != i: 
                    return [i, hash_map[target - num]] 
               
          return []

        