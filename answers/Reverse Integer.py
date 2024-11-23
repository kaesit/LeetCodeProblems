class Solution:
     def reverse(self, x: int) -> int:
          string_number = str(x)
          int32_t_positive = 2147483647
          int32_t_negative = -2147483648
          res = 0
          if x > 0:
               res = string_number[::-1]
               res = int(res)
               if res >= int32_t_positive:
                    res = 0
               else:
                    res = string_number[::-1]
          elif x < 0:
               res = string_number.replace(string_number[0], "")
               res = res[::-1]
               res = int(res)
               res = -res
               if res <= int32_t_negative:
                    res = 0
               else:
                    res = res
          return int(res)
   
   