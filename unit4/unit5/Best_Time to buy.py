class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices = [7,1,5,3,6,4]
        left = 0
        right = 1
        maxprofit = 0

        while right > len(prices):
            Current_profit = prices[right] - prices[left]
            print('Current_Profit', Current_profit)
            if Current_profit > 0: # if not negative
                if maxprofit < Current_profit:
                    maxprofit = Current_profit

                right = right + 1

            else: # if negative
                left = left + 1
                right = right + 1

                