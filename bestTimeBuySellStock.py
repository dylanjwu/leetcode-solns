class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mxrev = 0
        if(prices == None):
            return 0
        for i in range(len(prices)-1):
            if(prices[i] < prices[i+1]):
                mxrev += prices[i+1] - prices[i]
        
        return mxrev
