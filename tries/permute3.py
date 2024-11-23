class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path, remaining):
            if not remaining:
                # No more elements to permute, add the current path to the result
                result.append(path)
                return
            for i in range(len(remaining)):
                # Recur with the current element added to the path
                # and the remaining elements excluding the current one
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        result = []
        backtrack([], nums)
        return result

# Testing the solution
array = [0, 1]
print(Solution().permute(array)) # Expected output: [[0, 1], [1, 0]]

array2 = [1]
print(Solution().permute(array2)) # Expected output: [[1]]

array3 = [1, 2, 3]
print(Solution().permute(array3)) # Expected output: [