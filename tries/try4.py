
class Solution:
     def divide(self, dividend: int, divisor: int) -> int:
          res, controller = 0, 0
          
          division = dividend / divisor
          #res = int(self.truncate_float(division, 0))
          controller = int(self.truncate_float(division, 0))
          if controller >= 2147483648:
               res = 2147483648 - 1
          elif controller < -2147483648:
               res = -2147483648
          else:
               res = int(self.truncate_float(division, 0))
          return res
     def truncate_float(self, float_number, decimal_places):
          multiplier = 10 ** decimal_places
          return int(float_number * multiplier) / multiplier

print(Solution().divide(2147483648, 3))


a = [12, 43, 43, 56, 12]
new_a = str(a)
new_a = new_a.replace("43", "")
print(new_a)


"""def truncate_float(float_number, decimal_places):
              multiplier = 10 ** decimal_places
              return int(float_number * multiplier) / multiplier

float3 = 3.14159
result = int(truncate_float(float3, 0))

print(result)

res = -2147483648 / -1
print(res)"""