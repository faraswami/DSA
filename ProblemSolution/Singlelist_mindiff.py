# Problem Statement: Minimum Difference Between Any Two Elements

# You are given an integer array nums.
# Find the minimum absolute difference between any two elements in the array.

# Return the minimum difference.

# Input: nums = [4, 9, 1, 32, 13]
# Output: 3
# Explanation: The closest pair is (4, 1) with difference = 3.


# Input: nums = [10, 20, 30, 40]
# Output: 10
# Explanation: Every pair has difference of at least 10.


# Input: nums = [5, 5, 5]
# Output: 0
# Explanation: Same numbers → difference is 0.


from typing import List


class Solution:
    def mindiff(self, prices: List[int]) -> int:
        mindiff = float("inf")

        prices.sort()

        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         diff = prices[j] - prices[i]
        #         if diff < mindiff:
        #             mindiff = diff
        # return mindiff

        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            mindiff = min(mindiff, diff)
        return mindiff


if __name__ == "__main__":
    solution = Solution()
    print(solution.mindiff([20, 10, 30, 40]))
    print(solution.mindiff([5, 2, 8, 3]))
    print(solution.mindiff([7, 7, 7, 7]))
