class Solution:
     def letterCombinations(self, digits: str) -> List[str]:
          mc = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
          res = []
          if digits in mc:
               temp = mc.get(digits)
               letter = [x for x in temp]
               return letter
          if digits == "":
               return []
          def recursive(combination, next_digits):
               if len(next_digits) == 0:
                    res.append(combination)
               else:
                    for letter in mc[next_digits[0]]:
                         recursive(combination + letter, next_digits[1:])
          recursive("", digits)
          return res