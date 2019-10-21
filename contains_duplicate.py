from typing import List
import argparse
from loguru import logger


"""

NAME : Contains Duplicate

LINK :
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

DESC:
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

"""
def containdublicate(nums: List[int]) -> bool:
 
    """
    DOCTEST
    >>> nums = [1, 2, 3, 1]
    >>> containdublicate(nums)
    True
    
    >>> nums = [1, 2, 3, 4]
    >>> containdublicate(nums)
    False
    
    >>> nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    >>> containdublicate(nums)
    True

    >>> nums = [0]
    >>> containdublicate(nums)
    False
    """
    res = False
    if len(nums) == 1:
        return res
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            res = True
            break
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--nums", nargs= "+",
            help="List an array of integers",
            required=True)
    nums = parser.parse_args().nums

    logger.info(f'Got array from command line arguments : {nums}')
    logger.info(f'Contain duplicates ...')

    res = containdublicate(nums)

    logger.info(f'...Done')

    print('Result contain :', res)
    