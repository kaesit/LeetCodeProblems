def get_permutations(nums, p_list=[], temp_items=[]):
     if not nums:
          return
     elif len(nums) == 1:
          new_items = temp_items+[nums[0]]
          p_list.append(new_items)
          return
     else:
          for i in range(len(nums)):
               temp_nums = nums[:i]+nums[i+1:]
               new_temp_items = temp_items + [nums[i]]
               get_permutations(temp_nums, p_list, new_temp_items)

     return p_list
nums = [1,2,3]
nums2 = [0, 1]
p_list = []

print(get_permutations(nums, p_list))


"""def permutate(l:list):
     for i, x in enumerate(l):
          for y in l[i + 1:]:
               yield x, y
     return list

array = [0, 1]
if __name__ == '__main__':
    print(list(permutate(list('abcd'))))
    print(list(permutate([1, 2, 3, 4])))"""

