
def subArray(arr, n):
     best_sum = float('-inf')
     current_sum = 0
     for x in arr:
          current_sum = max(x, current_sum * x)
          best_sum = max(best_sum, current_sum)
     return best_sum

            
# Driver program
arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)
print ("All Non-empty Subarrays")

print(subArray(arr, n))