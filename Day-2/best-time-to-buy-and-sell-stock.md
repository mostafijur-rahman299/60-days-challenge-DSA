## 121. Best Time to Buy and Sell Stock

```
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
```

### Solution
```python
class Solution:
    def maxProfit(self, prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
    
s = Solution()
s.maxProfit([7,6,4,3,1])
```

#### Time complexity analysis
```
This code appears to be a simple implementation for finding the maximum profit from a list of stock prices. 
The algorithm initializes a buy index and a sell index, iterates through the list of prices, 
and updates the max_profit whenever a better profit is found.

Let's analyze the time complexity of this code:

The while loop iterates over the list of prices from the sell index of 1 to the end. 
Therefore, the loop executes len(prices) - 1 times.

Inside the loop, the operations performed are basic comparisons, arithmetic operations, 
and updating the max_profit. These operations have a constant time complexity of O(1).

Therefore, the overall time complexity of the code is O(n), where n is the length of the list prices. 
This linear time complexity arises from the fact that the code iterates through the list only once, 
performing constant-time operations at each step.
```

#### Space complexity analysis
```
buy, sell, and max_profit are integer variables. These variables occupy constant space, 
regardless of the size of the input prices list. Therefore, they contribute O(1) to the space complexity.

The current_profit variable is also an integer, and it's created within the loop. 
It is assigned a value, but it is a temporary variable that is replaced in each iteration 
of the loop. Therefore, it doesn't add to the space complexity.

The prices list is not explicitly mentioned in your code, but assuming it's a parameter passed to the function, 
it doesn't create any additional space complexity within the function because it's just a reference to an existing list. 
The space occupied by the prices list is external to this function and not counted in its space complexity.

In summary, the space complexity of this code is O(1) because it uses a fixed and constant amount of space 
regardless of the size of the input list prices.
```

