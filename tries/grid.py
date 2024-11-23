from typing import Literal

columns : list[int | float] = [9, 6, 5]
columns2 : list[int | float] = [4, 3, 8]

# columns 0 indisi columns 1 ve columns2 0 indisi ile komşu 00 01 10
# columns 1 indisi columns 0 ve columns2 1 indisi ile komşu

neighbor : Literal[0, 1] = 0


for i in range(len(columns2)):
     a : list[int | float] = [[columns[0], columns2[0]], 
                              [columns[1], columns2[1]], 
                              [columns[2], columns2[2]]]
     """x = a[i]
     x2 = a[i + 3:1]
     y = a[i + 1] """

     row_one = f' # \t{a[i - 2][0]} \t {a[i - 2][i - 1]} \t {a[i - 1][0]} \t {a[i][0]} \t {a[i][i-1]}'
     column_one = f'\n {a[i - 2][0]} \n {a[i - 2][i - 1]} \n {a[i - 1][0]} \n {a[i][0]} \n {a[i][i-1]}'
     nieghbor_grid :list[int | float] = []

     if a[i - 2] == a[0]:
          if a[i - 2][0] == a[0][0] or a[i - 2][1] == a[0][1]:
               if a[i - 2][0] >= a[i - 1][0] and a[i - 2][0] <= a[i - 1][0]:
                    print("Hello2")
                    neighbor = 1
               elif a[i - 1][0] >= a[i - 1][0] and a[i - 1][0] <= a[i - 1][1]:
                    print("Hello2")
                    neighbor = 1
               elif a[i][0] >= a[i][1] and a[i][0] <= a[i][1]:
                    print("Hello2")
                    neighbor = 0
               else :
                    neighbor = 0
          nieghbor_grid :list[int | float] = [[neighbor - 2] * (i + 2), [neighbor - 1] * (i), [neighbor] * (i)]
     #elif a[]
     
     
     
     

     """print("X: \n", x, "\n")
     print("X2: \n", x2, "\n")
     print("Y: \n", y, "\n")"""

#result :str = f' # \t {a[0][0]} \t {a[0][1]} \t {a[1][0]} \t {a[1][1]} \t {a[2][0]} \t {a[2][1]} \n {a[0][0]}  \n {a[0][1]} \n {a[1][0]} \n {a[1][1]} \n {a[2][0]} \n {a[2][1]}'
print(a)
print(row_one + column_one)
print(nieghbor_grid)


from collections import deque

# BFS from given source s
def bfs(adj, s, visited):
  
    q = deque() # Create a queue for BFS

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        curr = q.popleft() # Dequeue a vertex
        print(curr, end=" ")

        # Get all adjacent vertices of curr
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True # Mark as visited
                q.append(x) # Enqueue it

# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u) # Undirected graph

# Perform BFS for the entire graph
def bfs_disconnected(adj):
    visited = [False] * len(adj) # Not visited

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited)

# Example usage
V = 6 # Number of vertices
adj = [[] for _ in range(V)] # Adjacency list

# Add edges to the graph
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 3, 4)
add_edge(adj, 4, 5)

# Perform BFS traversal for the entire graph
bfs_disconnected(adj)

class Solution():
    def twoSum(self, nums, target):
        new_nums = []
        for i in range(0, len(nums) - 1):
            if target == nums[i] + nums[i + 1]:
                new_nums = [int(nums.index(nums[i])), int(nums.index(nums[i + 1]))]
            elif target == nums[i - 1] + nums[i + 1]:
                new_nums = [int(nums.index(nums[i])), int(nums.index(nums[2]))]
        if target == nums[0]  + nums[1] and nums[0] == nums[1]:
            new_nums = [0, 1]
        return (new_nums) 

nums1 = [3, 2, 6, 7, 8, 12, 67, 23, 65 ,12]

a = Solution()
        
print(a.twoSum(nums1, 77))

class Solution(object):
    def isPalindrome(self, x):
        check = False
        string_number = str(x)
        for i in range(0, len(string_number) - 1):
            new_number = '{}{}{}'.format(string_number[i - 2:], string_number[i], string_number[i - 1])
            new_number_int = int(new_number)
            if new_number_int == x:
                check = True
            else:
                check = False
        return check, new_number
        #print(new_number)
        #print(number_digits)

print(Solution().isPalindrome(22))
        
