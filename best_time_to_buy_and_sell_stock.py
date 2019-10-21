from typing import List
import argparse
from loguru import logger
import doctest

"""

NAME : Best Time to Buy and Sell Stock
LINK :
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
DESC:

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).

"""
def maxProfit(prices: List[int]) -> int:
    """
    DOCTEST
    >>> prices = [7,1,5,3,6,4]
    >>> maxProfit(prices)
    7
    
    >>> prices = [1,2,3,4,5]
    >>> maxProfit(prices)
    4
    
    >>> prices = [7,6,4,3,1]
    >>> maxProfit(prices)
    0
    
    """
    sdelka = 0 # Sell Stock
    Sum = 0
    for i in range(len(prices)):
        if ((i + 1) == len(prices)):
            if (sdelka == 1):
                sdelka = 0
                Sum += int(prices[i])
            break
        if (prices[i] < prices[i+1]) & (sdelka == 0):
            sdelka = 1 # Buy Stock
            Sum = Sum - int(prices[i])
        if (prices[i] > prices[i+1]) & (sdelka == 1):
            sdelka = 0 # Sell Stock
            Sum = Sum + int(prices[i])
    return Sum

if __name__ == "__main__":
    doctest.testmod()

    parser = argparse.ArgumentParser()
    parser.add_argument('--prices', nargs='+',
                    help='List of the price a stock',
                    required=True)
    prices = parser.parse_args().prices

    logger.info(f'Got array from command line arguments : {prices}')
    logger.info(f'Find the maximum profit ...')

    res = maxProfit(prices)
    logger.info(f'...Done')

    print('Result profit :', res)
   