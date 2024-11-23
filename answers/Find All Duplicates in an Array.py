class Solution:
     def findDuplicates(self, nums: List[int]) -> List[int]:
          seen = set()
          seen_add = seen.add
          # adds all elements it doesn't know yet to seen and all other to seen_twice
          seen_twice = set( x for x in nums if x in seen or seen_add(x) )
          
          # turn the set into a list (as requested)
          return list( seen_twice )  