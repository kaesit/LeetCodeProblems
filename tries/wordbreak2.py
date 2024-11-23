from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        lngth = len(s)
        x = set(wordDict)
        res = [[] for _ in range(lngth + 1)]
        res[0] = [""]
        for i in range(1, lngth + 1):
            temp = []
            for j in range(i):
                suffix = s[j:i]
                if suffix in x:
                    for substring in res[j]:
                        temp.append(f"{substring}{' ' if substring else ''}{suffix}")
            res[i] = temp
        return res[lngth]

str1, dict1 = "catsanddog", ["cat","cats","and","sand","dog"]
str2, dict2 = "pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]
str3, dict3 = "catsandog", ["cats","dog","sand","and","cat"]

print(Solution().wordBreak(str1, dict1))
print(Solution().wordBreak(str2, dict2))
print(Solution().wordBreak(str3, dict3))



class Solution2:
    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        lngth = len(s)
        x = set(wordDict)
        answer:bool = False 
        res = [False] * (lngth + 1)
        res[0] = [""]
        for i in range(1, lngth + 1):
            for j in range(i):
                if res[j] and s[j:i] in x:
                    res[i] = True
                    break
        return res[lngth]
    
print(Solution2().wordBreak2(str1, dict1))
print(Solution2().wordBreak2(str2, dict2))
print(Solution2().wordBreak2(str3, dict3))

lngth = len(str1)
res = [False] * (lngth + 1)
#print(res[lngth])