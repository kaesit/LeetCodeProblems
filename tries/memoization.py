mem = {}

a = "gffdgd"

mem[0] = a

n = len(a)

"""for word in a:
     #word.split()
     print(word)
     if word[-1] == word[0]:
          mem[n] = word"""
          
for i in range(0, n):
     mem


b = str(mem.get(0))
letter = [x for x in b]

print(letter)

print(mem.items())

mc = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
if 2 in mc:
     temp = mc.get(2)
     letter = [x for x in temp]
print(letter)


dp = [[False for _ in range(len(a))] for _ in range(len(a))]
#print(dp)

class Solution:
     def longestPalindrome(self, s: str) -> str:
          mem = {}
          n = len(s)
          if s[0] == s[::-1]:
               return s
          if 1 <= n and n <= 1000:
               for i in range(0, n):
                    mem[i] = s
          return mem[n - 1]
               
print(Solution().longestPalindrome(a))
print(Solution().longestPalindrome("bab"))


"""for i in range(0, n - 1):
               word = s[i] + s[i + 1]"""
          #print(word)
          
find = ['house', 'John', 'garden']
s = 'MynameisJohn'
results = [item for item in find if item in s]
print( results )