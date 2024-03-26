# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://youtu.be/1pkOgXD63yU?si=ZbOLMQLBgL5H3QD7

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Initialize left and right pointers for the sliding window
        l = 0  # Buy
        r = 1  # Sell

        # Initialize maximum profit variable
        maxP = 0

        # Loop until the right pointer reaches the end of the prices list
        while r < len(prices):
            # Check if the price at the left pointer is less than the price at the right pointer
            if prices[l] < prices[r]:
                # Calculate the profit if buying at prices[l] and selling at prices[r]
                profit = prices[r] - prices[l]
                # Update the maximum profit if the current profit is greater
                maxP = max(profit, maxP)
            else:
                # If the price at prices[l] is not less than prices[r],
                # update the left pointer to the right pointer position
                l = r

            # Move the right pointer to the next element
            r += 1

        # Return the maximum profit obtained
        return maxP
