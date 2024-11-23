class Solution():
     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
          nums1.extend(nums2)
          nums1.sort()
          result = 0
          med = len(nums1) // 2
          result = (nums1[med] + nums1[~med]) / 2
          
          return result
     
array1, array2 = [2, 4], [1, 3]
array3, array4 = [1, 5], [2]
print(Solution().findMedianSortedArrays(array1, array2))
print(Solution().findMedianSortedArrays(array3, array4))   