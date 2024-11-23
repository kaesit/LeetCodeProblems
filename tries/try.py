"""
nums1, array2 = [2, 4], [1, 3]
first_element = nums1[0]
last_element = nums1[-1]
print(first_element)
print(last_element)
print(nums1.index(first_element))

test_list = [4, 5, 8, 9, 10, 17] 
 
# printing list 
print("The original list : " + str(nums1)) 
 
# Median of list 
# Using loop + "~" operator 
nums1.sort() 
mid = len(nums1) // 2
res = (nums1[mid] + nums1[~mid]) / 2
 
# Printing result 
print("Median of list is : " + str(res)) 


stri = ["fgdf", "gdfgd", "fgdfgfd"]
print(f'"{stri[2]}"')"""


"""class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
    
        k -= 1
        numbers = list(range(1, n + 1))
        permutation = []

        for i in range(n, 0, -1):
            index = k // factorials[i - 1]
            k %= factorials[i - 1]
            permutation.append(numbers[index])
            numbers.pop(index)
    
        return ''.join(map(str, permutation))
   
print(Solution().getPermutation(3, 3))"""

numbers = [1, 5, 6, 1, 2, 3]
numbers.sort()
print(numbers)