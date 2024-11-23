def grid_paths(n, m):
     mem = {}
     
     for i in range(1, n + 1):
          mem[(i, 1)] = 1
     for j in range(1, m + 1):
          mem[(1, j)] = 1
     
     for i in range(2, n + 1):
          for j in range(2, m + 1):
               mem[(i, j)] = mem[(i - 1, j)] + mem[(i, j - 1)]
     
     return mem[(n, m)]

print(grid_paths(3, 7))
#print(grid_paths(16, 18))

N = 2
 
# printing dimension
print("The dimension : " + str(N))
 
# using list comprehension
# matrix creation of n * n
res = [list(range(0 + N * i, 0 + N * (i + 1)))
                            for i in range(N)]
 
# print result
print("The created matrix of N * N: " + str(res))

"""arr = [[1, 55, 43, 7, 12, 99], [23, 43,65, 32, 23, 12, 56]]
arr2 = ["fkgdfgjdfgkldfjgkljdf dsfgdsfsdfsdfsdfsdfsdfsd sdfs fdsf dsfds fsd fsdf sdfsd fdsf", "fkgdfgjdfgkldfjgkljdf dsfgdsfsdfsdfsdfsdfsdfsd sdfs fdsf dsfds fsd fsdf sdfsd fdsf"]

n = [False] * len(arr)
print(arr[0][2])
print(arr2[1][8])"""

"""def find_maximum_length_of_sequence(arr):
     visited = [False] * len(arr)
     length = 0
     max_length = 0
     arr_set = set(arr)
     for i in range(0, len(arr)):
          if not visited[i]:
               visited[i] = True
               length += 1
               forward = arr[i] + 1
               while forward in arr_set:
                    visited[forward] = True
                    length += 1
                    forward += 1
               backward = arr[i] - 1
               while backward in arr_set:
                    visited[backward] = True
                    length += 1
                    backward -= 1
               
               max_length = max(max_length, length)
               length = 0
     return max_length

print(find_maximum_length_of_sequence(arr))"""