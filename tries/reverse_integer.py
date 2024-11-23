class Solution:
     def reverse(self, x: int) -> int:
          string_number = str(x)
          int32_t_positive = 2147483647
          int32_t_negative = -2147483648
          res = ""
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
               res = -(res)
               if res <= int32_t_negative:
                    res = 0
               else:
                    res = res
            #res[0:1 + 1] = reversed(res[0:1 + 1])
          return int(res)
   
print(Solution().reverse(-1534236469))
print(Solution().reverse(-123))
print(Solution().reverse(1534236469))
print(Solution().reverse(123))
"""ns = -4
nsn = str(ns)
print(nsn[0:])
l = [0,1,2,3,4,5,6,7]
l[0:1 + 1] = reversed(l[0:1 + 1])
print(l)"""

string = "dgfd"
string.replace(string[0], "")
print(string)

if -5 > -6:
     print(True)