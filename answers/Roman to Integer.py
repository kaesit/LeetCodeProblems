class Solution:
     def romanToInt(self, s: str) -> int:
          result = 0
          dicti = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
          dicti.get("I")
          for i in range(len(s) - 1):
               if dicti[s[i]] < dicti[s[i + 1]]:
                    result -= dicti[s[i]]
               elif dicti[s[i]] > dicti[s[i + 1]]:
                    result += dicti[s[i]]
               elif dicti[s[i]] == dicti[s[i]]:
                    result += dicti[s[i]]
               elif dicti[s[i]] >= dicti[s[i + 1]]:
                    result = dicti[s[i + 1]] - dicti[s[i]]
                   
          return result + dicti[s[-1]]

print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("LV"))
print(Solution().romanToInt("LVIV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("CM"))


class Solution2:
     def romanToInt(self, s: str) -> int:
          result = 0
          dicti = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
          dicti.get("I")
          s = s.replace("IV", "IIII")
          s = s.replace("IX", "IIIIIIIII")
          s = s.replace("XL", "XXXX")
          s = s.replace("XC", "LXXXX")
          s = s.replace("CD", "CCCC")
          s = s.replace("CM", "DCCCC")
          for new_number in s:
               result +=dicti[new_number]

          return result

print(Solution2().romanToInt("MCMXCIV"))
print(Solution2().romanToInt("LV"))
print(Solution2().romanToInt("III"))
print(Solution2().romanToInt("IX"))