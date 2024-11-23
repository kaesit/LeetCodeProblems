from typing import List
from matplotlib import pyplot

array = [2,3,6,7,12,4,5]
array2 = [2,2]
array3 = [1,1]

class Solution():
     def find_area(height:List) -> int:
          n = len(height)
          left = 0
          right = n - 1
          res = 0
          while left <= right:
               res = max(res, (right - left) * min(height[left], height[right]))
               if height[left] < height[right]:
                    left += 1
               else:
                    right -= 1
          #print(temp)
          return res
          
print(Solution.find_area(array))

class Solution2:
     def maxArea(self, height: List[int]) -> int:
          res = 0
          n = len(height)
          #largest_element = max(height, lambda x:x)
          for i in range(0,n-1):
               if height[i] == height[i + 1] and n <= 2:
                    return height[i]
               i+=1
        

          return res
     def find_index(self, arr, element:int):
          left = 0
          right = len(arr) - 1
          while left <= right:
               mid = left + (right - left) // 2
               if arr[mid] == element:
                    return mid
               elif arr[mid] < element:
                    left = mid + 1
               else:
                    right = mid - 1
          return -1
     
print(Solution2().maxArea(array))
print(Solution2().maxArea(array2))
print(Solution2().maxArea(array3))



import matplotlib.pyplot as plt
# generate some data
x = [1, 2, 3, 4, 5, 6, 7]
y = [2,3,6,7,12,4,5]
# create the bar plot
plt.bar(x, array)
# add a title and labels for the x and y axes
plt.title('Bar Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
# show the plot
plt.show()
