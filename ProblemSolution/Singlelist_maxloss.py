# <!-- You are given an array prices where prices[i] is the price of a given stock on the i-th day.

# You want to calculate the maximum loss you could experience if you buy one stock on a day and sell it later on another day.

# Return the maximum loss (as a positive number). If no loss is possible, return 0.


# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 6
# Explanation: Buy on day 1 (price = 7), sell on day 2 (price = 1), loss = 7-1 = 6.

# Input: prices = [1, 2, 3, 4, 5]
# Output: 0
# Explanation: Prices only go up, no loss possible.

# Input: prices = [10, 8, 12, 5, 7]
# Output: 7
# Explanation: Buy at 12 (day 3) and sell at 5 (day 4), loss = 12-5 = 7. -->


from typing import List


class Solution:
    def minProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxloss = 0
        maxprice = prices[0]  # track max price seen so far

        for price in prices:
            # update max price
            if price > maxprice:
                maxprice = price
            # calculate loss if sold today
            loss = maxprice - price
            if loss > maxloss:
                maxloss = loss

        return maxloss


# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.minProfit([7, 1, 5, 3, 6, 4]))  # Output: 6
    print(solution.minProfit([1, 2, 3, 4, 5]))  # Output: 0
    print(solution.minProfit([10, 8, 12, 5, 7]))  # Output: 7
