class Solution:
     def plusOne(self, digits: List[int]) -> List[int]:
          adding = ""
          res = 0
          string_number = ""
          num_list_string = map(str, digits)
          string_number = adding.join(num_list_string)
          string_number = int(string_number)
          string_number += 1
          res = [int(x) for x in str(string_number)]
          return res