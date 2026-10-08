class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        arr = [0]  + cuts
        arr.append(n)
        arr.sort()

        dp = {}

        def recursive(i , j):

            if (i , j) in dp:
                return dp[(i ,j)]

            if i > j:
                return 0

            mini = float('inf')

            for idx in range( i , j + 1):
                cost = (arr[j + 1] - arr[i - 1]) + recursive(i , idx - 1) + recursive(idx + 1 , j)
                mini = min(mini , cost)

            dp[(i ,j)] = mini
            return dp[(i , j)]

        return recursive(1 , len(cuts))
