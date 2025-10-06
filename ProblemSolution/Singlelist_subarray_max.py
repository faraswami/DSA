# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        subarray = nums[0]
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) + 1):
                print("value of i and j", i, j)
                print("subarray", nums[i:j])
                curr_sum = sum(nums[i:j])
                if curr_sum > max_sum:
                    subarray = nums[i:j]
                    max_sum = curr_sum
                    print("subarray updated", subarray)
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([5, 4, -1, 7, 8]))
