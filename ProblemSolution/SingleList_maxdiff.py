# You are given an array of integers nums.
# Find the maximum difference between two elements such that the larger element comes after the smaller element.

# Return the maximum difference. If no such pair exists, return 0.

# Input: nums = [2, 3, 10, 6, 4, 8, 1]
# Output: 8
# Explanation: The maximum difference is 10 - 2 = 8.

# Input: nums = [7, 9, 5, 6, 3, 2]
# Output: 2
# Explanation: The maximum difference is 9 - 7 = 2.

# Input: nums = [10, 9, 8, 7]
# Output: 0
# Explanation: Since numbers only decrease, no valid pair exists.


from typing import List


class Solution:
    def maxdiff(self, prices: List[int]) -> int:
        minvalue = float("inf")
        maxdiff = 0

        for price in prices:
            if price < minvalue:
                minvalue = price
            diff = price - minvalue
            if diff > maxdiff:
                maxdiff = diff
        return maxdiff


if __name__ == "__main__":
    solution = Solution()
    results = solution.maxdiff([7, 1, 5, 3, 6, 4])
    print(results)
